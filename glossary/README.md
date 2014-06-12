- [Apo structure](#apostructure)
- [Conformation](#conformation)
- [Holo structure](#holostructure)
- [Orientation](#orientation)
- [Pose](#pose)
- [Root-mean-square deviation(RMSD)](#RMSD)


<br>
<br>
<hr>

<a id='apostructure'></a>
#### Apo structure 
The observed structure of a protein if its ligand is not bound. In contrast to [holo structure](#holostructure)

<a id='conformation'></a>
#### Conformation   

- Ligands/proteins can exist in different conformations. Usually, "conformation" refers to the same chemical composition but with altered bond-angles between two/multiple ligands or proteins. See also [orientation](#orientation).

![ligand conformation](./images/ligand_conformation.png)


<a id='holostructure'></a>
#### Holo structure    
The observed structure of a protein in its ligand bound state. In contrast to [apo structure](#apostructure)


<a id='orientation'></a>
#### Orientation

- In contrast to [conformation](#conformation), the bond angles are the same between two/multiple ligands (as well as the chemical composition), but the orientation in space (transition, global rotation) is differs between two/multiple orientations.

![ligand orientation](./images/ligand_orientation.png)


<a id='pose'></a>
#### Pose  
A ligand pose describes the binding-mode of a ligand in a protein binding site. Typically, this is considered to be a combination of [orientation](#orientation) & [conformation](#conformation)

<a id='RMSD'></a>
#### Root-mean-square deviation (RMSD) 
The RMSD measures the average distance between atoms of 2 protein or ligand structures via the equation

![rmsd equation](./images/rmsd_equation.png)

where *a_i* refers to the atoms of molecule 1, and *b_i* to the atoms of molecule 2, respectively. The subscripts *x, y, z* are denoting the x-y-z coordinates for every atom.

The RMSD is most commonly calculated without taking hydrogen-atoms into consideration (typically only C-alpha or main-chain atoms in proteins).

![Ligand overlay](./images/ligand_overlay_rmsd.png)

(overlay between 2 ligand structures, RMSD = 1.9959 Angstrom)