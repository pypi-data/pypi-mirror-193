## function to set style for matplotlib
## return path to file *.mplstyle

"""
Set style for matplotlib

New use:

```py
from thatool.vis         import matplot_style
import matplotlib.pyplot as plt
plt.style.use(matplot_style.light)
```
```py
## to see all availabes styles
matplot_style.all_types
```

Old use:

```py
from thatool.vis         import matplot_param
import matplotlib.pyplot as plt
plt.rcParams.update(matplot_param.myPARAM)
```

Figure size [Elsevier](https://www.elsevier.com/authors/policies-and-guidelines/artwork-and-media-instructions/artwork-sizing)
- Single column: W = 90 mm (~3.5 in). H = W*4/5 = 2.8
- Double column: W = 190 mm (~7.5 in). H = 6
"""

from pathlib   import Path



MPL_PATH = Path(__file__).parent.resolve()/"mplstyle"   # path Obj


### ============================================================================
### mplstyle
### ============================================================================
light = str(MPL_PATH/"light.mplstyle")    # string

## return all available styles
p = MPL_PATH.glob('*.mplstyle')
all_styles = [n.stem for n in p]



### ============================================================================
### Some pre define data
### ============================================================================
myCOLOR = ['black','red','blue','green','magenta','orange','lime','cyan','violet','purple','olive','gray','yellow','navy','saddlebrown','darkgreen','lawngreen', 'lightgreen','steelblue','darkcyan','plum','slateblue','indigo']

## marker: https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
myMARKER = ['o','s','D','p','*','^','d','H','X','>','<','^']

## linestyle: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
myLINE = {
     'solid': 'solid',      # Same as (0, ()) or '-'
     'dotted': 'dotted',    # Same as (0, (1, 1)) or ':'
     'dashed': 'dashed',    # Same as '--'
     'dashdot': 'dashdot',  # Same as '-.'

     'loosely dotted':        (0, (1, 10)),
     'dotted':                (0, (1, 1)),
     'densely dotted':        (0, (1, 1)),

     'loosely dashed':        (0, (5, 10)),
     'dashed':                (0, (5, 5)),
     'densely dashed':        (0, (5, 1)),

     'loosely dashdotted':    (0, (3, 10, 1, 10)),
     'dashdotted':            (0, (3, 5, 1, 5)),
     'densely dashdotted':    (0, (3, 1, 1, 1)),

     'dashdotdotted':         (0, (3, 5, 1, 5, 1, 5)),
     'loosely dashdotdotted': (0, (3, 10, 1, 10, 1, 10)),
     'densely dashdotdotted': (0, (3, 1, 1, 1, 1, 1))
	}

