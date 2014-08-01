# Sebastian Raschka 2014
# Script that converts amino acid residues from a PDB file into a FASTA string


#############################
# Amino acid abbreviations
#############################
#
# Unusual/modified amino acids
#
# ASH (protonated ASP) = D
# CYX (disulfide-bonded CYS) = C
# GLH (protonated GLU) = E
# HID/HIE/HIP (different protonation states of HIS) = H
# HYP (hydroxyproline) = P
# MSE (selenomethionine) = M
# CSE (selenocysteine) = U
# LNT (N-((2S)-2-amino-1,1-dihydroxy-4-methylpentyl)-L-threonine)

# Ambiguous amino acids
#
# ASX (asparagine or aspartic acid) = B
# GLX (glutamine or glutamic acid = Z



AMINO_ACIDS_3TO1 = {'CYS': 'C', 'ASP': 'D', 'GLN': 'Q', 'ILE': 'I',
                     'ALA': 'A', 'TYR': 'Y', 'TRP': 'W', 'HIS': 'H',
                     'LEU': 'L', 'ARG': 'R', 'VAL': 'V', 'GLU': 'E',
                     'PHE': 'F', 'GLY': 'G', 'MET': 'M', 'ASN': 'N',
                     'PRO': 'P', 'SER': 'S', 'LYS': 'K', 'THR': 'T',
                     # extended set of amino acids:
                     'MSE': 'M', 'CSE': 'U', 'LNT': 'X', 'GLH': 'E',
                     'HID': 'H', 'HIE': 'H', 'HIP': 'H', 'HYP': 'P',
                     # ambigous amino acids:
                     'ASX': 'B', 'GLX': 'Z'
                    }

AMINO_ACIDS_1TO3 = {'A': 'ALA', 'C': 'CYS', 'D': 'ASP', 'E': 'GLU',
                     'F': 'PHE', 'G': 'GLY', 'H': 'HIS', 'I': 'ILE',
                     'K': 'LYS', 'L': 'LEU', 'M': 'MET', 'N': 'ASN',
                     'P': 'PRO', 'Q': 'GLN', 'R': 'ARG', 'S': 'SER',
                     'T': 'THR', 'V': 'VAL', 'W': 'TRP', 'Y': 'TYR',
                     # extended set of amino acids:
                     'U': 'CSE', 'X': 'LNT',
                     # ambigous amino acids:
                     'B': 'ASX', 'Z': 'GLX'
                    }

class Pdb(object):
    """ Object that allows operations with protein files in PDB format. """

    def __init__(self, file_cont = [], pdb_code = ""):
        self.cont = []
        self.chains = []
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
             self.chains = self._get_chains()

    def _get_chains(self):
        """
        Splits a PDB file into individual chains.
        Returns a dictionary with the respective chains, where
        the Chain IDs are the keys, and the lines of the chain
        are the dictionary values as lists:
        {'A':[chain A lines], 'B':[...], ...}

        """
        chain_dict = dict()
        for line in self.cont:
            if line.startswith(('ATOM', 'HETATM', 'TER')):
                if line[21:22] not in chain_dict:
                    chain_dict[line[21:22]] = []
                chain_dict[line[21:22]].append(line)
        return chain_dict


    def to_fasta(self, hetatm=False):
        """
        Converts the PDB protein atoms into a fasta string and
        returns the results as a dictionary, where the keys are
        chain IDs and the items a list of 1-letter amino acid
        codes.
        E.g., {'H': ['K'], 'L': ['D', 'I', 'V', 'M']}

        Keyword arguments:
            hetatm (bool): If True, also HETATM lines are considered.

        Returns a dictionary with the protein chain letters A-Z as keys
            and the FASTA sequence as values (as list of characters).
            E.g.,

            {'A': ['P', 'Q', 'I', ...], 'B': ['P', 'Q', 'I', ...], ...}

        """
        prev_seq_num = 0
        fasta_dict = dict()
        if hetatm:
            hetatm = "HETATM"
        else:
            hetatm = "ATOM"
        for chain in self.chains.items():
            fasta_sequence = []
            for line in chain[1]:
                if line.startswith(("ATOM", hetatm)):
                    try:
                        aa_3letter = line[17:20].strip()
                        aa_1letter = AMINO_ACIDS_3TO1[aa_3letter]
                        res_seqnumber = line[22:26].strip()

                        res_seqnumber = int(res_seqnumber)
                        if prev_seq_num != res_seqnumber:
                            fasta_sequence.append(aa_1letter)
                        prev_seq_num = res_seqnumber

                    except KeyError:
                        pass
                        if line.startswith("ATOM"):
                            print('Warning: Residue {} unknown.'.format(line))
            fasta_dict[chain[0]] = fasta_sequence
        return fasta_dict
   
        
if __name__ == '__main__':
    
    import argparse


    parser = argparse.ArgumentParser(
        description='Converts amino acid residues from PDB file into a FASTA string',

        formatter_class=argparse.RawTextHelpFormatter
        )


    parser.add_argument('PDBfile')

    parser.add_argument('-l', '--ligand', action='store_true', help='includes HETATM residues.')
    parser.add_argument('-o', '--out', metavar='out.fasta', type=str, 
            help='writes FASTA strings to an output file instead of printing it to the screen')
    parser.add_argument('-v', '--version', action='version', version='pdb_to_fasta v. 1.0')



    args = parser.parse_args()
    
    in_pdb = Pdb(args.PDBfile)

    fastas = sorted(in_pdb.to_fasta(hetatm=args.ligand).items())
    
    if args.out:
        with open(args.out, 'w') as out:
            for chain in fastas:
                out.write('>Chain {}:\n'.format(chain[0]))
                for amino_code in chain[1]:
                    out.write(amino_code)
                out.write('\n\n')
                
    else:
        for chain in fastas:
            print('>Chain {}:\n'.format(chain[0]))
            amino_list = []
            for amino_code in chain[1]:
                amino_list.append(amino_code)
            print("".join(amino_list))
            print('\n\n')       