# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:06:00 2024

@author: melvi
"""

import openpyxl

# Create a new workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Sample RF scanning data as a list of lists
rf_scanning_data = ["AWB", "REF#","SCHI","ON HAND#"]
