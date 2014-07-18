
# protein-science - Scripts and Tools

## PDB to FASTA

<br>
<br>


A script that converts amino acid residues from PDB files into a FASTA string

<br>
<br>

### Requirements:

- Python 2.7.x or Python 3.x

<br>
<br>

### Usage:

run `python pdb_to_fasta.py --help` for the usage information:

<pre>
usage: pdb_to_fasta.py [-h] [-l] [-o out.fasta] PDBfile

Converts amino acid residues from PDB file into a FASTA string

positional arguments:
  PDBfile

optional arguments:
  -h, --help            show this help message and exit
  -l, --ligand          includes HETATM residues.
  -o out.fasta, --out out.fasta
                        writes FASTA strings to an output file instead of printing it to the screen

</pre>

<br>
<br>

### Example

command:

	python pdb_to_fasta.py 3B7V.pdb -o 3B7V.fasta



![](./images/fasta.png)

