# SOL https://py-pkgs.org/04-package-structure.html
# read version from installed package
import sys
from importlib.metadata import version
__version__ = version("dipwmsearch")

# ##################################################
# print ( __version__ )
sys.stderr.write( f"version {__version__}\n"  )
# ##################################################

from .AhoCorasick import *
# from .BestWords import *
from .Block import *
from .diPwm import *
from .Enumerate import *
from .SemiNaive import *
# from .Super import *
# Q: do we need the following line?
# from .__main__ import *
#
