
Nucleotides = ["A","C","G","T"]


def validate_seq(dna_seq):
    dna_seq = dna_seq.upper()
    for nuc in dna_seq:
        if nuc not in Nucleotides:
            return "Invalid seq!"
    
    return dna_seq.upper()


def count_nucleotide_freq(seq):
    nucl_freq_dict = {'A':0, 'C':0, 'G':0, 'T':0, }
    for nucl in seq:
        nucl_freq_dict[nucl] += 1
    
    return nucl_freq_dict

