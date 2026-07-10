🧬 DNA Mutation Simulator

A Python based bioinformatics tool that simulates substitution, insertion, and deletion mutations in a DNA sequence, then analyzes their impact on RNA transcription, protein translation, and the resulting amino acid sequence.

This project demonstrates how a single change in DNA can influence the downstream biological processes described by the Central Dogma of Molecular Biology.

⸻

✨ Features

* 🔬 Validates user-provided DNA sequences
* 🧬 Simulates substitution mutations
* ➕ Simulates insertion mutations
* ➖ Simulates deletion mutations
* 🧪 Generates the mutated DNA sequence
* 🧫 Transcribes both original and mutated DNA into RNA sequences
* 🧬 Translates RNA into protein sequences using the standard genetic code
* ⚖️ Compares original and mutated proteins to determine whether the mutation changed the resulting protein
* 📊 Displays results in a clear, sectioned console format

⸻

🧠 Biological Workflow

Original DNA
      │
      ▼
Mutation Simulation
      │
      ▼
Mutated DNA
      │
      ▼
RNA Transcription
      │
      ▼
mRNA Sequence
      │
      ▼
Protein Translation
      │
      ▼
Protein Comparison

⸻

🧪 Mutation Types Supported

Mutation Type	Description	Example
Substitution	Replaces one nucleotide with another	A → G
Insertion	Adds a new nucleotide at a specified position	+A
Deletion	Removes a nucleotide from a specified position	-T

Insertion and deletion mutations can cause frameshift mutations, altering the codon reading frame and potentially changing the entire downstream protein sequence.

⸻

🧬 Example Run

Input

Enter a DNA sequence: ATGGCCATTGTAATGGGCCGCTGA
Choose mutation type: Substitution
Enter position to mutate: 5
Enter base: T

Output

=======================================================
              DNA MUTATION SIMULATOR
=======================================================
✓ DNA sequence is valid.
-------------------------------------------------------
GENE SEQUENCE
-------------------------------------------------------
Original gene : ATGGCCATTGTAATGGGCCGCTGA
Mutated Gene  : ATGGTCATTGTAATGGGCCGCTGA
-------------------------------------------------------
RNA SEQUENCE
-------------------------------------------------------
Original RNA : AUGGCCAUUGUAAUGGGCCGCUGA
Mutated RNA  : AUGGUCAUUGUAAUGGGCCGCUGA
-------------------------------------------------------
PROTEIN TRANSLATION
-------------------------------------------------------
Original protein : MAIVMGR
Mutated protein  : MVIVMGR
-------------------------------------------------------
RESULT
-------------------------------------------------------
Protein sequence has changed due to mutation

⸻

🧬 Understanding the Results

* Original gene shows the DNA sequence before mutation.
* Mutated gene shows the DNA sequence after the selected mutation.
* Original RNA and Mutated RNA show transcription results after replacing thymine (T) with uracil (U).
* Original protein and Mutated protein show translation results using the standard codon table.
* The Result section indicates whether the mutation changed the resulting protein sequence.

⸻

⚙️ Technologies Used

* 🐍 Python 3
* 🧬 Bioinformatics concepts
* 🔁 String manipulation
* 🔄 Loops and conditional statements
* 📚 Dictionaries for codon-to-amino-acid mapping
* 🧪 Molecular biology principles: DNA, RNA, codons, and protein translation

⸻

🚀 How to Run

1. Clone the repository:

git clone https://github.com/your-username/dna_mutation_simulator.git

2. Navigate to the project folder:

cd dna-mutation-simulator

3. Run the program:

python dna_mutation_simulator.py

4. Enter a DNA sequence and choose a mutation type when prompted.

⸻

📚 Scientific Concepts Demonstrated

* DNA sequence validation
* Point mutations
* Frameshift mutations
* RNA transcription
* Protein translation
* Codon amino acid mapping
* Mutation impact on protein structure

⸻

🎯 Learning Outcomes

This project helped strengthen my understanding of:

* Python programming and problem solving
* Biological sequence analysis
* The relationship between DNA, RNA, and proteins
* How genetic mutations can alter protein synthesis
* Computational approaches used in introductory bioinformatics

⸻

👨‍💻 Author

Harshit Mishra

Aspiring Bioinformatics student interested in computational biology, genomics, machine learning, and biomedical data analysis.

⸻

📜 License

This project is licensed under the MIT License.

⸻

⭐ If you find this project interesting, consider giving the repository a star and following my bioinformatics learning journey!
