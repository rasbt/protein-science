# Python 2.7
#
# This scripts creates a 2-column list file with pairs of atoms that are
# connected either by hydrogen or electrostatic bonds.
#
# Requires a proflexdataset file as input.
# Bonds can be viewed in PyMOL by reading the out put list via the PyMOL 
# BondVis plugin [link]
#
# 11/01/13 Sebastian Raschka

import os.path

def get_filename(file_type):
    '''repeatedly prompts user for a file of specific type.
       arguments:
           file_type: list with accepted file types as strings.
       returns:
           (string): absolute path to the specified input file.
    '''
    while True:
        print "\n\nplease enter a file name, \nor type --help to get"\
                " a list of the accepted file formats"
        file_name = raw_input(": ")
        if file_name == "--help":
            print "\naccepted file format(s): ",
            for f in file_type:
                print f,
            continue        
        if not os.path.isfile(file_name):
            print "\n\nsorry, this file doesn't exist. please try again.\n"
            continue
        if file_type:
            if not (file_name.split(".")[-1] in file_type):
                print "\nplease provide a file in correct format."
                continue
        break
    return os.path.abspath(file_name)

def get_ligand_atoms(proflex_dataset):
    '''Collects atom numbers of the ligand(s) from the Proflex dataset
     and returns them as a list of integers'''
    atom_list = list()
    with open(proflex_dataset, "rb") as pdbfile:
        for line in pdbfile:
            line = line.strip()
            if line[0:6] == "HETATM" and line[17:20] != "XXX":
                try:
                    atom_num = int(line[6:11])
                    atom_list.append(atom_num)
                except ValueError:
                    continue
    return atom_list

def get_bonded_atoms(proflex_dataset, atom_list):
    '''
    Collects atom numbers of bonded ligand and protein atoms
       from the proflex_dataset output file.
    Arguments:
        proflex_dataset (string): name of the proflex_dataset file        
        atom_list (list): list of atom numbers of the ligand as integers
    Returns:
        list with sublists of the bonded atoms
'''
    bond_pairs = list()     
    with open(proflex_dataset, "rb") as pdata:
        for line in pdata:
            line = line.strip()
            if line[0:9] == "REMARK:HB":
                columns = line.split()
                if int(columns[4]) in atom_list or int(columns[5]) in atom_list:
                    bond_pairs.append([int(columns[4]), int(columns[5])])
    return bond_pairs

def print_bonded_list(bond_pairs):
    '''Prints atom numbers of bonded pairs to the screen in 2 columns '''
    print "\nAtom#1 Atom#2"
    for pair in bond_pairs:
        print "{} {}".format(pair[0], pair[1])

def write_bonded_list(bond_pairs, out_file):
    '''Writes a result file with 2 columns that contain the numbers of
       bonded atoms.'''
    with open(out_file, "wb") as out:
        # 1st column is hydrogen atom number, 2nd is acceptor atom number
        for pair in bond_pairs:
            new_line = "{} {}\n".format(pair[0], pair[1])
            out.write(new_line)

def main():

    print "\n\nPROFLEXDATASET FILE"
    pflex_dataset = get_filename([])
    out_file = raw_input("File name to save the results: ")
    lig_atoms = get_ligand_atoms(pflex_dataset)
    bonded_atoms = get_bonded_atoms(pflex_dataset, lig_atoms)
    print_bonded_list(bonded_atoms)
    write_bonded_list(bonded_atoms, out_file)

main()



# =================
# EXAMPLE
# =================

'''
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

'''
