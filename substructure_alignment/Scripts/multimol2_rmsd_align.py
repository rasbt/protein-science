# Sebastian Raschka 2014
#
# Aligns multiple mol2 files to a reference mol2 files and
# writes the aligned targets to the hard drive.
#
# USAGE from command shell command line:
# %> python3 multimol2_rmsd_align.py input_dir/ output_dir/ ref.mol2 smiles_string

import subprocess
import os
import sys

RMSD_TOOL = "/soft/linux64/.../oechem-utilities/rmsd"       # put the correct path to the RMSD bin here


try:
    assert len(sys.argv) == 5
    INPUT_DIR = sys.argv[1]
    TARGET_DIR = sys.argv[2]
    REFERENCE_MOL = sys.argv[3]
    SMILES = sys.argv[4]
    
    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)

    for i in [m for m in os.listdir(INPUT_DIR) if m.endswith('.mol2')]:
        in_mol = INPUT_DIR + '/' + i
        out_mol = TARGET_DIR + '/' + i
        subprocess.call("{} -in {} -ref {} -overlay -out {} -smarts '{}'".format(
	    RMSD_TOOL, in_mol, REFERENCE_MOL, out_mol, SMILES), shell=True)

except:
    print("ERROR\nUSAGE: python3 multimol2_rmsd_align.py input_dir/ output_dir/ ref.mol2 smiles_string")
