# gene analysis

from collections import Counter
from itertools import chain
import matplotlib.pyplot as plt

from prince import PCA
import pandas as pd
from Bio.Data.CodonTable import unambiguous_dna_by_id
from Bio.SeqIO import parse
from analyzer.internal_comp import filter_reference


def plot_MCA_1(gene_lst: list, gene_id: int):
    codons = [codon for codon, _ in unambiguous_dna_by_id[gene_id].forward_table.items()]
    gene_names = [f'gene_{i}' for i in range(len(gene_lst))]
    len_lst = [len(gene) for gene in gene_lst]
    s = []
    # organisms = []
    # for name in lst:
    #     _organism = name.split('/')[-1]
    #     organisms.append(_organism.split('.')[0].split('_')[1])
    contingency_table = pd.DataFrame(index=gene_names, columns=codons)
    # print(contingency_table)
    for idx, gene in enumerate(gene_lst):
        #     records = parse(handle, 'fasta')
        #     reference = filter_reference(records, 300)
        # sequences = (gene[i: i + 3].upper() for i in range(0, len(gene), 3))
        sequences = ((sequence[i:i + 3].upper() for i in range(0, len(sequence), 3)) for sequence in [gene])
        # for i in sequences:
        #     print(i)
        _codons = chain.from_iterable(sequences)
        counts = Counter(_codons)
        # print(counts)
        for codon in codons:
            contingency_table[codon][gene_names[idx]] = counts[codon]
        s.append(len(gene) / max(len_lst) * 100)
    # print(contingency_table)
    # pca = PCA(random_state=42, n_components=59)
    pca = PCA(random_state=42)
    pca.fit(contingency_table)
    plot_df = pca.row_coordinates(contingency_table)
    print(plot_df)
    x = plot_df.iloc[:, 0]
    y = plot_df.iloc[:, 1]
    plt.scatter(x, y, s, alpha=0.5, c=s, cmap='viridis')
    plt.colorbar()
    plt.show()
    # print(pca.explained_inertia_)
    # ax = pca.plot_row_coordinates(contingency_table)
    # ax.get_figure().savefig('test.png')

    # mca_ben = mca.MCA(contingency_table)


if __name__ == '__main__':
    # lst = [
    #     '../Results/Nucleotide/Staphylococcus_agnetis_nucleotide.fasta',
    #     '../Results/Nucleotide/Staphylococcus_argenteus_nucleotide.fasta'
    #     # '../Results/Nucleotide/human_cr_2.fasta'
    # ]
    records = parse('../Results/Nucleotide/Staphylococcus_agnetis_nucleotide.fasta', 'fasta')
    lst = filter_reference(records, 300)
    plot_MCA_1(lst, 11)
