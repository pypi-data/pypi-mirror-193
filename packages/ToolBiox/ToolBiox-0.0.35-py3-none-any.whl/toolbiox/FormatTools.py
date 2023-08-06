outfmt6_fieldnames = ["query_id", "subject_id", "identity", "alignment_length", "mismatches", "gap_openings",
                        "q_start", "q_end", "s_start", "s_end", "e_value", "bit_score"]


if __name__ == '__main__':
    import argparse

    # argument parse
    parser = argparse.ArgumentParser(
        prog='FormatTools',
    )

    subparsers = parser.add_subparsers(
        title='subcommands', dest="subcommand_name")

    # argparse for outfmt5To6
    parser_a = subparsers.add_parser('outfmt5To6',
                                     help='convert blast results from outfmt 5 to 6',
                                     description='convert blast results from outfmt 5 to 6')

    parser_a.add_argument('input_file', type=str,
                          help='input file with outfmt 5')
    parser_a.add_argument('output_file', type=str, help='output file path')

    # argparse for outfmt5complete
    parser_a = subparsers.add_parser('outfmt5complete',
                                     help='check if outfmt5 is complete')

    parser_a.add_argument('input_file', type=str,
                          help='input file with outfmt 5')

    # argparse for genblasta2BED
    parser_a = subparsers.add_parser('genblasta2BED',
                                     help='convert genblasta output to bed file')

    parser_a.add_argument('input_file', type=str,
                          help='input file with outfmt 5')
    parser_a.add_argument('output_file', type=str, help='output file path')
    parser_a.add_argument('-p', "--ID_prefix", type=str, default='subject_',
                          help='gene output name prefix defaults: subject_')

    # argparse for blast2DB
    parser_a = subparsers.add_parser('blast2DB',
                                     help='save blast results into sqlite db')

    parser_a.add_argument('input_bls', type=str,
                          help='input file with outfmt 6')
    parser_a.add_argument('db_fasta', type=str, help='output database file')
    parser_a.add_argument('-g', "--gzip_flag",
                          help='if bls is gzipped', action='store_true')

    # argparse for outfmt6ToFasta
    parser_a = subparsers.add_parser('outfmt6ToFasta',
                                     help='extract subject sequence by blast outfmt6 results')

    parser_a.add_argument('outfmt6', type=str, help='input file with outfmt 6')
    parser_a.add_argument('db_fasta', type=str,
                          help='input file with database fasta file')
    parser_a.add_argument('output_fasta', type=str, help='output file path')

    # argparse for MD5Checker
    parser_a = subparsers.add_parser('MD5Checker',
                                     help='check md5 files in whole dir')

    parser_a.add_argument('dir_path', type=str, help='path of dir to check')

    args = parser.parse_args()
    args_dict = vars(args)

    # ---------------------------------------------------------
    # command detail

    # outfmt5to6
    if args_dict["subcommand_name"] == "outfmt5To6":

        from toolbiox.lib.common.util import printer_list
        from toolbiox.api.common.genome.blast import outfmt5_read_big, keep_outfmt6_info

        input_file = args.input_file
        output_file = args.output_file

        output_dict = outfmt5_read_big(input_file, False)
        with open(output_file, 'w') as f:
            for query in output_dict:
                for hsp in keep_outfmt6_info(query):
                    f.write(printer_list(hsp) + "\n")

    elif args_dict["subcommand_name"] == "outfmt5complete":
        from toolbiox.api.common.genome.blast import outfmt5_complete

        if outfmt5_complete(args.input_file):
            print("%s is complete" % args.input_file)
        else:
            print("%s is not complete" % args.input_file)

    elif args_dict["subcommand_name"] == "genblasta2BED":
        import re
        from toolbiox.lib.common.fileIO import tsv_file_dict_parse
        """
        class abc(object):
            pass

        args = abc()

        args.input_file = '/lustre/home/xuyuxing/Work/Csp/ITS/Cau.rRNA'
        args.output_file = '/lustre/home/xuyuxing/Work/Csp/ITS/Cau.rRNA.bed'
        args.ID_prefix = 'Cau_ITS_'
        """

        def fancy_name_parse(input_string):
            contig_name, c_start, c_end = re.search(
                r'^(\S+):(\d+)\.\.(\d+)$', input_string).groups()
            return contig_name, int(c_start), int(c_end)

        gb_file = tsv_file_dict_parse(args.input_file, seq="|",
                                      fieldnames=['query_name', 'subject_name', 'strand', 'gene_cover', 'score',
                                                  'rank'])

        with open(args.output_file, 'w') as f:
            num = 0
            for i in gb_file:
                if gb_file[i]['rank'] is not None and re.match(r'rank:\d+', gb_file[i]['rank']):
                    num = num + 1

                    score = float(
                        re.search(r'score:(.*)', gb_file[i]['score']).group(1))

                    contig_name, c_start, c_end = fancy_name_parse(
                        gb_file[i]['subject_name'])

                    f.write("%s\t%d\t%d\t%s\t%f\t%s\n" % (
                        contig_name, c_start, c_end, args.ID_prefix + str(num), score, gb_file[i]['strand']))

    elif args_dict["subcommand_name"] == "outfmt6ToFasta":
        from toolbiox.lib.common.fileIO import tsv_file_dict_parse
        from pyfaidx import Fasta
        from Bio.Seq import Seq
        from Bio.SeqRecord import SeqRecord

        """
        class abc(object):
            pass

        args = abc()

        args.outfmt6 = '/lustre/home/xuyuxing/Work/Csp/Cleistogrammica/Cau.ITS.bls'
        args.db_fasta = '/lustre/home/xuyuxing/Work/Csp/ITS/Cuscuta.genome.v1.1.fasta'
        args.output_fasta = '/lustre/home/xuyuxing/Work/Csp/Cleistogrammica/Cau.ITS.seq'
        """

        blast_file = tsv_file_dict_parse(
            args.outfmt6, fieldnames=outfmt6_fieldnames)

        ref_dict = Fasta(args.db_fasta)

        with open(args.output_fasta, 'w') as f:
            for ID in blast_file:
                s_name = blast_file[ID]['subject_id']
                s_start = int(blast_file[ID]['s_start'])
                s_end = int(blast_file[ID]['s_end'])

                if s_end > s_start:
                    neg_strand = False
                    strand = "+"
                else:
                    neg_strand = True
                    strand = "-"
                    tmp = s_start
                    s_start = s_end
                    s_end = tmp

                a = ref_dict.get_seq(s_name, s_start, s_end, rc=neg_strand)
                fancy_name = "%s:%d-%d:%s" % (s_name, s_start, s_end, strand)

                contig_record = SeqRecord(
                    Seq(a.seq), id=ID, description=fancy_name)

                f.write(contig_record.format("fasta"))

    elif args_dict["subcommand_name"] == "MD5Checker":
        import os
        from toolbiox.lib.common.os import cmd_run


        def check_md5(dir_path):
            dir_path = os.path.abspath(dir_path)

            file_dir_list = os.listdir(dir_path)
            for tmp_name in file_dir_list:
                tmp_name_full_path = dir_path + "/" + tmp_name
                if os.path.isdir(tmp_name_full_path):
                    check_md5(tmp_name_full_path)
                else:
                    tmp_list = tmp_name.split("_")
                    if len(tmp_list) > 1:
                        if tmp_list[0] == 'MD5':
                            cmd_string = "md5sum -c %s" % tmp_name
                            # print(dir_path)
                            # print(cmd_string)
                            flag, output, error = cmd_run(cmd_string, cwd=dir_path, retry_max=5, silence=True,
                                                          log_file=None)
                            print(output)

        check_md5(args.dir_path)

    elif args_dict["subcommand_name"] == "blast2DB":
        from toolbiox.api.common.genome.blast import blast_to_sqlite

        blast_to_sqlite(args.db_fasta, args.input_bls, None,
                        None, 6, None, None, None, False, args.gzip_flag)


    elif args_dict["subcommand_name"] == "id_replace":
        import re
        import sys

        target_file = sys.argv[1]
        map_file = sys.argv[2]
        output_file = sys.argv[3]

        replace_dict = {}
        with open(map_file, 'r') as f:
            for each_line in f:
                each_line.strip()
                a,b = each_line.split()
                replace_dict[a] = b

        with open(output_file, 'w') as fo:
            with open(target_file, 'r') as f:
                for each_line in f:
                    each_line.strip()
                    get_list = list(set(re.findall(r'[a-zA-Z]+_\d+', each_line)))
                    num = 0
                    
                    from_string = None
                    for i in get_list:
                        if i in replace_dict:
                            num += 1
                            from_string = i

                    if num > 1:
                        raise ValueError('two more match %s' % each_line)
                    elif num == 1:
                        to_string = replace_dict[from_string]
                        each_line = each_line.replace(from_string, to_string)

                    fo.write(each_line)



