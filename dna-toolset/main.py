import dna_toolkit as dtlk
import random

#test_seq = "ACGTTAGTGATGTG"

rand_seq = ''.join([random.choice(dtlk.Nucleotides) for nuc in range(60)]) # remeber, list comprehension goes from right to left

print(dtlk.validate_seq(rand_seq.lower()))

print(dtlk.count_nucleotide_freq(rand_seq))