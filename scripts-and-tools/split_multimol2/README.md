
# protein-science - Scripts and Tools

## Efficient Multi-MOL2 File Splitter

Sebastian Raschka, 09/01/2014  
** Version 1.0**

<br>
<br>

<hr>
I would be happy to hear your comments and suggestions. 
Please feel free to drop me a note via
[twitter](https://twitter.com/rasbt), [email](mailto:bluewoodtree@gmail.com), or [google+](https://plus.google.com/+SebastianRaschka).
<hr>

<br>
<br>


The `split_multimol2.py` splits a file that contains multiple MOL2 structures into individual MOL2 files where the names of the output files correspond to the name of the molecule in the input file.

**Even very large multi-mol2 files (up to Gigabytes) can be parsed efficiently** due to the usage of a generator expression, thus, `split_multimol2.py` avoids reading in the whole file into memory at once, but processes it incrementally.



<br>
<br>

### Requirements:

- Python 2.7.x or Python 3.x

<br>
<br>



### Usage:

run `python ./split_multimol2.py --help` for the usage information:

<pre>
usage: split_multimol2.py [-h] [-v] MOL2_FILE OUT_DIR

Splits a multi-mol2 file into individual mol2 files

positional arguments:
  MOL2_FILE
  OUT_DIR

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
</pre>

<br>
<br>

### Example: center of mass of a protein

command:

	python ./split_multimol2.py confs.mol2 my_out_dir

output:

![](./images/overview_1.png)