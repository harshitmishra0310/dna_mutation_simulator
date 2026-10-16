"""
DNA Mutation Simulator
 
Takes a DNA sequence and a mutation type (substitution, insertion, or
deletion) and reports:
- the mutated gene
- the transcribed RNA before and after mutation
- the translated protein before and after mutation
- whether the mutation changed the resulting protein
"""
 
print("=" * 55)
print("              DNA MUTATION SIMULATOR")
print("=" * 55)
 
dna = input("\nEnter a DNA sequence: ").upper().strip()
 
if len(dna) == 0:
    print("\n✗ DNA sequence cannot be empty.")
    exit()
 
valid = True
 
for base in dna:
    if base not in "ATGC":
        valid = False
 
if valid:
    print("\n✓ DNA sequence is valid.")
else:
    print("\n✗ DNA sequence is invalid.")
    exit()
 
codon_table = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
    'UAU':'Y','UAC':'Y','UAA':'Stop','UAG':'Stop',
    'UGU':'C','UGC':'C','UGA':'Stop','UGG':'W',
 
    'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
 
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R',
 
    'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
}
 
print("\n" + "-" * 55)
print("CHOOSE MUTATION TYPE")
print("-" * 55)
 
print("1. Substitution")
print("2. Insertion")
print("3. Deletion")
 
choice = input("\nEnter your choice (1/2/3): ")
 
if choice not in ["1", "2", "3"]:
    print("\n✗ Invalid choice.")
    exit()
 
if choice == '1':
    try:
        position = int(input('\nEnter position to mutate: ')) - 1
    except ValueError:
        print("\n✗ Position must be an integer.")
        raise SystemExit(1)
 
    if position < 0 or position >= len(dna):
        print('\n✗ The position is not valid')
        exit()
 
    new_base = input('Enter base: ').upper().strip()
 
    if len(new_base) != 1 or new_base not in 'ATGC':
        print('\n✗ The base you entered is not in ATGC and is invalid')
        exit()
 
    mutated_gene = dna[:position] + new_base + dna[position+1:]
 
    print("\n" + "-" * 55)
    print("GENE SEQUENCE")
    print("-" * 55)
 
    print("Original gene :", dna)
    print("Mutated Gene  :", mutated_gene)
 
    RNA_sequenceO = dna.replace('T', 'U')
    RNA_sequence = mutated_gene.replace('T', 'U')
 
    print("\n" + "-" * 55)
    print("RNA SEQUENCE")
    print("-" * 55)
 
    print("Original RNA :", RNA_sequenceO)
    print("Mutated RNA  :", RNA_sequence)
 
    proteinO = ""
    for i in range(0, len(RNA_sequenceO) - 2, 3):
        codon = RNA_sequenceO[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        if amino_acid == "Stop":
            break
        proteinO += amino_acid
 
    protein = ""
    for i in range(0, len(RNA_sequence) - 2, 3):
        codon = RNA_sequence[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        if amino_acid == "Stop":
            break
        protein += amino_acid
 
    print("\n" + "-" * 55)
    print("PROTEIN TRANSLATION")
    print("-" * 55)
 
    print("Original protein :", proteinO)
    print("Mutated protein  :", protein)
 
    print("\n" + "-" * 55)
    print("RESULT")
    print("-" * 55)
 
    if proteinO == protein:
        print("The original protein is the same as the mutated protein")
    else:
        print("Protein sequence has changed due to mutation")
 
 
elif choice == '2':
    try:
        position1 = int(input('\nEnter position to mutate: ')) - 1
    except ValueError:
        print("\n✗ Position must be an integer.")
        raise SystemExit(1)
 
    if position1 < 0 or position1 > len(dna):
        print('\n✗ The position is not valid')
        exit()
 
    new_base1 = input('Enter base: ').upper().strip()
 
    if len(new_base1) != 1 or new_base1 not in 'ATGC':
        print('\n✗ The base you entered is not in ATGC and is invalid')
        exit()
 
    mutated_gene1 = dna[:position1] + new_base1 + dna[position1:]
 
    print("\n" + "-" * 55)
    print("GENE SEQUENCE")
    print("-" * 55)
 
    print("Original gene :", dna)
    print("Mutated Gene  :", mutated_gene1)
 
    RNA_sequenceO1 = dna.replace('T', 'U')
    RNA_sequence1 = mutated_gene1.replace('T', 'U')
 
    print("\n" + "-" * 55)
    print("RNA SEQUENCE")
    print("-" * 55)
 
    print("Original RNA :", RNA_sequenceO1)
    print("Mutated RNA  :", RNA_sequence1)
 
    proteinO1 = ""
    for i in range(0, len(RNA_sequenceO1) - 2, 3):
        codon = RNA_sequenceO1[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        if amino_acid == "Stop":
            break
        proteinO1 += amino_acid
 
    protein1 = ""
    for i in range(0, len(RNA_sequence1) - 2, 3):
        codon = RNA_sequence1[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        if amino_acid == "Stop":
            break
        protein1 += amino_acid
 
    print("\n" + "-" * 55)
    print("PROTEIN TRANSLATION")
    print("-" * 55)
 
    print("Original protein :", proteinO1)
    print("Mutated protein  :", protein1)
 
    print("\n" + "-" * 55)
    print("RESULT")
    print("-" * 55)
 
    if proteinO1 == protein1:
        print("The original protein is the same as the mutated protein")
    else:
        print("Protein sequence has changed due to mutation")
 
 
elif choice == '3':
    try:
        position2 = int(input('\nEnter the position you want to remove the gene from: ')) - 1
    except ValueError:
        print("\n✗ Position must be an integer.")
        raise SystemExit(1)
 
    if position2 < 0 or position2 >= len(dna):
        print('\n✗ The position is not valid')
        exit()
 
    mutated_gene2 = dna[:position2] + dna[position2+1:]
 
    print("\n" + "-" * 55)
    print("GENE SEQUENCE")
    print("-" * 55)
 
    print("Original gene :", dna)
    print("Mutated Gene  :", mutated_gene2)
 
    RNA_sequenceO2 = dna.replace('T', 'U')
    RNA_sequence2 = mutated_gene2.replace('T', 'U')
 
    print("\n" + "-" * 55)
    print("RNA SEQUENCE")
    print("-" * 55)
 
    print("Original RNA :", RNA_sequenceO2)
    print("Mutated RNA  :", RNA_sequence2)
 
    proteinO2 = ""
    for i in range(0, len(RNA_sequenceO2) - 2, 3):
        codon = RNA_sequenceO2[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        if amino_acid == "Stop":
            break
        proteinO2 += amino_acid
 
    protein2 = ""
    for i in range(0, len(RNA_sequence2) - 2, 3):
        codon = RNA_sequence2[i:i+3]
        amino_acid = codon_table.get(codon, "?")
        if amino_acid == "Stop":
            break
        protein2 += amino_acid
 
    print("\n" + "-" * 55)
    print("PROTEIN TRANSLATION")
    print("-" * 55)
 
    print("Original protein :", proteinO2)
    print("Mutated protein  :", protein2)
 
    print("\n" + "-" * 55)
    print("RESULT")
    print("-" * 55)
 
    if proteinO2 == protein2:
        print("The original protein is the same as the mutated protein")
    else:
        print("Protein sequence has changed due to mutation")
 
print("\n" + "=" * 55)
print("Analysis Complete!")
print("=" * 55)
 
