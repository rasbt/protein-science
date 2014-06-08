# Script that uses OpenBabel to create
# PDB files from a FASTA file.

# 07/07/2013
# Sebastian Raschka


import os
import sys

def is_ascii(s):
    '''Tests 1-letter strings if they are in ascii format.
    Returns boolean.
    '''
    try:
        return all(ord(c) < 128 for c in s)
    except TypeError:
        return False

def get_options():
    '''Prompt user to specify the input FASTA file
    and test if it exists. Ask whether results should
    be written to one or multiple pdb files.
    Returns: 
       - String of the input file
       - Boolean for multifile
    '''
    print "\n\nPlease enter the directory and name of\n",\
                   "the FASTA input file.\n",\
                   "E.g., /home/sebastian/Desktop/myfasta.fasta\n"
    
    print "\n Your current working directory is %s\n" %(os.getcwd())
    
    # prompt user for input file until correct.
    while True:

        print "\nEnter the file name now or q to quit\n"
        sFileName = raw_input('\n... : ')
        print "\n"
        try:
            if sFileName.lower() in ["q", "quit", "exit"]:
                raise KeyboardInterrupt
            sBaseName = os.path.basename(sFileName)
            sFront, sEnd = sBaseName.split(".")
            if sEnd.lower() not in ["txt", "fasta", "fas"]:
                raise IOError
            oFile = open(sFileName, 'r')
    

            # test if FASTA file is in proper ASCII format
            for line in oFile:
                line = line.strip()
                if line:
                    for letter in line:
                        bAscii = is_ascii(letter)
                        if not bAscii:
                            raise TypeError
        
            oFile.close()
            break
        except KeyboardInterrupt:
            sys.exit()
        except IOError:
            print "\n\nERROR: %s does not exist, please try again.\n"\
                   %(sFileName)
        except ValueError:
            print "\n\nERROR: %s does not seem to be a valid fasta file.\n\
                   Please try again.\n\n" %(sBaseName)
        except TypeError:
            print "\n\nERROR: %s contains non-ASCII characters.\n\
                   Please provide a valid FASTA file.\n\n" %(sBaseName)


    return sFileName

def get_input(sFile):
    '''Read in the Fasta file.
    Expects: Dir+Path of the fasta file
    Returns: list with sublists that represent fasta codes
             [[line1, line2,...], [line1, line2,...], [...], 
    '''
    lFastas = []
    lNewEntry = []
    oFile = open(sFile, 'r')
    for line in oFile:
        line = line.strip()
        if line:
            if line[0] == ">":
                if lNewEntry:
                    lFastas.append(lNewEntry)
                lNewEntry = []
            lNewEntry.append(line)
    if lNewEntry:
        lFastas.append(lNewEntry)
    oFile.close()
    return lFastas

def create_single_fastafiles(lFastas, sFileName):
    '''Creates new fasta files that can be used as
       inputs for openBabel
    Expects: list with fasta entries, Filename of
             original Fasta.
    '''
    
    # create a subfolder
    sDirName = os.path.dirname(sFileName)
    if not sDirName:
        sDirName = os.path.curdir

    i = 0
    while True:
        i += 1
        sFolderName = sDirName + "/Single_Fastas_" + str(i)
        if not os.path.exists(sFolderName):
            os.mkdir(sFolderName)
            break

    # write Fasta Files to that folder
    os.chdir(sFolderName)
    for fasta in lFastas:
        
        sName = fasta[0][1:12] + '.fasta'
        i = 1
        while True:
            i += 1
            if not os.path.exists(sName):
                break
            sName = fasta[0][1:8] + "_" + str(i) + '.fasta'
        oFile = open(sName, "w")
        for line in fasta:
            oFile.write(line + '\n')
        oFile.close()
    return sFolderName


def main():
    try: 
        # get name of input FASTA file
        sFileName = get_options()
    
        # read in fasta file
        lFastas = get_input(sFileName)
    
        # create fasta files for openBabel
        sFolderName = create_single_fastafiles(lFastas, sFileName)

        
        print """ ______       _____ _______        
 |  ____/\\    / ____|__   __|/\\     
 | |__ /  \\  | (___    | |  /  \\    
 |  __/ /\\ \\  \___ \\   | | / /\\ \\   
 | | / ____ \\ ____) |  | |/ ____ \\  
 |_|/_/_   \\_\\_____/   |_/_/    \_\\ 
  / ____|     | (_) | | |           
 | (___  _ __ | |_| |_| |_ ___ _ __ 
  \\___ \\| '_ \\| | | __| __/ _ \\ '__|
  ____) | |_) | | | |_| ||  __/ |   
 |_____/| .__/|_|_|\\__|\\__\\___|_|   
        | |                         
        |_|  

     by Sebastian Raschka

      v. 1.0   07/22/2013

"""
        print "\t\n\n\nFASTA files written to %s \n\n" %(sFolderName)


    except KeyboardInterrupt:
        sys.exit()

main()
