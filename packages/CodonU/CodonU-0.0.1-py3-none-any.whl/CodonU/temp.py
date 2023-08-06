from CodonU.correspondence_analysis import mca_codon_freq
from Bio.SeqIO import parse

handle = '../Results/Nucleotide/Staphylococcus_agnetis_nucleotide.fasta'
mca_codon_freq(handle, 11, n_components=2)
