import os
import numpy
import sys
def calculate_distances(coords1, coords2):
    """
    This function accepts coordinates of two atoms and calculates distance btwn atoms
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12

def bond_check (distance, minimum = 0, maximum = 1.5):
    """
    Checks distance to determine if it is a bond. User specifys minimum and maximum
    """
    if minimum<distance_12<maximum:
        return True
    else:
        return False

file_location = sys.argv[1]
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
coordinates = coordinates.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0,num_atoms):
    for num2 in range(0,num_atoms):
        if num1>num2:
            distance_12 = calculate_distances(coordinates[num1], coordinates[num2])
            if bond_check(distance_12) is True:
                print (F'{symbols[num1]} to {symbols[num2]} :{distance_12}')
