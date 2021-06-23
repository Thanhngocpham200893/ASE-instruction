###Sort the atoms with chemical symbol order
Ca = bulk[[atom.index for atom in bulk if atom.symbol =='Ca']]
O  = bulk[[atom.index for atom in bulk if atom.symbol =='O']]
Ti = bulk[[atom.index for atom in bulk if atom.symbol =='Ti']]
surf = Ca + O + Ti


###set constrainst for the atom with z position is less than 8.5 angstrom 
c = FixAtoms(indices = [atom.index for atom in surf if atom.position[2] < 8.5])
surf.set_constraint(c)

###set initial magnetic moments for Ca16O48Ti16
surf.set_initial_magnetic_moments(16*[0]+48*[0]+16*[2])
