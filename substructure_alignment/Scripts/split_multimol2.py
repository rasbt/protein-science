# Sebastian Raschka 01/10/2014

# Splits a multi-mol2 file into individual mol2 files.

import sys
import os

def split_multimol2(multimol2):
    """Splits a multi-mol2 file (a mol2 file consisting of multiple mol2 entries)
        into individual mol2-file contents.

    Arguments:
        multimol2 (string): path to the multi-mol2 file

    Returns:
        A list consisting of a sublist for every extracted mol2-file. Sublists contain
        the molecule ID and the mol2 file contents.
        e.g., [['ID1234', '@<TRIPOS>MOLECULE...'],['ID1235', '@<TRIPOS>MOLECULE...'], ...]
    
    """
    with open(multimol2, 'r') as mol2file:
        line = ""
        mol2cont = ""
        single_mol2s = []
        line = mol2file.readline()

        while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
            if line.startswith("@<TRIPOS>MOLECULE"):
                mol2cont = ""
                mol2cont += line
                line = mol2file.readline()
                molecule_id = line.strip()

                while not line.startswith("@<TRIPOS>MOLECULE"):
                    mol2cont += line
                    line = mol2file.readline()
                    if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                        mol2cont += line
                        break
                
                single_mol2s.append([molecule_id, mol2cont])
    return single_mol2s


try:
    assert len(sys.argv) == 3
    multimol2 = sys.argv[1]
    out_dir = sys.argv[2]
    
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    single_mol2s = split_multimol2(multimol2)
    for mol2 in single_mol2s:
        out_mol2 = os.path.join(out_dir, mol2[0]) + '.mol2'
        with open(out_mol2, 'w') as out_file:
            for line in mol2[1]:
                out_file.write(line)

except:
    print("ERROR\nUSAGE: python3 multimol2.mol2 output_directory")
 
