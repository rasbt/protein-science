
# protein-science - Scripts and Tools

## Renumber PDB Atoms and Residues



Sebastian Raschka, 10/22/2014  
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


The `renumber_pdb.py` script renumbers atoms and/or residues in a PDB file.

### Requirements:

- Python 2.7.x or Python 3.x

<br>
<br>

### Usage:

run `python renumber_pdb.py --help` for the usage information:

<pre>
usage: renumber_pdb.py [-h] [-i INPUT] [-s START] [-a] [-r] [-c]

Renumber residues in a pdb file

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input PDB file
  -s START, --start START
                        Number of the first residue in the renumbered file (default = 1)
  -a, --atoms           Renumbers atoms
  -r, --residues        Renumbers residues
  -c, --chainreset      Resets the residue renumbering after encountering a new chain.
  -v, --version         show program's version number and exit
</pre>

<br>
<br>

## Example

### Command:

	python renumber_pdb.py -i examples/example_1.pdb -a -r  > examples/out_1.pdb

### Input:
<pre>
ATOM    774  N   LYS A 105      10.079  34.838  11.847  1.00 29.57           N  
ATOM    775  CA  LYS A 105      10.147  36.293  12.036  1.00 28.05           C  
ATOM    776  C   LYS A 105      11.562  36.720  12.391  1.00 27.06           C  
ATOM    777  O   LYS A 105      12.174  36.150  13.289  1.00 27.14           O  
ATOM    778  CB  LYS A 105       9.142  36.750  13.090  1.00 27.30           C  
ATOM    779  CG  LYS A 105       7.712  36.235  12.749  1.00 27.03           C  
ATOM    780  CD  LYS A 105       6.645  37.016  13.447  1.00 26.83           C  
ATOM    781  CE  LYS A 105       5.287  36.300  13.367  1.00 24.94           C  
ATOM    782  NZ  LYS A 105       4.698  36.387  11.996  1.00 23.03           N  
ATOM    783  N   LEU A 106      12.058  37.734  11.691  1.00 25.68           N  
ATOM    784  CA  LEU A 106      13.374  38.275  11.962  1.00 25.87           C  
ATOM    785  C   LEU A 106      13.354  39.143  13.222  1.00 25.22           C  
ATOM    786  O   LEU A 106      12.314  39.719  13.598  1.00 24.89           O  
ATOM    787  CB  LEU A 106      13.857  39.118  10.784  1.00 25.38           C  
ATOM    788  CG  LEU A 106      14.443  38.394   9.564  1.00 27.94           C  
ATOM    789  CD1 LEU A 106      13.727  37.094   9.184  1.00 27.95           C  
ATOM    790  CD2 LEU A 106      14.567  39.332   8.388  1.00 26.61           C  
[...]
</pre>

### Output:
<pre>
ATOM      1  N   LYS A   1      10.079  34.838  11.847  1.00 29.57           N
ATOM      2  CA  LYS A   1      10.147  36.293  12.036  1.00 28.05           C
ATOM      3  C   LYS A   1      11.562  36.720  12.391  1.00 27.06           C
ATOM      4  O   LYS A   1      12.174  36.150  13.289  1.00 27.14           O
ATOM      5  CB  LYS A   1       9.142  36.750  13.090  1.00 27.30           C
ATOM      6  CG  LYS A   1       7.712  36.235  12.749  1.00 27.03           C
ATOM      7  CD  LYS A   1       6.645  37.016  13.447  1.00 26.83           C
ATOM      8  CE  LYS A   1       5.287  36.300  13.367  1.00 24.94           C
ATOM      9  NZ  LYS A   1       4.698  36.387  11.996  1.00 23.03           N
ATOM     10  N   LEU A   2      12.058  37.734  11.691  1.00 25.68           N
ATOM     11  CA  LEU A   2      13.374  38.275  11.962  1.00 25.87           C
ATOM     12  C   LEU A   2      13.354  39.143  13.222  1.00 25.22           C
ATOM     13  O   LEU A   2      12.314  39.719  13.598  1.00 24.89           O
ATOM     14  CB  LEU A   2      13.857  39.118  10.784  1.00 25.38           C
ATOM     15  CG  LEU A   2      14.443  38.394   9.564  1.00 27.94           C
ATOM     16  CD1 LEU A   2      13.727  37.094   9.184  1.00 27.95           C
ATOM     17  CD2 LEU A   2      14.567  39.332   8.388  1.00 26.61           C
</pre>
<br>
<br>
	
