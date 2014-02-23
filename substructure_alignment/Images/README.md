#Substructure Alignment Using OpenEye OEChem RMSD



### Task:

We want to align a set of molecules to a reference substructure (in contrast to "regular" whole molecule-to-molecule alignments, where the focus lies on minimizing the atom distances over the whole molecule structures).


**Requirements:**   
- OpenEye OEChem RMSD alignment tool  
- protein structure visualization tool (e.g., PyMOL)  
- Python 3.x
- reference molecule in `.mol2` or `.pdb` format
- target molecule structures as multi- or single-mol2 files.  


### 1) Extract substructure in PyMOL


Open the `.mol2` or `.pdb` file of the reference molecule in PyMOL and extract the substructure which you want to align to the query molecules (save it as PDB file).
For this example, I randomly picked a steroid-ring containing structure from the ZINC database, which we want to use here to specifically focus on the alignment of the steroid-ring center itself.

[http://zinc.docking.org/substance/80135621](http://zinc.docking.org/substance/80135621)

1. Top-Panel: Mouse -> Selection Mode -> Atoms
2. click on atoms of interest to mark them as selected
3. On the new selection : Action -> copy to object
4. Save substructure as PDB file: File -> Save Molecule...

#### Reference molecule (ZINC80135621)
![](./Images/reference_molecule.png =350x215)

![](./Images/pymol_copy_substructure.png =450x)


#### Reference substructure

![](./Images/reference_substructure.png =350x)


## 2) Convert substructure into SMILES 

I recommend to use the free online SMILES translator at [http://cactus.nci.nih.gov/translate/](http://cactus.nci.nih.gov/translate/) to upload your converted substructure as PDB file in order to obtain the corresponding SMILES string.  

Alternatively, you can also draw the substructure via the "Search Structure" molecule editor on the ZINC website ([http://zinc.docking.org/search/structure](http://zinc.docking.org/search/structure)) to obtain the SMILE string of the substructure. In this case you would not need to use PyMOL to extract the substructure from the main molecule.  
For such a simple substructure like this steroid-ring construct, it would also probably be the more convenient approach.


## 3) Use OpenEye's RMSD tool

Run OpenEye's OEChem RMSD tool to align target molecules to the reference molecule based on the extracted substructure. The aligned pairs will be written to a new file. The command-line syntax for a typical usage of the OEChem RMSD toll could be: 

	/soft/linux64/openeye/.../oechem-utilities/rmsd\
	-in /home/.../ query.mol2\ 
	-ref ~/Desktop/reference_molecule.mol2\
	-overlay\
	-out /home/.../output.mol2\ 	
	-automorph false\
	-smarts C1CCC2C(C1)CCC3C4CCCC4CCC2

## 4) Some helpful scripts to automate the workflow

#### 4 a) Python script to split a multi-mol2 file

If your target molecules are in a multi-mol2-file, you can use the Python script [split_multimol2.py](./Scripts/split_multimol2.py) to split it into individual mol2 files:

	USAGE: python3 multimol2.mol2 output_directory

#### 4 b) Python subprocess.call() wrapper

And to automate the RMSD substructure alignment over the individual mol2 files, you can use the script [multimol2_rmsd_align.py](./Scripts/multimol2_rmsd_align.py) where you just have to modify the path to your OpenEye RMSD executable.

	USAGE: python3 mmol2_rmsd_align.py input_dir/ output_dir/ ref.mol2 smiles_string


#### 4 c) Concatenate the results

Finally, you can concatenate the resulting alignments back into one single multi-mol2 file via

	> cat mol2_dir/*.mol2 > my_multimol2 file
