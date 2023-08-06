### file contains Ovito's user-defined modifiers

import numpy as np


def scale_RGB_color(RGB=(255,255,255)):
    """ Function to convert RGB color code from scale 0-255 to scale 0-1.

	Args:
		RGB (tuple): RGB code in scale 0-255

	Returns:
		rgb (tuple): RGB code in scale 0-1

	Examples:
		```py
		rgb = scale_RGB_color((255,255,255)))
		```

	???+ tip "See also"
	    1. [rgb-values-to-0-to-1-scale](https://stackoverflow.com/questions/10848990/rgb-values-to-0-to-1-scale)

	"""
    return tuple(np.asarray(RGB)/255)


def mod_set_prop_atom_name(frame, data):
    """ Modifier to set atom names

	Examples:
		```py
		from thatool.visual.ovito_modifier import mod_set_prop_atom_name
		from ovito.io import import_file

		pipeline = import_file("test.cfg")
		pipeline.add_to_scene()
		## add mod
		dict_name = {'type_id':[1, 2], 'atom_name':['C', 'H']}
		pipeline.modifiers.append(mod_set_prop_atom_name)
		```

	???+ note
	    - So far, can not a custom argument to modifier, [see here](https://www.ovito.org/forum/topic/passing-arguments-to-a-custom-python-modifier/). So we need to define a `global variable` before using this function
			```
			dict_name = {'type_id':(1, 2), 'atom_name':('C', 'H')}
			```
	    - Do not use 'return` in modifier
	    - the underscore notation mean modifiable version of the quantity in ovito


	???+ tip "See also"
	    1. [Pass custom args to modifier](https://www.ovito.org/forum/topic/passing-arguments-to-a-custom-python-modifier/)
	    2. [ovito.data.Property](https://www.ovito.org/docs/current/python/modules/ovito_data.html#ovito.data.Property)
			- type.id, type.name, type.color, type.radius

    """
    tprop = data.particles_.particle_types_      # the underscore notation mean modifiable version of the quantity in ovito
    for i,ty in enumerate(tprop):
        for j,item in enumerate(dict_name['type_id']):
            if ty == item:
                tprop.type_by_id_(ty).name = dict_name['atom_name'][j]


def mod_set_prop_atom_color_PMMAori(frame, data):
    """ Modifier to assign atom colors based on atom_names.

	Examples:
		```py
		from thatool.visual.ovito_modifier import mod_set_prop_atom_color_PMMAori
		from ovito.io import import_file

		pipeline = import_file("test.cfg")
		pipeline.add_to_scene()
		## add mod
		pipeline.modifiers.append(mod_set_prop_atom_color_PMMAori)
		```
    """
    tprop = data.particles_.particle_types_      # the underscore notation mean modifiable version of the quantity in ovito
    for i,ty in enumerate(tprop):
        if tprop.type_by_id_(ty).name =="C1":
            tprop.type_by_id_(ty).color = scale_RGB_color((0, 85, 127))
        if tprop.type_by_id_(ty).name =="H":
            tprop.type_by_id_(ty).color = scale_RGB_color((255, 170, 0))
            # tprop.type_by_id_(ty).radius = 0.46






