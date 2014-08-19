Sebastian Raschka

Last updated: 08/19/2014

<a class="mk-toclify" id="table-of-contents"></a>

#Table of Contents
- [Apo structure](#apo-structure)
- [B-factor](#b-factor)
- [Binding affinity](#binding-affinity)
- [Conformation](#conformation)
- [High-throughput screening](#high-throughput-screening)
- [Holo structure](#holo-structure)
- [Lennard-Jones Potential](#lennard-jones-potential)
- [Molecular Mechanics and Molecular Dynamics](#molecular-mechanics-and-molecular-dynamics)
- [Orientation](#orientation)
- [Pose](#pose)
- [R-factor](#r-factor)
- [Root-mean-square deviation (RMSD)](#root-mean-square-deviation-rmsd)
- [Van der Waals force](#van-der-waals-force)
- [Virtual screening](#virtual-screening)





<br>
<br>
<hr>


<a class="mk-toclify" id="apo-structure"></a>
#### Apo structure 

[[back to top](#table-of-contents)]

The observed structure of a protein if its ligand is not bound. In contrast to [holo structure](#holo-structure)

<br>
<br>


<a class="mk-toclify" id="b-factor"></a>
#### B-factor 

[[back to top](#table-of-contents)]

The B-factor (original name: Debye-Waller factor) is sometimes also called temperature factor, since it describes the thermal mobility of an atom based on the amount of scatter in the X-ray crystallographic experiment.

High B-factor values are usually associated with high mobility of an atom. However, a high B-factor value must not necessarily be associated with a flexible region, but can also indicate experimental uncertainty (i.e., positional errors).  
Typical B-factor values are around 15-20 A<sup>2</sup>.

![](./images/3eiy_by_bfactor.png)
![](./images/bfactor_colorbar.png)

The image above shows a protein (inorganic pyrophosphatase, [3eiy](http://www.rcsb.org/pdb/explore.do?structureId=3EIY)) colored by its B-factor values (PyMol command: `spectrum b, blue_white_red, minimum=20, maximum=50`).

<br>
<br>

<a class="mk-toclify" id="binding-affinity"></a>
#### Binding affinity

[[back to top](#table-of-contents)]

Binding affinity describes the strength of intermolecular interactions in a binding interface between a ligand (typically, a small chemical compound) and a protein binding site. The components of intermolecular interactions are composed of electrostatic interactions (ionic bonds), hydrogen bonds, and [van der Waals forces](#van-der-waals-forces).

![](./images/binding_affinity.png)

The binding affinity is defined by the following equation:

![](./images/binding_affinity.gif)

with 

the ideal gas constant:  
![](./images/gas_constant.gif) 

*T* = Temperature

*&Delta;G* = [Gibbs Free Energy](#gibbs-free-energy)

<br>
<br>


<a class="mk-toclify" id="conformation"></a>
#### Conformation   
[[back to top](#table-of-contents)]

- Ligands/proteins can exist in different conformations. Usually, "conformation" refers to the same chemical composition but with altered bond-angles between two/multiple ligands or proteins. See also [orientation](#orientation).

![ligand conformation](./images/ligand_conformation.png)

<br>
<br>

<a class="mk-toclify" id="high-throughput-screening"></a>
#### High-throughput screening   

[[back to top](#table-of-contents)]  

High-throughput screening (HTS) is an experimental (in contrast to virtual screening) approach for drug discovery that were especially popular in the 1980's and 1990's. HTS uses automated mechanical devices, such as robots, in order to test up to millions of chemical compounds for activity.

<br>
<br>

<a class="mk-toclify" id="holo-structure"></a>
#### Holo structure    

[[back to top](#table-of-contents)]

The observed structure of a protein in its ligand bound state. In contrast to [apo structure](#apo-structure).

<br>
<br>

<a class="mk-toclify" id="lennard-jones-potential"></a>
#### Lennard-Jones Potential

[[back to top](#table-of-contents)]

The Lennard-Jones potential describes the energy potential between two non-bonded atoms based on their distance to each other; it is a mathematical approximation that is used in molecular dynamics to estimate the [van der Waals force](#van-der-waals-force).

![](./images/lennard_jones_1.gif)

V = intermolecular potential  
&sigma; = distance where V is 0  
r = distance between atoms, measured from one center to the other  
&epsilon; = interaction strength

![](./images/lennard_jones_graph_1.png)

<br>
<br>

<a class="mk-toclify" id="molecular-mechanics-and-molecular-dynamics"></a>
#### Molecular Mechanics and Molecular Dynamics 

[[back to top](#table-of-contents)]

Molecular Mechanics uses principles based on Newtonian mechanics to model molecular systems and so-called force fields to calculate potential energies of a molecular system.

Molecular Dynamics refers to computer simulations that involve the modeling of interactions and motions of a molecular system over time.

<br>
<br>

<a class="mk-toclify" id="orientation"></a>
#### Orientation

[[back to top](#table-of-contents)]

- In contrast to [conformation](#conformation), the bond angles are the same between two/multiple ligands (as well as the chemical composition), but the orientation in space (transition, global rotation) is differs between two/multiple orientations.

![ligand orientation](./images/ligand_orientation.png)

<br>
<br>

<a class="mk-toclify" id="pose"></a>
#### Pose  

[[back to top](#table-of-contents)]

A ligand pose describes the binding-mode of a ligand in a protein binding site. Typically, this is considered to be a combination of [orientation](#orientation) & [conformation](#conformation)

<br>
<br>

<a class="mk-toclify" id="r-factor"></a>
#### R-factor

[[back to top](#table-of-contents)]

The R-factor is one of several measures to assess the quality of a protein crystal structure. After building and refining an atomistic model of the crystal structure, the R-factor measures how well this model can describe the experimental diffraction patterns via the equation:

![](./images/r_factor.gif)

[]

Where *F* is the so-called static structure factor which measures the amount of electron scatter.
Thus, a perfect R-factor value would be 0; the RCSB ([http://www.rcsb.org](http://www.rcsb.org/pdb/101/static101.do?p=education_discussion/Looking-at-Structures/Rvalue.html)) reports that R-factors of 0.20 are typical whereas an R-factor for a random set of atoms would be 0.63.

Additionally, the related **R-free** measure was defined as more unbiased approach: It calculates the R-factor for 10% of the experimental data that was removed prior to the refinement (here: refinement is done on 90% of the experimental data).



<br>
<br>

<a class="mk-toclify" id="root-mean-square-deviation-rmsd"></a>
#### Root-mean-square deviation (RMSD) 

[[back to top](#table-of-contents)]

The Root-mean-square deviation (RMSD) measures the average distance between atoms of 2 protein or ligand structures. This calculation of the Cartesian error follows the equation

![rmsd equation](./images/rmsd_equation.png)

where *a_i* refers to the atoms of molecule 1, and *b_i* to the atoms of molecule 2, respectively. The subscripts *x, y, z* are denoting the x-y-z coordinates for every atom.

The RMSD is most commonly calculated without taking hydrogen-atoms into consideration (typically only C-alpha or main-chain atoms in proteins).

![Ligand overlay](./images/ligand_overlay_rmsd.png)

(overlay between 2 ligand structures, RMSD = 1.9959 Angstrom)


<br>
<br>

<a class="mk-toclify" id="van-der-waals-force"></a>
#### Van der Waals force

[[back to top](#table-of-contents)]

The Van der Waals force (after Johannes Diderik van der Waals) describes the sum of attractive and repulsive forces between atoms or molecules between dipole interactions. Basically, van der Waals forces describe the interaction between atoms that are not based on covalent bonds, hydrogen bonds, or other electrostatic interaction.  
In molecular dynamics, the van der Waals force is often approximated by the [Lennard-Jones potential](#lennard-jones-potential).

![](./images/van_der_waals.png)

<br>
<br>

<a class="mk-toclify" id="virtual-screening"></a>
#### Virtual screening

[[back to top](#table-of-contents)]

Virtual screening (VS) is a computer-aided, knowledge-driven approach for drug-discovery (in contrast to the experimental High-throughput screening (HTS)). Typically, a large database of small, drug-like compounds is screened for molecules that can fit into a protein-receptor binding interface.
