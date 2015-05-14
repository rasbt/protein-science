
# protein-science - Scripts and Tools

## Strip Hydrogens


Sebastian Raschka, 05/14/2015  
**Version 1.0**

<br>
<br>

<hr>
I would be happy to hear your comments and suggestions. 
Please feel free to drop me a note via
[twitter](https://twitter.com/rasbt), [email](mailto:bluewoodtree@gmail.com), or [google+](https://plus.google.com/+SebastianRaschka).
<hr>

<br>
<br>


The `strip_h.py` strips hydrogen atoms from PDB files in single file or batch mode

<br>
<br>

### Requirements:

- Python 2.7.x or Python 3.x

<br>
<br>

### Usage:

run `python strip_h.py --help` for the usage information:

<pre>
usage: strip_h.py [-h] [-i INPUT] [-o OUTPUT] [-r] [-v]

Renumber residues in a pdb file

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input PDB file or directory
  -o OUTPUT, --output OUTPUT
                        Output PDB file or directory
  -r, --recursive       Applies strip_h recursively if --input is a directory
  -v, --version         show program's version number and exit</pre>

<br>
<br>

### Example

command:

	python grab_atom_radius.py -i ./main_pdb_dir -o ./output_dir --recursive




