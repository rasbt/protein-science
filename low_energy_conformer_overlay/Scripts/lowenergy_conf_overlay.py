# Sebastian Raschka, 02/2014
# Script to run OpenEye OMEGA2 and ROCS command line tools.
# File directories and paths to the OpenEye executables need to be
# adjusted in the main (if __name__ == '__main__':) function.

import os
import subprocess
import time


def run_omega(omega2_exe, fraglib, in_mol2, out_mol2):
    """ 
    Runs OpenEye OMEGA2 in a shell environment to 
    generate up to 200 low-energy concormers.

    Keyword Arguments:
        omega2_exe (str): path to the OMEGA2 executable
        fraglib (str): path to the OMEGA2 fragment library
        in_mol2 (str): path to the input mol2 structure
        out_mol2 (str): path to the multi-conformer output file

    """
    omega2_cmd = "{0} " \
            "-in {1} " \
            "-out {2} " \
            "-warts true " \
            "-fraglib {3} " \
            "-commentEnergy true " \
            "-prefix test".format(
            omega2_exe, in_mol2, out_mol2, fraglib)
    with open(os.devnull, "w") as fnull:
        result = subprocess.call(omega2_cmd, stdout=fnull, stderr=fnull, shell=True)
    print(in_mol2)


def run_rocs(rocs_exe, query_mol2, db_mol2, rocs_prefix, rocs_out, rocs_cutoff=0.6):
    """
    Runs OpenEye ROCS to overlay a query molecule to a database mol2 file.
    The query file is typically a multi-mol2 file that consists of 1 query molecule
    in multiple low-energy conformations.
    The database file typically consists of many molecules in multiple low-energy
    conformations.

    Keyword Arguments:
        rocs_exe (str): path to the ROCS executable
        query_mol2 (str): path to the query molecule (multi-)mol2 file.
        db_mol2 (str): path to the database (multi-)mol2 file.
        rocs_prefix (str): prefix for the report files.
        rocs_out (str): path to the output directory (will be created if it doesn't exist yet).
        rocs_cutoff (float): Maximum TanimotoCombo score that will be considered.

    """
    if not os.path.exists(ROCS_OUT):
        os.mkdir(ROCS_OUT)

    subprocess.call("{0} "\
        "-query {1} "\
        "-dbase {2} "\
        "-randomstarts 20 -stats best -besthits 0 -maxhits 0 -maxconfs 1 "\
        "-rankby TanimotoCombo "\
        "-mcquery "\
        "-prefix {3}/{4} "\
        "-cutoff {5} "\
        "-reportfile {3}/{4}.rpt -oformat mol2 -report one"\
       .format(rocs_exe, query_mol2, db_mol2, rocs_out, rocs_prefix, rocs_cutoff), shell=True)


if __name__ == '__main__':
    start = time.time()    

    OMEGA2_EXE = "/soft/linux64/openeye/bin/omega2"
    FRAGLIB = "/soft/linux64/openeye/data/omega2/fraglib.oeb.gz"
    IN_MOL2_1 = '../ZINC00062008.mol2'
    OUT_MOL2_1 = '../ZINC00062008_confs.mol2'
    
    run_omega(OMEGA2_EXE, FRAGLIB, IN_MOL2_1, OUT_MOL2_1)

    IN_MOL2_2 = '../ZINC00082321.mol2'
    OUT_MOL2_2 = '../ZINC00082321_confs.mol2'

    run_omega(OMEGA2_EXE, FRAGLIB, IN_MOL2_2, OUT_MOL2_2)

    ROCS_EXE = '/soft/linux64/openeye/rocs/2.4.2/bin/rocs'
    QUERY_MOL2 = OUT_MOL2_1
    DB_MOL2 = OUT_MOL2_2
    ROCS_CUTOFF = 0.6
    ROCS_PREFIX = 'b12'
    ROCS_OUT = '../rocs'
   
    run_rocs(ROCS_EXE, QUERY_MOL2, DB_MOL2, ROCS_PREFIX, ROCS_OUT, ROCS_CUTOFF)

    end = time.time()
    print("\nTime elapsed: {} sec".format(round(end-start,3)))
