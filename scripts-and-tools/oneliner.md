Sebastian Raschka  
Last updated: 10/15/2014

## Useful One-liner for working with Protein Files



### Remove ANISOU entries from PDB files

	grep -v ANISOU orig.pdb > no_anisou.pdb

### Remove water molecules

	grep -v -E 'HETATM.*HOH' prot.pdb > prot_noH2O.pdb