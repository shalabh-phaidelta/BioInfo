import dna_toolkit as dtlk
import random

from utilities import colored

#test_seq = "ACGTTAGTGATGTG"

rand_seq = ''.join([random.choice(dtlk.Nucleotides) for nuc in range(20)]) # remember, list comprehension goes from right to left

print(colored(dtlk.validate_seq(rand_seq.lower())))

print(f"[1] Sequence length {len(rand_seq)}\n")

print(colored(f"[2] Nucloetide frequency {dtlk.count_nucleotide_freq(rand_seq)}\n"))

print(f"[3] DNA->RNA Transcription {colored(dtlk.transcription(rand_seq))}\n")

print(f"p[4] Reverse complement:\n5' {colored(rand_seq)} 3'")
print(f"   {''.join(['|' for c in range(len(rand_seq))]) } ")
print(f"5' {colored(dtlk.reverse_complement(rand_seq))} 3' ") 

print(f"[6] GC Content {dtlk.gc_content(rand_seq)}")
print(f"[7] GC Subsequence Content {dtlk.gc_content_subsec(rand_seq, 10)}")