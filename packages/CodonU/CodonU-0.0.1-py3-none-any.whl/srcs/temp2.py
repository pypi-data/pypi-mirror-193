from vizualizer import plot_pr2, plot_enc, plot_neutrality

# handle = '../Results/Nucleotide/Staphylococcus_agnetis_nucleotide.fasta'
# handle = '../Results/Nucleotide/Staphylococcus_argenteus_nucleotide.fasta'
handle = '../Results/Nucleotide/human_cr_2.fasta'

min_len_hu = 300
min_len = 200

plot_neutrality(handle, min_len_threshold=min_len_hu, save_image=True,
                organism_name='Human Cr 2',
                folder_path='/home/souro/Projects/final_yr/CodonU/images')
