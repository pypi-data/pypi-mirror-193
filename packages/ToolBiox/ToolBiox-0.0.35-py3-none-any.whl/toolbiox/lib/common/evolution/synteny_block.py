import pandas as pd
from toolbiox.lib.common.genome.genome_feature2 import read_gff_file, GenomeFeature
from toolbiox.lib.common.genome.seq_base import read_fasta_by_faidx
from collections import OrderedDict
from toolbiox.lib.common.os import multiprocess_running
import re

class GeneLoci(GenomeFeature):
    def __init__(self, gene_id, chr_id, loci, species=None, gf=None):
        if gf:
            gf.sp_id = species
            gf.chr_id = chr_id
            gf.id = gene_id
            super(GeneLoci, self).__init__(id=gene_id, chr_loci=gf, sp_id=gf.sp_id,
                                           type=gf.type, qualifiers=gf.qualifiers, sub_features=gf.sub_features)
        else:
            super(GeneLoci, self).__init__(id=gene_id, type=None, chr_loci=None, qualifiers={},
                                           sub_features=None, chr_id=chr_id, strand=None, start=None, end=None, sp_id=species)
        self.loci = loci
        self.gf = gf

    def __str__(self):
        return "%s: No. %d gene on %s from %s" % (self.id, self.loci, self.chr_id, self.sp_id)


class Genome(object):
    def __init__(self, species_prefix, gff3_file=None, fasta_file=None):
        self.chr_dict = {}
        self.gene_dict = {}
        self.chr_length_dict = {}
        self.id = species_prefix

        if gff3_file:
            gff_dict = read_gff_file(gff3_file)

            chr_dict = {}
            gene_dict = {}
            for i in gff_dict['gene']:
                gf = gff_dict['gene'][i]
                if not gf.chr_id in chr_dict:
                    chr_dict[gf.chr_id] = []
                chr_dict[gf.chr_id].append(gf)
                gene_dict[gf.id] = gf

            for chr_id in chr_dict:
                chr_dict[chr_id] = sorted(
                    chr_dict[chr_id], key=lambda x: x.start)

            chr_gene_id_dict = {}
            for chr_id in chr_dict:
                chr_gene_id_dict[chr_id] = [i.id for i in chr_dict[chr_id]]

            self.chr_dict = {}
            self.gene_dict = {}
            for chr_id in chr_gene_id_dict:
                num = 0
                self.chr_dict[chr_id] = OrderedDict()
                for gene_id in chr_gene_id_dict[chr_id]:
                    gene = GeneLoci(gene_id, chr_id, num,
                                    species_prefix, gene_dict[gene_id])
                    self.chr_dict[chr_id][num] = gene
                    self.gene_dict[gene_id] = gene
                    num += 1

            self.chr_length_dict = {}
            if fasta_file:
                fa_dict = read_fasta_by_faidx(fasta_file)
                self.chr_length_dict = {i: fa_dict[i].len() for i in fa_dict}


class GenePair(object):
    def __init__(self, q_gene, s_gene, property_dict=None):
        self.q_gene = q_gene
        self.s_gene = s_gene
        self.property = property_dict

    def __str__(self):
        return "%s vs %s" % (self.q_gene.id, self.s_gene.id)

    def reverse_myself(self):
        new_GP = GenePair(self.s_gene, self.q_gene, self.property)
        return new_GP


