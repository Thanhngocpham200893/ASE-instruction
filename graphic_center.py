import numpy as np
import os
import sys


if len(sys.argv) == 4:
    atom_structure           = str(sys.argv[1])
    prefix                   = str(sys.argv[2])
    view                     = str(sys.argv[3]) 
else:
    sys.exit('make_graphic.py atomic_structure  prefix view[side]')



from ase import Atoms
from ase.io import write, read
from ase.build import molecule
from ase.io.pov import get_bondpairs, set_high_bondorder_pairs
slab = read(atom_structure, index = -1)
slab.center(axis=(0,1))
cluster  = slab[[atom.index for atom in slab if atom.position[2] > 0.4]]
com      = cluster.get_center_of_mass()
cell_slab = slab.get_cell(complete = True)
com_slab = 0.5*( cell_slab[0] + cell_slab[1] + cell_slab[2])
dis = [com_slab[0] - com[0], com_slab[1] - com[1] , com_slab[2] - com[2] ]
slab.translate(dis)
slab.wrap()
slab.center(axis=(0,1))

#bondpairs = get_bondpairs(slab, radius=1.0)
#high_bondorder_pairs = {}
#bondpairs = set_high_bondorder_pairs(bondpairs, high_bondorder_pairs)

# View used to start ag, and find desired viewing angle
# view(atoms)

if view == 'side':
    rot = '-60x,0y,0z'  # found using ag: 'view -> rotate'
    unit_cell = (1,1,1)
else:
    rot = '0x,0y,0z'  # found using ag: 'view -> rotate'
    unit_cell = (1,1,1)

slab = slab*unit_cell
###make the radius
"""
radius = []
for atom in slab:
    if atom.position[2] > 0.5:
        if atom.symbol == 'Pd':
            radius.append(0.9)
        elif atom.symbol =='O':
            radius.append(0.7)
    else:
        if atom.symbol == 'Pd':
            radius.append(0.5)
        elif atom.symbol =='O':
            radius.append(0.3)
        elif atom.symbol =='Ti':
            radius.append(0.5)
        elif atom.symbol =='Sr':
            radius.append(0.6)
        elif atom.symbol =='Cu':
            radius.append(0.3)

print(radius)
"""
        

# Common kwargs for eps, png, pov
generic_projection_settings = {
    'rotation': rot,  # text string with rotation (default='' )
    'radii': 0.8,  # float, or a list with one float per atom
    'colors': None,  # List: one (r, g, b) tuple per atom
    'show_unit_cell': 1,   # 0, 1, or 2 to not show, show, and show all of cell
}

# Extra kwargs only available for povray (All units in angstrom)
povray_settings = {
    'display': False,  # Display while rendering
    'pause': True,  # Pause when done rendering (only if display)
 #   'transparent': False,  # Transparent background
    'canvas_width': 1200,  # Width of canvas in pixels
    'canvas_height': None , # Height of canvas in pixels
    'camera_dist': 50.,  # Distance from camera to front atom
    'image_plane': None,  # Distance from front atom to image plane
    'camera_type': 'orthographic',  # perspective, ultra_wide_angle, orthohraphic
    'point_lights': [],             # [[loc1, color1], [loc2, color2],...]
    'area_light': [(2., 3., 40.),  # location
                   'White',       # color
                   .7, .7, 3, 3],  # width, height, Nlamps_x, Nlamps_y
    'background': 'White',        # color
#    'bondatoms' : bondpairs,
    'textures': None,  # Length of atoms list of texture names
    'celllinewidth': 0.1,  # Radius of the cylinders representing the cell
}

# Write the .pov (and .ini) file.
# comment out render not call the povray executable
renderer = write('%s.pov' %(prefix), slab,
                 **generic_projection_settings,
                 povray_settings=povray_settings)

renderer.render()
