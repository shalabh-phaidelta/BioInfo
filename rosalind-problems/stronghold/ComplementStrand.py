DNA_Reverse_Complement = {"A":"T", "T":"A", "C":"G", "G":"C"}


def reverse_complement(seq):
    #return transcription(seq[::-1])
    #return seq.maketrans("ATCG", "TAGC")[::-1]
    return "".join([DNA_Reverse_Complement[nuc] for nuc in seq])[::-1]


dna = 'CTGAGACGATCGAGGTCTACACAATCGTCTTAAATAACGGGTTGCGTAACGGCGAGGAATACAGGGTCTTTTGGACTGCCTTATGTGTCTACAAGGCCCTTGAGTCCAAAGAGAGTAACTTTGTCCCCCCTATGTGCAGAAGGTTTTCAAAGCGCAATTTTGATGCTACCGTCATAGTAAATCGGGTCGTGTCGTTACAAGCCATACACCTTGCACCCCCAATCTATCAACACTATTTGTGCGGTGCATTAGATCCTGAATCCAATCATCGGAGTTGCCCTTGTCTGTGGTTGGAGCAACAACCCAGCCAATTTCGATGTTCAGCAGGGAGAATGAAAGGGATCTCCTTCTTATGGCGATGACGTCCATATACCTGAACTAGCAGCAATAGAATTATATATCCCCGGAAAACGGATTGAGGCCTTGATGGCCAATCATAGGAGGCCATGTTATGATACTCAGAATATCGAACCGCTACAGAAGTTCCTGGTGAAGTGAGGGTGAGTGCAATGCTGCGGTTGTTGCGCGTAGAATTACTGGCGTACGCTTTGCTCATCGATTCGCCATTGATAAGTTCCCTTATAACTTCATACCCAACGTAATGGGAACGCCGGAGCGAAAGTAACGGGCTTTTGCTTGGCAAGAAGTATGCGGACGAAGTAGTCTACTCATCCAATTCAGTGCCGTTGGCCACATAGAACCCCTCGAACTGGGGTAACCCGTGTAGGACCCCGACCGAATATTAATGTTCTTATAAGGGTAGCGGGGTTTCATGAGCCCGCGGGCTCAAGTCGAGCTTCTATGGTGACCTGAATAGTTGACTCTTGCGCTGCAAAACTGAATCTAGGCATTCATACAATTTAAACAATCCTATTTTCTC'
print(reverse_complement(dna))