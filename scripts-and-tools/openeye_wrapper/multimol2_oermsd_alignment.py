# Sebastian Raschka 2014
#
# Aligns multiple mol2 files to a reference mol2 files and
# writes the aligned targets to the hard drive.

import subprocess
import os

INPUT_DIR = '/home/mol2_out'
TARGET_DIR = '/home/mol2_out_aligned'
REFERENCE_MOL = '~/Desktop/xxx_docked.mol2'
RMSD_TOOL = "/soft/openeye/oechem-utilities/openeye/toolkits/rmsd"

if not os.path.exists(TARGET_DIR):
    os.mkdir(TARGET_DIR)

for i in [m for m in os.listdir(INPUT_DIR) if m.endswith('.mol2')]:
    in_mol = INPUT_DIR + '/' + i
    out_mol = TARGET_DIR + '/' + i
    subprocess.call("{} -in {} -ref {} -overlay -out {}".format(
	RMSD_TOOL, in_mol, REFERENCE_MOL, out_mol), shell=True)
