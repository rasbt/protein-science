import glob
import os
import string

def print_copyright():
	''' Printing program name, version, date, and my name '''
	print '\n\n%s\n%s PDB TO FASTA CONVERTER %s\n%s\n' \
		%((40 * '#'), (8 * '#'), (8 * '#'), (40 * '#'))
	print 16*'~', 'v. 1.0', 16*'~'
	print 14*'~', '04/21/2013', 14*'~', '\n'
	print 10*'*', 'Sebastian Raschka', 11*'*'
	print 40 * '*'
	print 40 * '*', '\n', '\n'

def get_target_folder():
	'''Prompts user repeatedly for folder. Changes workdir if folder
	exists. Gets all .pdb .PDB files in this folder and returns the
	names as a list'''
	while True:
		target_folder = raw_input('\n\nPath of folder with PDB files: ')
		try:
			os.chdir(target_folder)
		except OSError: 
			print '\nError: %s does not exist, try again!\n' %(target_folder)
			continue
		else:
			pdb_file_list = glob.glob('*.pdb')
			PDB_file_list = glob.glob('*.PDB')
			pdb_file_list = pdb_file_list + PDB_file_list
		if pdb_file_list:
			break 
		else:
			print '\nError: %s does not contain valid '\
				'PDB files, try again!\n' %(target_folder)
	return pdb_file_list


def open_pdb(pdb_filename_str):
	'''Expects name of a valid .pdb file. Opens PDB file and returns
	a list with lines as items'''
	file_obj = open(pdb_filename_str, 'r')
	entries_list = []
	try:
		for line in file_obj:
			line = line.strip()
			entries_list.append(line)
	except OSError:
		print 'Error: could not read %s' %(pdb_filename_str)
		return None
	else:
		return entries_list
	finally:
		file_obj.close()
	
	
def set_up_outfile(file_str):
	file_obj = open(file_str, 'w')
	return file_obj	


def extract_lines(lines_list, file_str):
	'''Expects a list with pdb file lines as items
	and expects the name of the pdb origin file.
	Returns lines that contain atom entries as list
	of format [[chainA lines], [chainB lines], ...] '''
	atomentry_list = []
	chainentry_list = []
	for line in lines_list:
		if line[0:6] == "ATOM  ":
			chainentry_list.append(line)
		if line[0:6] == "TER   ":
			atomentry_list.append(chainentry_list)
			chainentry_list = []
	if chainentry_list:
		atomentry_list.append(chainentry_list)
	if not atomentry_list:
		print 'Warning: %s is not correctly formatted' %(file_str)		
	return atomentry_list

def derive_fastaseq(fasta_str, pdb_str, atomentry_list):
	'''Expects:
	- name of the fasta file for FASTA_results
	- name of the current pdb file for header
	- list of format [[chainA lines], [chainB lines], ...]'''

	prev_seq_num = 0
	chain_fastas = []
	for chain in atomentry_list:
		fasta_sequence = []
	
		for line in chain:
			try:
				aa_3letter = line[17:20].strip()
				aa_1letter = aa_dict[aa_3letter]
				res_seqnumber = line[22:26].strip()
				
				res_seqnumber = int(res_seqnumber)
				if prev_seq_num != res_seqnumber:
					fasta_sequence.append(aa_1letter)
				prev_seq_num = res_seqnumber

			except KeyError:
				pass
				print 'Warning: %s contains unknown residue name' %(pdb_str)	
			except ValueError:
				print 'Warning: Residue sequence numbers of %s' %(pdb_str),\
				 'are not correctly formated' 
		chain_fastas.append(fasta_sequence)

	return chain_fastas

def writeout_fastas(pdb_str, fasta_list, file_obj):
	if len (fasta_list) == 1:
		file_obj.write('>%s \n' %(pdb_str[:-4]))
		aa_pos = 49
		while aa_pos <= len(fasta_list[0])-1:
			fasta_list[0].insert(aa_pos, '\n')
			aa_pos += 50
		file_obj.write(''.join(fasta_list[0]))
		file_obj.write('\n\n')
	else:
		count = 0
		for chain in fasta_list:
			
			file_obj.write('>%s |Chain %s\n' %(pdb_str[:-4],\
				 string.uppercase[count]))
			aa_pos = 49
			while aa_pos <= len(chain)-1:
				chain.insert(aa_pos, '\n')
				aa_pos += 50
			file_obj.write(''.join(chain))
			file_obj.write('\n\n')
			count += 1
			if count > 25:
				count = 0


def main():

	print '''
 _____   _____   ____    _______       ______         _____  _______        
|  __ \ |  __ \ |  _ \  |__   __|     |  ____|/\     / ____||__   __| /\    
| |__) || |  | || |_) |    | |  ___   | |__  /  \   | (___     | |   /  \   
|  ___/ | |  | ||  _ <     | | / _ \  |  __|/ /\ \   \___ \    | |  / /\ \  
| |     | |__| || |_) |    | || (_) | | |  / ____ \  ____) |   | | / ____ \ 
|_|     |_____/ |____/     |_| \___/  |_| /_/    \_\|_____/    |_|/_/    \_\\\

        _____                                _                                    
       / ____|                              | |                                   
      | |      ___   _ __ __   __ ___  _ __ | |_  ___  _ __                       
      | |     / _ \ | '_  \\ \ / // _ \| '__|| __|/ _ \| '__|                      
      | |____| (_) || | | |\ V /|  __/| |   | |_|  __/| |                         
       \_____|\___/ |_| |_| \_/  \___||_|    \__|\___||_|                         
                                                                               
               
	-- Sebastian Raschka --

	v 1.1

	'''	

	outfile_str = 'FASTA_sequences.fasta'
	#pdb_file = '2M18.pdb'
	#print_copyright()
	pdb_file_list = get_target_folder()
	fasta_obj = set_up_outfile(outfile_str)
	count = 1
	max_count = len(pdb_file_list)
	print '\n\nPROCESSING: '
	for pdb_file in pdb_file_list:

		print pdb_file
	
		pdb_content_list = open_pdb(pdb_file)
		
		atomentry_list = extract_lines(pdb_content_list, pdb_file)

		fasta_sequences = derive_fastaseq(outfile_str, pdb_file, atomentry_list)
	
		writeout_fastas(pdb_file, fasta_sequences, fasta_obj)
		count += 1

	fasta_obj.close()
	if os.path.isfile('%s/FASTA_sequences.fasta' %(os.getcwd())):
		print '\n\nResults written to %s/FASTA_sequences.fasta\n\n' %(os.getcwd())

aa_dict = {'ALA':'A', 'ARG':'R', 'ASN':'N', 'ASP':'D', 'CYS':'C', \
		'GLU':'E','GLN':'Q', 'GLY':'G', 'HIS':'H', 'ILE':'I', 'LEU':'L',\
		 'LYS':'K', 'MET':'M','PHE':'F', 'PRO':'P', 'SER':'S', 'THR':'T',\
		 'TRP':'W', 'TYR':'Y', 'VAL':'V','MSE':'M', 'CSE':'C', \
		 'G':'G', 'U':'U', 'C':'C', 'A':'A', 'T':'T'} # DNA

main()
