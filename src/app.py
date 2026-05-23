#!/usr/bin/env python3

# ==================================================================|
# Import Statements
import streamlit as st
import matplotlib.pyplot as plt

n_colors = 10
combo_options = [
    "additive",
    "multiplicative",
]
colors, combo_fns, wheel = st.columns(3)
color_vals = []

with colors:
    num_colors = st.slider("number of colors:", 1, n_colors, 1)
    colors = st.empty()
    for i in range(num_colors):
        color = st.color_picker(f"color {i+ 1}")
        color_weight = st.number_input(f"relative weight", 0, 1, key=i)
        color_vals.append([color, color_weight])


with combo_fns:
    combos = st.pills("combinations:", combo_options)

with wheel:
    pass