class SyntenyBlock(object):
    def __init__(self, sb_id, q_sp, s_sp, strand, gene_pair_dict, property_dict, parameter_dict):
        self.id = sb_id
        self.property = property_dict
        self.parameter = parameter_dict
        self.strand = strand
        self.q_sp = q_sp
        self.s_sp = s_sp
        self.gene_pair_dict = gene_pair_dict

        if len(gene_pair_dict) > 0:
            self.get_info()

    def get_info(self):
        self.q_chr = self.gene_pair_dict[0].q_gene.chr_id
        self.s_chr = self.gene_pair_dict[0].s_gene.chr_id

        q_gene_list = sorted(
            [self.gene_pair_dict[i].q_gene for i in self.gene_pair_dict], key=lambda x: x.loci)
        self.first_q_gene = q_gene_list[0]
        self.last_q_gene = q_gene_list[-1]

        s_gene_list = sorted(
            [self.gene_pair_dict[i].s_gene for i in self.gene_pair_dict], key=lambda x: x.loci)
        self.first_s_gene = s_gene_list[0]
        self.last_s_gene = s_gene_list[-1]

        self.first_q_gene_loci = self.first_q_gene.loci
        self.last_q_gene_loci = self.last_q_gene.loci
        self.first_s_gene_loci = self.first_s_gene.loci
        self.last_s_gene_loci = self.last_s_gene.loci

        self.query_from = min([self.first_q_gene.gf.start, self.first_q_gene.gf.end,
                               self.last_q_gene.gf.start, self.last_q_gene.gf.end])
        self.query_to = max([self.first_q_gene.gf.start, self.first_q_gene.gf.end,
                             self.last_q_gene.gf.start, self.last_q_gene.gf.end])

        self.subject_from = min([self.first_s_gene.gf.start, self.first_s_gene.gf.end,
                                 self.last_s_gene.gf.start, self.last_s_gene.gf.end])
        self.subject_to = max([self.first_s_gene.gf.start, self.first_s_gene.gf.end,
                               self.last_s_gene.gf.start, self.last_s_gene.gf.end])

    def get_full_info(self, q_genome, s_genome):
        self.get_info()

        self.query_gene_list = []
        for i in range(self.first_q_gene_loci, self.last_q_gene_loci + 1):
            self.query_gene_list.append(q_genome.chr_dict[self.q_chr][i])

        self.subject_gene_list = []
        for i in range(self.first_s_gene_loci, self.last_s_gene_loci + 1):
            self.subject_gene_list.append(s_genome.chr_dict[self.s_chr][i])

    def reverse_myself(self, new_sb_id=None):
        gene_pair_dict = {
            i: self.gene_pair_dict[i].reverse_myself() for i in self.gene_pair_dict}
        if new_sb_id is None:
            new_sb_id = self.id

        new_sb = SyntenyBlock(new_sb_id, self.s_sp, self.q_sp,
                              self.strand, gene_pair_dict, self.property, self.parameter)

        new_sb.q_chr = new_sb.gene_pair_dict[0].q_gene.chr_id
        new_sb.s_chr = new_sb.gene_pair_dict[0].s_gene.chr_id

        new_sb.query_gene_list = self.subject_gene_list
        new_sb.subject_gene_list = self.query_gene_list

        new_sb.first_q_gene = self.first_s_gene
        new_sb.last_q_gene = self.last_s_gene
        new_sb.first_s_gene = self.first_q_gene
        new_sb.last_s_gene = self.last_q_gene

        new_sb.first_q_gene_loci = new_sb.first_q_gene.loci
        new_sb.last_q_gene_loci = new_sb.last_q_gene.loci
        new_sb.first_s_gene_loci = new_sb.first_s_gene.loci
        new_sb.last_s_gene_loci = new_sb.last_s_gene.loci

        new_sb.query_from = self.subject_from
        new_sb.query_to = self.subject_to
        new_sb.subject_from = self.query_from
        new_sb.subject_to = self.query_to

        return new_sb

    def __str__(self):

        return "Q = %s:%s gene: %d-%d (%d) base: %d-%d (%d) vs S = %s:%s gene: %d-%d (%d) base: %d-%d (%d), %s, have %d gene pair" % (self.q_sp, self.q_chr, self.first_q_gene_loci, self.last_q_gene_loci, self.last_q_gene_loci - self.first_q_gene_loci + 1,  self.query_from, self.query_to, self.query_to - self.query_from + 1, self.s_sp, self.s_chr, self.first_s_gene_loci, self.last_s_gene_loci, self.last_s_gene_loci - self.first_s_gene_loci + 1,   self.subject_from, self.subject_to, self.subject_to - self.subject_from + 1, self.strand, len(self.gene_pair_dict))

    __repr__ = __str__


