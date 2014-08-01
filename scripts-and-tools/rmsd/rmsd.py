# Sebastian Raschka 2014
#
# Root-mean-square deviation (RMSD) for proteins and/or ligands
# in PDB files.
#

class Pdb(object):
    """ Object that allows operations with protein files in PDB format. """

    def __init__(self, file_cont = [], pdb_code = ""):
        self.cont = []
        self.atom = []
        self.hetatm = []
        self.fileloc = ""
        if isinstance(file_cont, list):
            self.cont = file_cont[:]
        elif isinstance(file_cont, str):
            try:
                with open(file_cont, 'r') as pdb_file:
                    self.cont = [row.strip() for row in pdb_file.read().split('\n') if row.strip()]
            except FileNotFoundError as err:
                print(err)

        if self.cont:
             self.atom = [row for row in self.cont if row.startswith('ATOM')]
             self.hetatm = [row for row in self.cont if row.startswith('HETATM')]
             self.conect = [row for row in self.cont if row.startswith('CONECT')]
 

    def rmsd(self, sec_molecule, ligand=False, atoms="no_h"):
        """
        Calculates the Root Mean Square Deviation (RMSD) between two
        protein or ligand molecules in PDB format.
        Requires that both molecules have the same number of atoms in the
        same numerical order.

        Keyword arguments:
            sec_molecule (PdbObj): the second molecule as PdbObj object.
            ligand (bool): If true, calculates the RMSD between two
                ligand molecules (based on HETATM entries), else RMSD
                between two protein molecules (ATOM entries) is calculated.
            hydrogen (bool): If True, hydrogen atoms will be included in the
                    RMSD calculation.
            atoms (string) [all/c/no_h/ca]: "all" includes all atoms in the RMSD calculation,
                "c" only considers carbon atoms, "no_h" considers all but hydrogen atoms,
                and "ca" compares only C-alpha protein atoms.

        Returns:
            Calculated RMSD value as float or None if RMSD not be
            calculated.

        """
        rmsd = None

        if not ligand:
            coords1, coords2 = self.atom, sec_molecule.atom
        else:
            coords1, coords2 = self.hetatm, sec_molecule.hetatm
        if atoms == "c":
            coords1 = [row for row in coords1 if row[77:].startswith('C')]
            coords2 = [row for row in coords2 if row[77:].startswith('C')]
        elif atoms == "no_h":
            coords1 = [row for row in coords1 if not row[77:].startswith('H')]
            coords2 = [row for row in coords2 if not row[77:].startswith('H')]
        elif atoms == "ca":
            coords1 = self.calpha()
            coords2 = sec_molecule.calpha()

        if all((coords1, coords2, len(coords1) == len(coords2))):
            total = 0
            for (i, j) in zip(coords1, coords2):
                total += ( float(i[30:38]) - float(j[30:38]) )**2 +\
                         ( float(i[38:46]) - float(j[38:46]) )**2 +\
                         ( float(i[46:54]) - float(j[46:54]) )**2      
            rmsd = round(( total / len(coords1) )**0.5, 4)
        return rmsd

if __name__ == '__main__':
    
    import argparse


    parser = argparse.ArgumentParser(
        description='The RMSD measures the average distance between atoms \n'\
            'of 2 protein or ligand structures.\n'\
            'By default, all atoms but hydrogen atoms of the protein are included in the RMSD calculation.\n'\
            'NOTE: Both structures must contain the same number of atoms in similar order.',
        epilog='Example:\n'\
                'rmsd.py ~/Desktop/pdb1.pdb ~/Desktop/pdb2.pdb\n'\
                '0.7377',
        formatter_class=argparse.RawTextHelpFormatter
        )


    parser.add_argument('PDBfile1')
    parser.add_argument('PDBfile2')


    parser.add_argument('-l', '--ligand', action='store_true', help='Calculates RMSD between ligand (HETATM) atoms.')
    parser.add_argument('-c', '--carbon', action='store_true', help='Calculates the RMSD between carbon atoms only.')
    parser.add_argument('-ca', '--calpha', action='store_true', help='Calculates the RMSD between alpha-carbon atoms only.')
    parser.add_argument('-v', '--version', action='version', version='rmsd v. 1.0')


    args = parser.parse_args()

    pdb1 = Pdb(args.PDBfile1)
    pdb2 = Pdb(args.PDBfile2)

    if args.carbon and args.calpha:
        print('\nERROR: Please provide EITHER -c OR -ca, not both.\n')
        parser.print_help()
        quit()

    if args.ligand and args.carbon:
        print(pdb1.rmsd(sec_molecule=pdb2, ligand=True, atoms="c"))
    elif args.ligand and args.calpha:
        print(pdb1.calpha())
        print(pdb1.rmsd(sec_molecule=pdb2, ligand=True, atoms="ca"))
    elif args.ligand:
        print(pdb1.rmsd(sec_molecule=pdb2, ligand=True, atoms="no_h"))
    elif args.calpha:
        print(pdb1.rmsd(sec_molecule=pdb2, ligand=False, atoms="ca"))
    elif args.carbon:
        print(pdb1.rmsd(sec_molecule=pdb2, ligand=False, atoms="c"))
    else:
        print(pdb1.rmsd(sec_molecule=pdb2, ligand=False, atoms="no_h"))