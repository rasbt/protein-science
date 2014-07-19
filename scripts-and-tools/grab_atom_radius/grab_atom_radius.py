# Sebastian Raschka 2014
# Script that extracts atoms within a radius from a PDB file


def grab_radius(file, radius, coordinates, include='ATOM,HETATM'):
    """
    Grabs those atoms that are within a specified
    radius of a provided 3d-coordinate.

    Keyword arguments:
        file: path to a PDB file
        radius: radius in angstrom (float or integer)
        coordinates: a list of x, y, z coordinates , e.g., [1.0, 2.4, 4.0]
        include: coordinate lines to include (default: "ATOM,HETATM")

    Returns:
        A list that contains the pdb contents that are within the specified
        radius.

    """
    include = tuple(include.split(','))
    
    with open(file, 'r') as pdb_file:
        pdb_cont = [row.strip() for row in pdb_file.read().split('\n') if row.strip()]
        
    in_radius = []
    for line in pdb_cont:
        if line.startswith(include):
            xyz_coords = [float(line[30:38]),\
                          float(line[38:46]),\
                          float(line[46:54])]
            distance = (sum([(coordinates[i]-xyz_coords[i])**2 for i in range(3)]))**0.5
            if distance <= radius:
                in_radius.append(line)
    return in_radius


if __name__ == '__main__':
    
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Extracts atoms within a radius from a PDB file.\n'\
                    'By default, all atoms in the PDB file are included in the calculation.',
        formatter_class=argparse.RawTextHelpFormatter
        )
    

    # positional arguments
    parser.add_argument('PDBfile')
    parser.add_argument('-r', '--radius',
            type=float, 
            metavar='int/float',
            default='10.0',
            help='radius in Angstrom for atoms to extract (default 10.0)')
            
    parser.add_argument('-c', '--coordinates',
            type=str, 
            metavar='X,Y,Z',
            default='0,0,0',
            help='center for extracting atoms (default "0,0,0")')
    
    # optional arguments
    parser.add_argument('-i', '--include', type=str, 
            default='ATOM,HETATM', 
            metavar='coordinate-ID',
            help='Coordinate lines to include (default: "ATOM,HETATM")')
    parser.add_argument('-o', '--out', metavar='out.fasta', type=str, 
                help='writes atoms to an output file instead of printing it to the screen')
                          
                
    args = parser.parse_args()
    

    coords = args.coordinates.split(',')
    coords = [float(i) for i in coords]
    
    residues = grab_radius(args.PDBfile, args.radius, coords)    
    
    if args.out:
        with open(args.out, 'w') as out:
            for line in residues:
                out.write(line + '\n')
                
    else:
        for line in residues:
            print(line)
                
    


