#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Matplot"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    '''Plot something'''
    x_coord = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x_coord, np.sin(x_coord))       # Plot the sine of each x point
    plt.show()                   # Display the plot

if __name__ == "__main__":
    main()
