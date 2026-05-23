#!/usr/bin/env python3

# ===========================================================================|
# Imports
class Color:

    def __init__(self,r,g,b)
        self.r = r
        self.g = g
        self.b = b

from typing import List, Tuple


def blend_even(colors: List(Color)):
    strength = 1/len(colors)

    output = Color(0,0,0) # starting pure black

    for color in colors:
        output.r += strength * color.r
        output.g += strength * color.g
        output.b += strength * color.b
    return output

def blend(colors: List(Color), ratios: List(float)):

    # order matters as we are matching ratio to color pair-wise

    if len(colors) != len(ratios):
        return null

    
    pairs = List(Zip(colors,ratios))

    for color,strength in pairs:
        output.r += strength * color.r
        output.g += strength * color.g
        output.b += strength * color.b
    return output

    
    










# ===========================================================================|
