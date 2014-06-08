# Python 2.7
# Utilizes Openeye's RMSD tool to align molecules in PDB or MOL2 format.
#
# 10/23/13 Sebastian Raschka
#
#
#
import os
import commands

def read_input():
    '''Prompts user for a directory with .mol2 and .pdb files and returns a list of mol2 files.'''
    while True:
        print "\nDirectory with .mol2 and/or .pdb files"
        input_dir = raw_input(": ")
        if not os.path.isdir(input_dir):
            print "Sorry, directory doesn't exist. Please try again."
            continue
        break
    input_files = [i for i in os.listdir(input_dir) 
                 if i.split(".")[-1] == "mol2" or i.split(".")[-1] == "pdb"]
    return input_dir, input_files

def get_ref_molecule():
    '''Prompts user for a reference molecule to to align the other molecules against.'''
    while True:
        print "\nPath to the reference molecule"
        ref_mol = raw_input(": ")
        if not os.path.isfile(ref_mol):
            print "Sorry, this file doesn't exist. Please try again."
            continue
        if not (ref_mol.split(".")[-1] == "pdb" or ref_mol.split(".")[-1] == "mol2"):
            print "Please provide a file in .mol2 or .pdb format."
            continue
        break
    return ref_mol

def get_out_dir():
    '''Prompts user for an output directory'''
    while True:
        print "\nChoose an output directory"
        out_dir = raw_input(": ")
        if os.path.isfile(out_dir):
            print "Sorry, there is already a file with the same name.\n"
            continue
        if not os.path.isdir(out_dir):
            try:
                os.mkdir(out_dir)
            except OSError:
                print "Sorry, there was a problem creating this directory.\n"
                continue
        break
    return out_dir

def align(rmsd_cmd, ref_molecule, molecule, out_file):
    exe = "{} -automorph true -overlay true -ref {} -in {} -out {}" \
                      .format(rmsd_cmd, ref_molecule, molecule, out_file)
    print commands.getoutput(exe)

def main():
    print "Note:\nUses Openeye RMSD tool with parameters:\n"\
          "-automorph true -overlay true\n"
    print "Enter the command to execute Openeye RMSD, e.g.,\n"\
          "/soft/openeye/oechem-utilities/rmsd\n"
    rmsd_cmd = raw_input(": ")
    input_dir, input_files = read_input()
    ref_mol = get_ref_molecule()
    out_dir = get_out_dir()    
    results = list()
    for mol in input_files:
        in_file = "{}/{}".format(input_dir, mol)
        out_file = "{}/{}".format(out_dir, mol)
        align(rmsd_cmd, ref_mol, in_file, out_file)
    return

main()
