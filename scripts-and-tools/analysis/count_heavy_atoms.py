# Sebastian Raschka 03/2014
# Counting heavy atoms in PDB files

import os
import sys

def get_files(pdb_dir):
    """Returns file names of all PDB files in a given directory."""
    for i in os.listdir(pdb_dir):
        if i.endswith('.pdb'):
            yield os.path.join(sys.argv[1], i)

def count_atoms_pdb(pdb_path):
    """Counts heavy and non-heavy atoms in a pdb file."""
    heavy_cnt = 0
    notheavy_cnt = 0
    with open(pdb_path, 'r') as pdb_file:
        for line in pdb_file:
            line = line.strip()
            if line.startswith('HETATM') or line.startswith('ATOM'):
                if line[13:14] == 'H':
                    notheavy_cnt += 1
                else:
                    heavy_cnt += 1
    return (heavy_cnt, notheavy_cnt)
                           
if __name__ == '__main__':
    print('pdb_name,heavy,not_heavy,total')
    for pdb in get_files(sys.argv[1]):
        counts = count_atoms_pdb(pdb)
        print('{},{},{},{}'.format(pdb, counts[0], counts[1], counts[0] + counts[1]))
