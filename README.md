# dna-toolset
DNA Toolset

Python based toolkit that creates a random string of dna/rna or allows you to enter your own string.  The appication has the following functions:

-Gets the sequence info<br/>
-Nucleotide Frequency<br/>
-Transcription<br/>
-Reverse complement<br/>
-GC conttent<br/>
-GC content in a sub-sequence<br/>
-Translated Sequence<br/>
-Codon usage<br/>
-reading frames<br/>
-All possible proteins in frames<br/>
-read/write functions for fasta samples<br/>

Example output of randomly generated string:

[Label]: Randomly generated sequence
[Sequence]: GUGGCAUAUCUCUCGGAGGGACGGUGACAAUGGGGGAACG
[Biotype]: RNA
[Length]: 40
[Nucleotide Freqency]: {'G': 17, 'U': 7, 'C': 7, 'A': 9}
[Translated]: Not a DNA sequence
[Reverse Complement]: CGUUCCCCCAUUGUCACCGUCCCUCCGAGAGAUAUGCCAC
[GC Content in DNA/RNA Sequence]: 60%
[GC Content in a DNA/RNA sub-sequence length k]: [60, 60]
[Translated sequence: ['V', 'A', 'Y', 'L', 'S', 'E', 'G', 'R', '_', 'Q', 'W', 'G', 'N']
[Codon usage (Default is L)]: {'CUC': 1.0}
[Six reading frames]: ['V', 'A', 'Y', 'L', 'S', 'E', 'G', 'R', '_', 'Q', 'W', 'G', 'N']
[Six reading frames]: ['W', 'H', 'I', 'S', 'R', 'R', 'D', 'G', 'D', 'N', 'G', 'G', 'T']
[Six reading frames]: ['G', 'I', 'S', 'L', 'G', 'G', 'T', 'V', 'T', 'M', 'G', 'E']     
[Six reading frames]: ['R', 'S', 'P', 'I', 'V', 'T', 'V', 'P', 'P', 'R', 'D', 'M', 'P']
[Six reading frames]: ['V', 'P', 'P', 'L', 'S', 'P', 'S', 'L', 'R', 'E', 'I', 'C', 'H']
[Six reading frames]: ['F', 'P', 'H', 'C', 'H', 'R', 'P', 'S', 'E', 'R', 'Y', 'A']     
[All possible proteins in frames]: []
