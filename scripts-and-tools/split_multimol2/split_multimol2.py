# Sebastian Raschka 2014
# Script that splits a multi-mol2 file into individual mol2 files.

import sys
import os


def split_multimol2(multimol2):
    """
    Splits a multi-mol2 file.

    Parameters
    ----------
    multimol2 : str
      Path to the multi-mol2 file.

    Returns
    ----------
    A generator object for lists for every extracted mol2-file. Lists contain
      the molecule ID and the mol2 file contents.
      e.g., ['ID1234', '@<TRIPOS>MOLECULE...'

    """
    with open(multimol2, 'r') as mol2file:
        line = mol2file.readline()

        while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
            if line.startswith("@<TRIPOS>MOLECULE"):
                mol2cont = []
                mol2cont.append(line)
                line = mol2file.readline()
                molecule_id = line.strip()

                while not line.startswith("@<TRIPOS>MOLECULE"):
                    mol2cont.append(line)
                    line = mol2file.readline()
                    if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                        mol2cont.append(line)
                        break
                mol2cont[-1] = mol2cont[-1].rstrip() # removes blank line at file end
                yield [molecule_id, "".join(mol2cont)]


def write_multimol2(multimol2, out_dir):
    """
    Splits a multi-mol2 file into smaller multi-mol2 files.

    Parameters
    -----------
    multimol2 : str
      Path to the multi-mol2 file.

    out_dir : str:
      Output directory. New files will be named
      <molecule_name_1>.mol2, ... <molecule_name_n>.mol2

    Returns
    -----------
    chunks : int
      Number of files written.

    """
    if not os.path.exists(args.OUT_DIR):
        os.mkdir(args.OUT_DIR)

    if not args.chunksize:
        single_mol2s = split_multimol2(args.MOL2_FILE)
        for mol2 in single_mol2s:
            out_mol2 = os.path.join(args.OUT_DIR, mol2[0]) + '.mol2'
            with open(out_mol2, 'w') as out_file:
                for line in mol2[1]:
                    out_file.write(line)
                out_file.write('\n')


def write_multimol2_chunks(multimol2, chunk_size, out_dir):
    """
    Splits a multi-mol2 file into smaller multi-mol2 files.

    Parameters
    -----------
    multimol2 : str
      Path to the multi-mol2 file.

    chunksize : int
      Number of mol2 files per chunk.

    out_dir : str:
      Output directory. New files will be named
      <multimol2>_1.mol2, ... <multimol2>_n.mol2

    Returns
    -----------
    chunks : int
      Number of files written.

    """
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    out_path_stem = os.path.dirname(multimol2)
    out_file_stem = os.path.basename(multimol2).split('.mol2')[0]

    cnt = 0
    chunks = 1
    out_file = open(os.path.join(out_dir, out_file_stem)+'_%d.mol2' % chunks, 'w')
    for mol2 in split_multimol2(multimol2):
        cnt += 1
        if cnt >= chunk_size:
            cnt = 0
            chunks += 1
            out_file.close()
            out_file = open(os.path.join(out_dir, out_file_stem)+'_%d.mol2' % chunks, 'w')
        out_file.write(mol2[1] + '\n')
    out_file.close()
    return chunks


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description='Splits a multi-mol2 file into individual mol2 files',
        formatter_class=argparse.RawTextHelpFormatter
        )

    parser.add_argument('MOL2_FILE')
    parser.add_argument('OUT_DIR')
    parser.add_argument('-c', '--chunksize', help='Number of MOL2 structures per file (1 by default)', type=int)
    parser.add_argument('-v', '--version', action='version', version='split_multimol2 v. 1.1')

    args = parser.parse_args()


    if args.chunksize:
        write_multimol2_chunks(multimol2=args.MOL2_FILE, chunk_size=args.chunksize, out_dir=args.OUT_DIR)

    else:
        write_multimol2(multimol2=args.MOL2_FILE, out_dir=args.OUT_DIR)