class wgdi_collinearity:
    def __init__(self, options, points):
        self.gap_penality = -1
        self.over_length = 0
        self.mg1 = 40
        self.mg2 = 40
        self.pvalue = 1
        self.over_gap = 5
        self.points = points
        self.p_value = 0
        self.coverage_ratio = 0.8
        for k, v in options:
            setattr(self, str(k), v)
        if hasattr(self, 'grading'):
            self.grading = [int(k) for k in self.grading.split(',')]
        else:
            self.grading = [50, 40, 25]
        # if hasattr(self, 'mg'):
        #     self.mg1, self.mg2 = [int(k) for k in self.mg.split(',')]
        # else:
        #     self.mg1, self.mg2 = [40, 40]
        self.pvalue = float(self.pvalue)
        self.coverage_ratio = float(self.coverage_ratio)

    def get_martix(self):
        self.points['usedtimes1'] = 0
        self.points['usedtimes2'] = 0
        self.points['times'] = 1
        self.points['score1'] = self.points['grading']
        self.points['score2'] = self.points['grading']
        self.points['path1'] = self.points.index.to_numpy().reshape(
            len(self.points), 1).tolist()
        self.points['path2'] = self.points['path1']
        self.points_init = self.points.copy()
        self.mat_points = self.points

    def run(self):
        self.get_martix()
        self.score_matrix()
        data = []
        # plus
        points1 = self.points[['loc1', 'loc2',
                               'score1', 'path1', 'usedtimes1']]
        points1 = points1.sort_values(by=['score1'], ascending=[False])
        points1.drop(
            index=points1[points1['usedtimes1'] < 1].index, inplace=True)
        points1.columns = ['loc1', 'loc2', 'score', 'path', 'usedtimes']
        while (self.over_length >= self.over_gap or len(points1) >= self.over_gap):
            if self.maxPath(points1):
                if self.p_value > self.pvalue:
                    continue
                data.append([self.path, self.p_value, self.score])
        # minus
        points2 = self.points[['loc1', 'loc2',
                               'score2', 'path2', 'usedtimes2']]
        points2 = points2.sort_values(by=['score2'], ascending=[False])
        points2.drop(
            index=points2[points2['usedtimes2'] < 1].index, inplace=True)
        points2.columns = ['loc1', 'loc2', 'score', 'path', 'usedtimes']
        while (self.over_length >= self.over_gap) or (len(points2) >= self.over_gap):
            if self.maxPath(points2):
                if self.p_value > self.pvalue:
                    continue
                data.append([self.path, self.p_value, self.score])
        return data

    def score_matrix(self):
        for index, row, col in self.points[['loc1', 'loc2', ]].itertuples():
            points = self.points[(self.points['loc1'] > row) & (self.points['loc2'] > col) & (
                self.points['loc1'] < row+self.mg1) & (self.points['loc2'] < col+self.mg2)]
            row_i_old, gap = row, self.mg2
            for index_ij, row_i, col_j, grading in points[['loc1', 'loc2', 'grading']].itertuples():
                if col_j - col > gap and row_i > row_i_old:
                    break
                s = grading + (row_i-row+col_j-col)*self.gap_penality
                s1 = s+self.points.at[index, 'score1']
                if s > 0 and self.points.at[index_ij, 'score1'] < s1:
                    self.points.at[index_ij, 'score1'] = s1
                    self.points.at[index, 'usedtimes1'] += 1
                    self.points.at[index_ij, 'usedtimes1'] += 1
                    self.points.at[index_ij,
                                   'path1'] = self.points.at[index, 'path1']+[index_ij]
                    gap = min(col_j-col, gap)
                    row_i_old = row_i
        points_revese = self.points.sort_values(
            by=['loc1', 'loc2'], ascending=[False, True])
        for index, row, col in points_revese[['loc1', 'loc2']].itertuples():
            points = points_revese[(points_revese['loc1'] < row) & (points_revese['loc2'] > col) & (
                points_revese['loc1'] > row-self.mg1) & (points_revese['loc2'] < col+self.mg2)]
            row_i_old, gap = row, self.mg2
            for index_ij, row_i, col_j, grading in points[['loc1', 'loc2', 'grading']].itertuples():
                if col_j - col > gap and row_i < row_i_old:
                    break
                s = grading + (row-row_i+col_j-col)*self.gap_penality
                s1 = s + self.points.at[index, 'score2']
                if s > 0 and self.points.at[index_ij, 'score2'] < s1:
                    self.points.at[index_ij, 'score2'] = s1
                    self.points.at[index, 'usedtimes2'] += 1
                    self.points.at[index_ij, 'usedtimes2'] += 1
                    self.points.at[index_ij,
                                   'path2'] = self.points.at[index, 'path2']+[index_ij]
                    gap = min(col_j-col, gap)
                    row_i_old = row_i
        return self.points

    def maxPath(self, points):
        if len(points) == 0:
            self.over_length = 0
            return False
        self.score, self.path_index = points.loc[points.index[0], [
            'score', 'path']]
        self.path = points[points.index.isin(self.path_index)]
        self.over_length = len(self.path_index)
        # Whether the block overlaps with other blocks
        if self.over_length >= self.over_gap and len(self.path)/self.over_length > self.coverage_ratio:
            points.drop(index=self.path.index, inplace=True)
            [[loc1_min, loc2_min], [loc1_max, loc2_max]] = self.path[[
                'loc1', 'loc2']].agg(['min', 'max']).to_numpy()
            # calculate pvalues
            gap_init = self.points_init[(loc1_min <= self.points_init['loc1']) & (self.points_init['loc1'] <= loc1_max) &
                                        (loc2_min <= self.points_init['loc2']) & (self.points_init['loc2'] <= loc2_max)].copy()
            self.p_value = self.pvalue_estimated(
                gap_init, loc1_max-loc1_min+1, loc2_max-loc2_min+1)
            self.path = self.path.sort_values(by=['loc1'], ascending=[True])[
                ['loc1', 'loc2']]
            return True
        else:
            points.drop(index=points.index[0], inplace=True)
        return False

    def pvalue_estimated(self, gap, L1, L2):
        N1 = gap['times'].sum()
        N = len(gap)
        self.points_init.loc[gap.index, 'times'] += 1
        m = len(self.path)
        a = (1-self.score/m/self.grading[0])*(N1-m+1)/N*(L1-m+1)*(L2-m+1)/L1/L2
        return round(a, 4)


