# Sebastian Raschka 10/15/13
# fix_atomname_pos.py
#

import os

def fix_line(line):
    line_result = line
    line_chr = list()
    for c in line:
        line_chr.append(c)
    if len(line_chr) > 11:
        if line_chr[12].isalpha():
            line_chr.pop(16)
            line_chr.insert(11," ")
            line_result = "".join(line_chr)
    return line_result    

def user_in():
    while True:
        directory = raw_input("Input directory with pdb files: ")
        if not os.path.isdir(directory):
            print "Directory doesn't exist. Please try again."
            continue
        cur_dir = os.getcwd()   # because os.path.abspath() omits subfolder
        files = ["{}/{}/{}".format(cur_dir, directory, i)  for i in os.listdir(directory)
                    if i.split(".")[-1] == "pdb"]
        if not files:
            print "Directory doesn't contain any .pdb files. Please try again"
            continue
        break
    return files

def user_out():
    while True:
        directory = raw_input("Output directory for fixed pdb files: ")
        if os.path.isfile(directory):
            print "Cannot create this folder. There is already a file with similar name."
            print "Please try again."
            continue
        if not os.path.isdir(directory):
            os.mkdir(directory)
        break
    return directory

def read_file(f):
    new_pdb = list()
    with open(f, "r") as pdb:
        for line in pdb:
            line = line.strip()
            new_line = fix_line(line)
            new_pdb.append(new_line)

    return new_pdb        

def write_file(directory, f, new_pdb):
    path = "{}/{}".format(directory, os.path.basename(f))
    with open(path, "w") as new_file:
        for line in new_pdb:
            new_file.write(line + "\n")
    return path


def main():
    files = user_in()
    directory = user_out()
    for f in files:
        new_pdb = read_file(f)
        print write_file(directory, f, new_pdb)

main()    
