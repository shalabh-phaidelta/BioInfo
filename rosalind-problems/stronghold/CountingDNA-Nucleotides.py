def count_nucleotide_freq(seq):
    """Returns a dict of freq for each base"""
    nucl_freq_dict = {'A':0, 'C':0, 'G':0, 'T':0, }
    for nucl in seq:
        nucl_freq_dict[nucl] += 1
    
    return nucl_freq_dict


dna = 'CGCCACATTAATCTAGCACGTGGGTGACTGTCGCTCGGTCAGCAATTGCCCTGAAAAGGACACGATTTTGATCGCACACTCGTGACTGAAAATATGCCTTTGTGTCAGCAGTAGCACCGGTGAGAACATGCCAAGTCTCGGTCCGGTCTCGGGACGACGACTAACAAATAATCTTCACCTTGACGAACAATCTAAAAAGGACGTGCGTCGTCTCGAAAAAACTCAGATTACATCCGATTTTTGGTCGTTTAAATTGCATACCAGTGTTCCCATTACAACGAGCTCCGGGTGGGGACTATGATTCATGGACCTCAGTAGGTACGGCCCTTTTGAGAATCAGTCTTGGCCCCATTATTAACCCTTACTAATCTACCCATAGGAGCGTGCTACACCTAACTTATTTACAGACCCTGCCAGTGTAGCGCTACGTGTTAATAAGACCTCCATAAAAGTGTGAGATTAATGTTCAGTGCCGCATGCTAGAGTTGGAGTCCAAGTTCTGTTCAGACAAACATTCTACCCTTTACCATGAATGCCTCCCTTCCCTGTGGCGTGGCGGTTAGACACATACCAGCCTTCTACCACTCAGTCTCCATAACAATGAACCCAGTAGACGTATCAAAACTTTAATGAAACGGGGTAGTTAGCGTGGGTGCATAAAATCTAAGTGTAGTGGCCCCCATGACGCGGAACCCCTTTAGAGCTCCGGCCAACCCTGTATGCTTAGAGGACTCCTAGTGTCCGTTGTACTTCGGACTGTACAAGTCCATCTTTGTTAAATATAGCCGTATGACTGGACTGAACACCAAGGGCGCGTCGTAATAACG'
print(" ".join( [str(v) for k,v in count_nucleotide_freq(dna).items()] ) )