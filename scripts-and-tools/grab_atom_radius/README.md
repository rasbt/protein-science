
# protein-science - Scripts and Tools

## Grab Atom Radius

<br>
<br>

<hr>
I would be happy to hear your comments and suggestions. 
Please feel free to drop me a note via
[twitter](https://twitter.com/rasbt), [email](mailto:bluewoodtree@gmail.com), or [google+](https://plus.google.com/+SebastianRaschka).
<hr>

<br>
<br>


The `grab_atom_radius.py` script extracts atoms within a radius from a PDB file.

<br>
<br>

### Requirements:

- Python 2.7.x or Python 3.x

<br>
<br>

### Usage:

run `python grab_atom_radius.py --help` for the usage information:

<pre>
usage: grab_atom_radius.py [-h] [-r int/float] [-c X,Y,Z] [-i coordinate-ID]
                           [-o out.fasta]
                           PDBfile

Extracts atoms within a radius from a PDB file.
By default, all atoms in the PDB file are included in the calculation.

positional arguments:
  PDBfile

optional arguments:
  -h, --help            show this help message and exit
  -r int/float, --radius int/float
                        radius in Angstrom for atoms to extract (default 10.0)
  -c X,Y,Z, --coordinates X,Y,Z
                        center for extracting atoms (default "0,0,0")
  -i coordinate-ID, --include coordinate-ID
                        Coordinate lines to include (default: "ATOM,HETATM")
  -o out.fasta, --out out.fasta
                        writes atoms to an output file instead of printing it to the screen</pre>

<br>
<br>

### Example

command:

	python grab_atom_radius.py 3B7V.pdb -c 13.863,26.129,19.407 -r 7.0 -o 3B7V_rad7.pdb


![](./images/extract7.png)