def run_wgdi_collinearity(loc_pair_list, min_size=5, max_gap=25, max_pvalue=1, min_score=50, gap_penality=-1, **kargs):
    """
    loc_pair_list = [
        (8, 1618), # loc of homo gene pair
        (11, 273),
    ]

    return data.append([self.path, self.p_value, self.score])
    """

    loc_pair_list = sorted(loc_pair_list, key=lambda x: x[0])

    options = {
        "gap_penality": gap_penality,
        "over_length": 0,
        # The maximum gap(mg) value is an important parameter for detecting collinear regions.
        "mg1": max_gap,
        # The maximum gap(mg) value is an important parameter for detecting collinear regions.
        "mg2": max_gap,
        # Evaluate the compactness and uniqueness of collinear blocks, the range is 0-1, and the better collinearity range is 0-0.2.
        "pvalue": 1,
        "over_gap": 5,
        "p_value": 0,
        "coverage_ratio": 0.8,
    }

    for i in kargs:
        options[i] = kargs[i]

    loc1 = [i[0] for i in loc_pair_list]
    loc2 = [i[1] for i in loc_pair_list]

    df = pd.DataFrame(
        {
            'loc1': loc1,
            'loc2': loc2,
            'grading': 50,
        }
    )

    options = [(i, options[i]) for i in options]
    my_collinearity = wgdi_collinearity(
        options, df)

    data = my_collinearity.run()
    data = [i for i in data if len(
        i[0]) >= min_size and i[1] <= max_pvalue and i[2] >= min_score]

    return data


