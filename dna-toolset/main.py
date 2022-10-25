# DNA Toolset/Code testing file

from bio_seq import bio_seq #*** import class from bio_seq.py ****#
from utilities import read_FASTA, readTextFile, writeTextFile 

#test_dna = bio_seq("CACACATAGCTTGATAAGCCTACCAGCCCCGCAATTTGAAACGGATGTAT")
test_dna = bio_seq("")

test_dna.generate_rnd_seq(40, "RNA")

print(test_dna.get_seq_info())
print(f'[Nucleotide Freqency]: {test_dna.nucleotide_frequency()}')
print(f'[Translated]: {test_dna.transcription()}')
print(f'[Reverse Complement]: {test_dna.reverse_complement()}')
print(f'[GC Content in DNA/RNA Sequence]: {test_dna.gc_content()}%')
print(f'[GC Content in a DNA/RNA sub-sequence length k]: {test_dna.gc_content_subsec()}')
print(f'[Translated sequence: {test_dna.translate_seq()}')
print(f'[Codon usage (Default is L)]: {test_dna.codon_usage("L")}')

for rf in test_dna.gen_reading_frames():
    print(f'[Six reading frames]: {rf}')


print(f'[All possible proteins in frames]: {test_dna.all_proteins_from_orfs()}')

writeTextFile("test.txt", test_dna.seq)
for rf in test_dna.gen_reading_frames():
    writeTextFile("test.txt", str(rf), 'a')

#fasta = read_FASTA("fasta_samples.txt")
#print(fasta)
