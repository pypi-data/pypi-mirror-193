"""Python Bayesian Networks
"""

__version__ = '1'


try:
    import numpy as np
except ImportError:
    raise ImportError('NumPy no esta instalado, por favor instalelo con el comando pip')


from .network import *
from .nodes import *
            
        