import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from obrpy import obrpy

obrpy_obj = obrpy()
obrpy_obj.save()
obrpy_obj.load()