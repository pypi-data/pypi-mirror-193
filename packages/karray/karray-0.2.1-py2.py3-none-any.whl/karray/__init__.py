# karray
# copyright 2022, Carlos Gaete-Morales, DIW-Berlin 
"""
    karray
    copyright 2022, Carlos Gaete-Morales, DIW-Berlin 
"""
__version__ = (0, 2, 1)
__author__ = 'Carlos Gaete-Morales'


from .arrays import Long, Array, numpy_to_long, concat, from_feather, _from_feather, from_pandas, from_polars, _from_csv, from_csv
from .setting import settings