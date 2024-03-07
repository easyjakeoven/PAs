# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:18:29 2024

@author: JCCarpenter
"""

import numpy as np


def rooter(var, der, xn, it_num):
    # Calculate x's output
    new_var = np.polyval(var, xn)
    new_der = np.polyval(der, xn)   
    
    # Produces new root answer
    calc = new_var / new_der
    xn1 = round(xn - calc, 3)
    print(f'x{it_num} = {xn1}')
    
    # If the rounded root does not equal the last one, perform again
    if xn1 != xn:
        it_num += 1
        rooter(var, der, xn1, it_num)
    else:
        print(f'The final value with stabilized thousandths place is {xn}')



def main():
    # Create the user's polynomial
    num_polys = int(input("Input highest x exponent: "))
    var = []
    for i in range(num_polys):
        j = num_polys - i
        var.append(int(input(f"Coefficient for x^{j}: ")))
    
    var.append(int(input("Coefficient for x: ")))
    xn = float(input("Enter initial value: "))
    
    # Create them into numpy polynomials
    var = np.poly1d(var)
    der = np.polyder(var)
    rooter(var, der, xn, 1)
    
    # Output the roots
    print(f'Roots: {np.roots(var)}')
    
    
    
main()