from pathlib import Path
import os

def read_file(file_path):
    """ Reading files and returning a lsit of all lines"""
    with open(file_path, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq:list):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100, 6)


print(os.getcwd())

#./rosalind-problems/stronghold/test_data/gc_content.txt
FASTA_file = read_file(Path("./test_data/gc_content.txt"))

FASTA_dict = {}

FASTA_label = ""

for line in FASTA_file:
    if '>' in line:
        FASTA_label = line
        FASTA_dict[FASTA_label] = ""
    else:
        FASTA_dict[FASTA_label]  += line

print(FASTA_dict)

result_dict = {}

for k,v in FASTA_dict.items():
    result_dict[k] = gc_content(FASTA_dict[k])

print(result_dict)

max_gc = max(result_dict, key=result_dict.get)

print(f"{max_gc[1:]} \n{result_dict[max_gc]}")