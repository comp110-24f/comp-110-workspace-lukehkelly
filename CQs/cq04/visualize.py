"""Visualization file for CQ04"""

__author__ = "730761531"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(var1=x, var2=y))
get_coords(x, y)
