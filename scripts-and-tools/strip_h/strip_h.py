# Sebastian Raschka 2014
# Python 3 strip hydrogen atoms from PDB files
#
# run
# ./stip_h.py -h
# for help
#
import os

class Pdb(object):
    """ Object that allows operations with protein files in PDB format. """
    def __init__(self, file_cont=[], pdb_code=""):
        self.cont = []
        self.fileloc = ""
        if isinstance(file_cont, list):
            self.cont = file_cont[:]
        elif isinstance(file_cont, str):
            try:
                with open(file_cont, 'r') as pdb_file:
                    self.cont = [row.strip() for row in pdb_file.read().split('\n') if row.strip()]
            except FileNotFoundError as err:
                print(err)


    def strip_h(self):
        """ Removes hydrogen atoms from a PDB file content list """
        out = []
        for row in self.cont:
            if len(row) > 5:
                if row.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
                    if len(row) > 11 and (row[12] == 'H' or row[13] == 'H'):
                        continue
            out.append(row)
        return out
        
    def write(self, outfile):
        """ Writes PDB to output file. """
        with open(outfile, 'w') as out:
            for line in self.cont[:-1]:
                out.write(line + '\n')
            out.write(self.cont[-1])
            
    def printout(self):
        """ Prints PDB to output file to stdout. """
        for line in self.cont:
            print(line)


def find_files(substring, path, recursive=False, check_ext=None, ignore_invisible=True, ignore_substring=None): 
    """
    Function that finds files in a directory based on substring matching.
        
    Parameters
    ----------
    
    substring : `str`
      Substring of the file to be matched.
    
    path : `str` 
      Path where to look.
    
    recursive: `bool`
      If true, searches subdirectories recursively.
      
    check_ext: `str`
      If string (e.g., '.txt'), only returns files that
        match the specified file extension.
      
    ignore_invisible : `bool`
      If `True`, ignores invisible files (i.e., files starting with a period).
      
    ignore_substring : `str`
      Ignores files that contain the specified substring.
      
    Returns
    ----------
    results : `list`
      List of the matched files.
        
    """
    def check_file(f, path):
        if not (ignore_substring and ignore_substring in f):
            if substring in f:
                compl_path = os.path.join(path, f)
                if os.path.isfile(compl_path):
                    return compl_path
        return False 
        
    results = []
    
    if recursive:
        for par, nxt, fnames in os.walk(path):
            for f in fnames:
                fn = check_file(f, par)
                if fn:
                    results.append(fn)
    
    else:
        for f in os.listdir(path):
            if ignore_invisible and f.startswith('.'):
                continue
            fn = check_file(f, path)
            if fn:
                results.append(fn)
                
    if check_ext:
        results = [r for r in results if os.path.splitext(r)[-1] == check_ext]
    
    return results
           
if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(
        description='Renumber residues in a pdb file',
        formatter_class=argparse.RawTextHelpFormatter
        )


    parser.add_argument('-i', '--input', help='Input PDB file or directory')
    parser.add_argument('-o', '--output', help='Output PDB file or directory')
    parser.add_argument('-r', '--recursive', action='store_true', help='Applies strip_h recursively if --input is a directory')
    parser.add_argument('-v', '--version', action='version', version='v. 1.0')

    args = parser.parse_args()

    if not args.input:
        print('{0}\nPlease provide an input file or directory.\n{0}'.format(50* '-'))
        parser.print_help()
        quit()
        
    # if input is a directory
    if os.path.isdir(args.input):
        in_files = find_files(substring='', 
                            path=args.input, 
                            recursive=args.recursive, 
                            check_ext='.pdb', 
                            ignore_invisible=True, 
                            ignore_substring=None)
                            
        if not args.output:
            print('{0}\nWould strip the following files:\n{0}'.format(50*'-'))
            for f in in_files:
                print(f)
            print('{0}\nPlease provide an output directory!\n{0}'.format(50*'-'))
            parser.print_help()
            quit()
            
        out_files = [os.path.join(args.output, f.split(args.input)[-1]) for f in in_files]
        
        for i,o in zip(in_files, out_files):
            pdb = Pdb(file_cont=i)
            pdb.cont = pdb.strip_h()
            if not os.path.isdir(os.path.dirname(o)):
                os.makedirs(os.path.dirname(o))
            pdb.write(o)

    # if input is a file:
    else:
        pdb = Pdb(file_cont=args.input)
        pdb.cont = pdb.strip_h()
        
        if not args.output:
            pdb.printout()
            
        else:
            pdb.write(args.output)
