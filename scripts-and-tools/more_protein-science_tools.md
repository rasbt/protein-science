Sebastian Raschka, last updated: 21/07/2014


# Free and useful protein-science tools


<br>
<br>

<a class="mk-toclify" id="table-of-contents"></a>

#Table of Contents

- [Protein-ligand docking and scoring](#protein-ligand-docking-and-scoring)
    - [AutoDock Vina](#autodock-vina)
    - [DrugScoreX](#drugscorex)
    - [LigScore](#ligscore)
- [Protein file and structure processing](#protein-file-and-structure-processing)
    - [OpenBabel](#openbabel)
    - [Reduce](#reduce)
- [Multi-purpose tools and libraries](#multi-purpose-tools-and-libraries)
    - [Biopython](#biopython)
    - [scikit-bio](#scikit-bio)
    - [ProteoWizard](#proteowizard)







<br>
<br>

<hr>
I would be happy to hear your comments and suggestions. 
Please feel free to drop me a note via
[twitter](https://twitter.com/rasbt), [email](mailto:bluewoodtree@gmail.com), or [google+](https://plus.google.com/+SebastianRaschka).
<hr>

<br>
<br>


<a class="mk-toclify" id="protein-ligand-docking-and-scoring"></a>
## Protein-ligand docking and scoring
[[back to top](#table-of-contents)]

<br>
<br>

<a class="mk-toclify" id="autodock-vina"></a>
### AutoDock Vina
[[back to top](#table-of-contents)]

The successor of AutoDock4.2 for docking and re-scoring protein-ligand complexes with a scoring function that estimates the binding affinities, as well as individual terms, such as hydrophobic contribution and hydrogen bonding.

Website: [http://vina.scripps.edu](http://vina.scripps.edu)

*O. Trott, A. J. Olson, AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization and multithreading, Journal of Computational Chemistry 31 (2010) 455-461*

**Usage for re-scoring:**

	vina --config config.txt --score_only
	
Where a config.txt file has to be prepared for every protein-ligand complex, e.g.,

	
	receptor = protein.pdbqt
	ligand = ligand.pdbqt
	center_x = -2.491 # Center of Grid points X
	center_y = 30.038 # Center of Grid points Y
	center_z = -10.765 # Center of Grid points Z
	size_x = 25 # Number of Grid points in X direction
	size_y = 25 # Number of Grid points in Y Direction
	size_z = 25 # Number of Grid points in Z Direction
	
The required `pdbqt` files can be generated via e.g., [OpenBabel](#openbabel) or AutoDock's [MGLTools](http://mgltools.scripps.edu).  
For more details, please see the documentation for 

- [prepare_ligand4.py](http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-ligand-file-for-autodock4)
- [prepare_receptor4.py](http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-receptor-file-for-autodock4)


**Version:**

	vina --version
	AutoDock Vina 1.1.2 (May 11, 2011)


<br>
<br>

<a class="mk-toclify" id="drugscorex"></a>
### DrugScoreX
[[back to top](#table-of-contents)]

DrugScoreX is a new, independent DrugScore implementation with higher accuracy for scoring protein-ligand complexes. It's scoring function is based on statistical potentials.

Website: [http://pc1664.pharmazie.uni-marburg.de/drugscore/](http://pc1664.pharmazie.uni-marburg.de/drugscore/)

*DSX: A Knowledge-Based Scoring Function for the Assessment of Protein–Ligand Complexes
Gerd Neudert and Gerhard Klebe
Journal of Chemical Information and Modeling 2011 51 (10), 2731-2745*



**Usage:**

	dsx_mac_64.mac -h
	
	...

    pro_file    :  A pdb or mol2 file of your protein.
                  In pdb format metals in this file will be treated as part
                  of the protein. => Be sure to delete metals in the pdb file
                  if you want to supply some metals seperately (-M met_file)!
                  All other HETATMs will be ignored!
                  In mol2 format everything will be taken as part of the
                  protein. => Be sure to delete molecules you want to supply
                  seperately (-C, -W, -M) from the protein-mol2-file!
    lig_file    :  A mol2- or autodock dlg-file containing all molecules that
                  should be scored.
                  
    ... 
    
**Version:**
	
	dsx_mac_64.mac -h

 	+---------------------------------------------------------------------------+
 	| 'DSX'           Knowledge-based scoring function for the assessment       |
 	|                 of receptor-ligand interactions                           |
 	|  author     :   Gerd Neudert                                              |
 	|  supervisor :   Prof. Dr. G. Klebe                       ___    _ _       |
 	|  mailto     :   neudert@staff.uni-marburg.de             ))_    )\`)      |
 	|  version    :   0.88   (26.04.2011)                     ((_( o ((\( o     |
 	+---------------------------------------------------------------------------+

<br>
<br>

<a class="mk-toclify" id="ligscore"></a>
### LigScore
[[back to top](#table-of-contents)]

Like DrugScore, a scoring function for protein-ligand complexes based on statistical potentials. It is available as standalone (IMP toolkit) and as webserver.  

The two flavors are RankScore, which is recommended for scoring different ligands in a protein-binding interface (e.g., for virtual screening), and PoseScore, for finding the optimal binding pose of a set of ligand decoys (i.e., the same ligand in different orientations/conformations).

Website: [http://salilab.org/imp/](http://salilab.org/imp/) (for IMP package)

Webserver: [http://modbase.compbio.ucsf.edu/ligscore/](http://modbase.compbio.ucsf.edu/ligscore/)

*Fan H, Schneidman-Duhovny D, Irwin J, Dong GQ, Shoichet B, Sali A. Statistical Potential for Modeling and Ranking of Protein-Ligand Interactions. J Chem Inf Model. 2011, 51:3078-92.*

**Usage**:

Requires installation of the IMP toolkit
	
	ligand_score -h
	Usage: ligand_score file.mol2 file.pdb [libfile]
	
Where `protein_ligand_pose_score.lib` is used for scoring different ligand poses (PoseScore) for the same protein-ligand complex, and `protein_ligand_rank_score.lib` (RankScore) is used to score different ligands for a given binding interface.

(On a Mac, the library files are typically located at: `/usr/local/share/IMP/atom/protein_ligand_pose_score.lib` and `/usr/local/share/IMP/atom/protein_ligand_rank_score.lib`) 

"Two different scoring files are provided:
    - protein_ligand_pose_score.lib for use when one wants to find the
    most near-native poses of a ligand from many geometry decoys of the
    same ligand
    - protein_ligand_rank_score.lib for use when screening a compound database
    against a single protein to choose putative binders"
    
Source: [http://svn.salilab.org/imp/trunk/applications/ligand_score/README.md](README.md)    
    
(On a Mac, the library files are typically located at: `/usr/local/share/IMP/atom/protein_ligand_pose_score.lib` and `/usr/local/share/IMP/atom/protein_ligand_rank_score.lib`)    

**Example:**

	ligand_score my.mol2 my.pdb /usr/local/share/IMP/atom/protein_ligand_pose_score.lib

**Version:**

Not individually available for `ligand_score`, see IMP version (IMP 2.2.0).

<br>
<br>
<br>
<br>

<a class="mk-toclify" id="protein-file-and-structure-processing"></a>
## Protein file and structure processing
[[back to top](#table-of-contents)]

<br>
<br>

<a class="mk-toclify" id="openbabel"></a>
### OpenBabel
[[back to top](#table-of-contents)]

A conversion tool for different file formats. Comes with standalone binaries and APIs for various programming languages.

Website: [http://openbabel.org](http://openbabel.org)

*O'Boyle, Noel M., Michael Banck, Craig A. James, Chris Morley, Tim Vandermeersch, and Geoffrey R. Hutchison. “Open Babel: An Open Chemical Toolbox.” J Cheminf 3 (2011): 33.*

**Usage:**

	babel -H
	Open Babel converts chemical structures from one file format to another

	Usage: babel <input spec> <output spec> [Options]
	
**Example:**

	babel -i mol2 my.mol2 -o pdbqt my.pdbqt


**Version:**

	babel
	No output file or format spec!
	Open Babel 2.3.1 -- Oct 13 2011 -- 15:14:47

<br>
<br>



<a class="mk-toclify" id="reduce"></a>
### Reduce
[[back to top](#table-of-contents)]

A command-line tool that adds/removes hydrogen-atoms to/from proteins and ligands in PDB format.

Website: [http://kinemage.biochem.duke.edu/software/reduce.php](http://kinemage.biochem.duke.edu/software/reduce.php)


*Word, et al.(1999) "Asparagine and glutamine: using hydrogen atom contacts in the choice of sidechain amide orientation" J. Mol. Biol. 285, 1735-1747.*

Usage:

	~/Desktop >./reduce -h
	reduce: version 3.23 05/21/2013, Copyright 1997-2013, J. Michael Word
	reduce.3.23.130521
	arguments: [-flags] filename or -

	Suggested usage:
	reduce -FLIP myfile.pdb > myfileFH.pdb (do NQH-flips)
	reduce -NOFLIP myfile.pdb > myfileH.pdb (do NOT do NQH-flips)

	Flags:
	-FLIP             add H and rotate and flip NQH groups
	-NOFLIP           add H and rotate groups with no NQH flips
	-Trim             remove (rather than add) hydrogens

	-NUClear          use nuclear X-H distances rather than default
	                  electron cloud distances
	-NOOH             remove hydrogens on OH and SH groups
	-OH               add hydrogens on OH and SH groups (default)

	-HIS              create NH hydrogens on HIS rings
	-FLIPs            allow complete ASN, GLN and HIS sidechains to flip
	                        (usually used with -HIS)
	...
	
	
**Version:**

	reduce -v
	reduce.3.23.130521
	
	
<br>
<br>	
	
<a class="mk-toclify" id="multi-purpose"></a>
## Multi-purpose tools and libraries
[[back to top](#table-of-contents)]

<br>
<br>


<a class="mk-toclify" id="biopython"></a>
### Biopython
[[back to top](#table-of-contents)]

A collection of different tools written in Python

Website: [http://biopython.org/wiki/Main_Page](http://biopython.org/wiki/Main_Page)

<br>
<br>

<a class="mk-toclify" id="scikit-bio"></a>
### scikit-bio
[[back to top](#table-of-contents)]

A Python package with various functions, data structures, and algorithms for biosciences written in Python.

Website: [http://scikit-bio.org](http://scikit-bio.org)


<br>
<br>

<a class="mk-toclify" id="proteowizard"></a>
### ProteoWizard
[[back to top](#table-of-contents)]

A library of GUI and command line tools for proteomics analyses

Website: [http://proteowizard.sourceforge.net/index.shtml](http://proteowizard.sourceforge.net/index.shtml)