def get_synteny_block(gene_pair_list, min_size=5, max_gap=25, max_pvalue=1, min_score=50, gap_penality=-1):
    loc_pair_list = [(gp.q_gene.loci, gp.s_gene.loci) for gp in gene_pair_list]

    q_sp = gene_pair_list[0].q_gene.sp_id
    s_sp = gene_pair_list[0].s_gene.sp_id

    q_gene_dict = {gp.q_gene.loci: gp.q_gene for gp in gene_pair_list}
    s_gene_dict = {gp.s_gene.loci: gp.s_gene for gp in gene_pair_list}

    parameter_dict = {
        "min_size": min_size,
        "max_gap": max_gap,
        "max_pvalue": max_pvalue,
        "min_score": min_score,
        "gap_penality": gap_penality
    }

    wgdi_out_list = run_wgdi_collinearity(
        loc_pair_list, min_size, max_gap, max_pvalue, min_score, gap_penality)

    num = 0
    output_dict = OrderedDict()
    for wgdi_out in wgdi_out_list:
        sb_df, p_value, score = wgdi_out

        property_dict = {
            'score': score,
            'p_value': p_value,
            'gene_pair_num': len(sb_df),
        }

        a, b = sb_df['loc2'].head(2).values
        if a < b:
            strand = '+'
        else:
            strand = '-'

        gene_pair_dict = OrderedDict([(i, GenePair(
            q_gene_dict[sb_df.iloc[i].loc1], s_gene_dict[sb_df.iloc[i].loc2])) for i in range(len(sb_df))])

        sb = SyntenyBlock(num, q_sp, s_sp, strand,
                          gene_pair_dict, property_dict, parameter_dict)

        output_dict[num] = sb
        num += 1

    return output_dict


