# Python 2.7
# Utilizes PyMOL to convert .mol2 files read from a directory and convert
# them into PDB file format.
#
# 10/22/13 Sebastian Raschka
#
#
#
import os
import random
import commands

def read_mol2():
    '''Prompts user for a directory with .mol2 files and returns a list of mol2 files.'''
    while True:
        print "\nDirectory of mol2 ligand orientations"
        mol2_dir = raw_input(": ")
        if not os.path.isdir(mol2_dir):
            print "Sorry, directory doesn't exist. Please try again."
            continue
        break
    mol2_dir = os.path.abspath(mol2_dir)
    mol2_files = [i.split(".")[0] for i in os.listdir(mol2_dir) if i.split(".")[1] == "mol2"]
    return mol2_dir, mol2_files


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

def convert(mol2_file, pdb_file, pymol_cmd):
    tmp_script = str(random.random())[2:] + ".py"
    with open(tmp_script, "w") as file:
        file.write('pymol.cmd.load("{}")\n'.format(mol2_file))
        file.write('pymol.cmd.save("{}", "allatoms", 1, "pdb")\n'.format(pdb_file))
        file.write("pymol.cmd.quit()")
    commands.getoutput("{} -cr {}".format(pymol_cmd, tmp_script))
    os.remove(tmp_script)
    return

def main():
    print "If you use an other command than 'pymol' to run PyMOL\n"\
            "    please enter it here.\n    Else just hit ENTER."
    pymol_cmd = raw_input(": ")
    if pymol_cmd == "":
        pymol_cmd = "pymol"
    mol2_dir, mol2_files = read_mol2()
    out_dir = get_out_dir()
    for protfile in mol2_files:
        mol2_path = "{}/{}.mol2".format(mol2_dir, protfile)
        pdb_path = "{}/{}.pdb".format(out_dir, protfile)
        convert(mol2_path, pdb_path, pymol_cmd)
        print pdb_path
    return
main()
