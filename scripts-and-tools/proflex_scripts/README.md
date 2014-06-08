# proflex_scripts  

A collection of scripts to work with ProFlex in- and output files  

## grab_bonded_pflexdataset.py  

This scripts creates a 2-column list file with pairs of atoms that are  
connected either by hydrogen or electrostatic bonds.  
Requires a proflexdatase file as input.  
Bonds can be viewed in PyMOL by reading the out put list via the PyMOL   
BondVis plugin [link]  

### Example:  
<pre> <code>
[bash]~/Desktop >python grab_hb_proflexdataset.py


PROFLEXDATASET FILE

please enter a file name,
or type --help to get a list of the accepted file formats
: crystal_pflex_in_proflexdataset
File name to save the results: results.txt
Atom#1 Atom#2
11857 5911
11856 2673
11847 3646
11858 4372
11857 2672
11852 749
</code><pre>

## flexibility_color_v3.pml

PyMOL script to color a proflex output PDB file by flexibility indeces. Color range
from red (flexible) to gray (isostatic) to blue (rigid).

#### Usage: 
1. open PDB file in PyMOL 
2. click on File -> Run 
3. select script in from the menu