class GenomeSyntenyBlockJob(object):
    def __init__(self, sp1_id, sp1_gff, sp2_id=None, sp2_gff=None, gene_pair_file=None, sb_options=None):
        self.sp1_id = sp1_id
        self.sp1_gff = sp1_gff
        self.sp2_id = sp2_id
        self.sp2_gff = sp2_gff
        self.gene_pair_file = gene_pair_file

        self.sb_options = OrderedDict([
            ("min_size", 5),
            ("max_gap", 25),
            ("max_pvalue", 1),
            ("min_score", 50),
            ("gap_penality", -1)
        ])

        if sb_options:
            for i in sb_options:
                self.sb_options[i] = sb_options[i]

        self.sp1 = Genome(sp1_id, sp1_gff)
        if sp2_gff:
            self.sp2 = Genome(sp2_id, sp2_gff)
        else:
            self.sp2 = None

    def read_gene_pair(self, gene_pair_file, sp1, sp2=None):
        gene_pair_list = []
        with open(gene_pair_file, 'r') as f:
            for l in f:
                gene_id1, gene_id2 = l.strip().split()
                if sp2:
                    gp = GenePair(
                        sp1.gene_dict[gene_id1], sp2.gene_dict[gene_id2])
                    gene_pair_list.append(gp)
                else:
                    gp = GenePair(
                        sp1.gene_dict[gene_id1], sp1.gene_dict[gene_id2])
                    gene_pair_list.append(gp)
        return gene_pair_list

    def build_synteny_blocks(self, threads=8):
        self.gene_pair_list = self.read_gene_pair(
            self.gene_pair_file, self.sp1, self.sp2)

        sp1_chr_list = list(self.sp1.chr_dict.keys())
        if self.sp2:
            sp2_chr_list = list(self.sp2.chr_dict.keys())
            tmp_sp2_id = self.sp2_id
        else:
            sp2_chr_list = sp1_chr_list
            tmp_sp2_id = self.sp1_id

        sb_args = [self.sb_options[i] for i in self.sb_options]

        args_list = []
        args_id_list = []
        mlt_out = {}
        for q_chr in sp1_chr_list:
            for s_chr in sp2_chr_list:
                chr_gene_pair_list = []
                for gp in self.gene_pair_list:
                    if gp.q_gene.sp_id == self.sp1_id and gp.q_gene.chr_id == q_chr and gp.s_gene.sp_id == tmp_sp2_id and gp.s_gene.chr_id == s_chr:
                        chr_gene_pair_list.append(gp)
                    elif gp.s_gene.sp_id == self.sp1_id and gp.s_gene.chr_id == q_chr and gp.q_gene.sp_id == tmp_sp2_id and gp.q_gene.chr_id == s_chr:
                        chr_gene_pair_list.append(gp.reverse_myself)
                if len(chr_gene_pair_list):
                    if threads == 1:
                        mlt_out[((self.sp1_id, q_chr), (tmp_sp2_id, s_chr))] = {}
                        mlt_out[((self.sp1_id, q_chr), (tmp_sp2_id, s_chr))]['output'] = get_synteny_block(*tuple([chr_gene_pair_list] + sb_args))
                    args_list.append(tuple([chr_gene_pair_list] + sb_args))
                    args_id_list.append(
                        ((self.sp1_id, q_chr), (tmp_sp2_id, s_chr)))

        if threads > 1:
            mlt_out = multiprocess_running(
                get_synteny_block, args_list, threads, silence=False, args_id_list=args_id_list, timeout=None)
        self.synteny_blocks_dict = {i: mlt_out[i]['output'] for i in mlt_out}

        num = 0
        self.synteny_block_dict = OrderedDict()
        for chr_pair_info in self.synteny_blocks_dict:
            for sb_id in self.synteny_blocks_dict[chr_pair_info]:
                sb = self.synteny_blocks_dict[chr_pair_info][sb_id]
                self.synteny_block_dict[num] = sb
                num += 1


    def get_mcscan_parameter(self, mcscanx_collinearity_file):
        parameter_dict = OrderedDict()
        with open(mcscanx_collinearity_file, 'r') as f:
            for each_line in f:
                # statistics
                mobj = re.match(
                    r"# Number of collinear genes: (\d+), Percentage: (\d+\.\d+)", each_line)
                if mobj:
                    gene_in_coll, percentage = mobj.groups()
                    gene_in_coll, percentage = int(gene_in_coll), float(percentage)

                mobj = re.match(r"# Number of all genes: (\d+)", each_line)
                if mobj:
                    all_gene = mobj.groups()[0]
                    all_gene = int(all_gene)

                # statistics wgdi xyx
                mobj = re.match(
                    r"# Number of collinear gene pairs: (\d+), Percentage: (\d+\.\d+)%", each_line)
                if mobj:
                    gene_in_coll, percentage = mobj.groups()
                    gene_in_coll, percentage = int(gene_in_coll), float(percentage)

                mobj = re.match(r"# Number of all gene pairs: (\d+)", each_line)
                if mobj:
                    all_gene = mobj.groups()[0]
                    all_gene = int(all_gene)


                # Parameters
                mobj = re.findall(r"^# (\S+): (\S+)$", each_line)
                if len(mobj) > 0:
                    p,v = mobj[0]
                    bad_flag = False
                    try:
                        v = float(v)
                    except:
                        bad_flag = True
                    if bad_flag is False:
                        parameter_dict[p] = v

        parameter_dict["gene_in_coll"] = gene_in_coll
        parameter_dict["percentage"] = percentage
        parameter_dict["all_gene"] = all_gene

        return parameter_dict

    def write_mcscan_output(self, mcscan_output_file):

        sb_gp_num = 0
        for i in self.synteny_block_dict:
            sb = self.synteny_block_dict[i]
            sb_gp_num += sb.property['gene_pair_num']

        with open(mcscan_output_file, 'w') as f:
            f.write("############### Parameters ###############\n# MIN_SIZE: %d\n# MAX_GAP: %d\n# MAX_PVALUE: %.2f\n# MIN_SCORE: %d\n# GAP_PENALITY: %d\n" % tuple(
                [self.sb_options[i] for i in self.sb_options]))
            f.write("############### Statistics ###############\n# Number of collinear gene pairs: %d, Percentage: %.2f%%\n# Number of all gene pairs: %d\n##########################################\n" % (
                sb_gp_num, sb_gp_num/len(self.gene_pair_list)*100, len(self.gene_pair_list)))

            for num in self.synteny_block_dict:
                sb = self.synteny_block_dict[num]
                s = "## Alignment %d: score=%.1f e_value=%.3e N=%d %s&%s %s" % (
                    num, sb.property['score'], sb.property['p_value'], sb.property['gene_pair_num'], sb.q_chr, sb.s_chr, "+" if sb.strand == "+" else "-")
                f.write(s + "\n")
                for gp_id in sb.gene_pair_dict:
                    gp = sb.gene_pair_dict[gp_id]
                    s = "  %s-  %s:\t%s\t%s\t0" % (str(num),
                                                    str(gp_id), gp.q_gene.id, gp.s_gene.id)
                    f.write(s + "\n")

    def read_mcscan_output(self, mcscan_output_file, sp1_self_flag=False):
        mcscan_parameter = self.get_mcscan_parameter(mcscan_output_file)

        self.synteny_block_dict = OrderedDict()

        with open(mcscan_output_file, 'r') as f:
            for each_line in f:
                # Block title
                mobj = re.match(
                    r"## Alignment (\S+): score=(\S+) e_value=(\S+) N=(\S+) (\S+)&(\S+) (\S+)", each_line)
                if mobj:
                    align_id, score, e_value, gene_pair_num, q_chr, s_chr, strand = mobj.groups()

                    align_id, score, e_value, gene_pair_num, q_chr, s_chr, strand = align_id, float(
                        score), float(e_value), int(gene_pair_num), q_chr, s_chr, strand
                    if strand == 'plus' or strand == '+':
                        strand = "+"
                    elif strand == 'minus' or strand == '-':
                        strand = "-"
                    else:
                        raise

                    property_dict = {
                        'score': score,
                        'e_value': e_value,
                        'gene_pair_num': gene_pair_num,
                    }

                    if sp1_self_flag:
                        self.synteny_block_dict[align_id] = SyntenyBlock(
                            align_id, self.sp1_id, self.sp1_id, strand, {}, property_dict, mcscan_parameter)
                    else:
                        self.synteny_block_dict[align_id] = SyntenyBlock(
                            align_id, self.sp1_id, self.sp2_id, strand, {}, property_dict, mcscan_parameter)

                # block line
                if re.match("^#", each_line):
                    continue
                else:
                    if align_id not in self.synteny_block_dict:
                        continue

                    align_id = each_line.split("-", 1)[0]
                    pair_id = each_line.split("-", 1)[1].split(":", 1)[0]

                    align_id = re.sub(r'\s+', '', align_id)
                    pair_id = int(re.sub(r'\s+', '', pair_id))

                    q_gene_id, s_gene_id, e_value = each_line.split(
                        "-", 1)[1].split(":", 1)[1].split()
                    align_id, pair_id, q_gene_id, s_gene_id, e_value = align_id, pair_id, q_gene_id, s_gene_id, float(
                        e_value)

                    if sp1_self_flag:
                        q_gene = self.sp1.gene_dict[q_gene_id]
                        s_gene = self.sp1.gene_dict[s_gene_id]                   
                    else:
                        q_gene = self.sp1.gene_dict[q_gene_id]
                        s_gene = self.sp2.gene_dict[s_gene_id]

                    property_dict = {'e_value': e_value}

                    self.synteny_block_dict[align_id].gene_pair_dict[pair_id] = GenePair(
                        q_gene, s_gene, property_dict)

        for align_id in self.synteny_block_dict:
            if sp1_self_flag:
                self.synteny_block_dict[align_id].get_full_info(self.sp1, self.sp1)
            else:
                self.synteny_block_dict[align_id].get_full_info(self.sp1, self.sp2)

if __name__ == '__main__':

    sp1_id = 'Cca'
    sp1_gff = '/lustre/home/xuyuxing/tmp/T49390N0.genome.gff3'
    sp2_id = 'Sly'
    sp2_gff = '/lustre/home/xuyuxing/tmp/T4081N0.genome.gff3'
    gene_pair_file = '/lustre/home/xuyuxing/tmp/mcscanx.homology'

    # build synteny blocks
    sb_job = GenomeSyntenyBlockJob(
        sp1_id, sp1_gff, sp2_id, sp2_gff, gene_pair_file)
    sb_job.build_synteny_blocks()

    mcscan_output_file = "/lustre/home/xuyuxing/tmp/mcscanx.collinearity"
    sb_job.write_mcscan_output(mcscan_output_file)

    # load synteny blocks

    sb_job = GenomeSyntenyBlockJob(
        sp1_id, sp1_gff, sp2_id, sp2_gff)
    sb_job.read_mcscan_output(mcscan_output_file)
