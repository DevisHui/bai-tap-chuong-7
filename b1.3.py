# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:47:55 2024

@author: Chi
"""

n=int(input("Nhập số = "))
def chanam(a):
    return a < 0 and a % 2 == 0
print(chanam(n))