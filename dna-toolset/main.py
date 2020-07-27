import dna_toolkit as dtlk
import random

#test_seq = "ACGTTAGTGATGTG"

rand_seq = ''.join([random.choice(dtlk.Nucleotides) for nuc in range(6)]) # remeber, list comprehension goes from right to left

print(dtlk.validate_seq(rand_seq.lower()))

print(f"[1] Sequence length {len(rand_seq)}\n")

print(f"[2] Nucloetide frequency {dtlk.count_nucleotide_freq(rand_seq)}\n")

print(f"[3] DNA->RNA Transcription {dtlk.transcription(rand_seq)}\n")

print(f"p[4] Reverse complement of {rand_seq} is {dtlk.reverse_complement(rand_seq)}") 