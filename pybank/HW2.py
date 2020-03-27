#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 07:46:51 2020

@author: dbrims
"""

import csv

#initialize two lists to accept CSV data
dates=[]
pnl=[]

#open CSV file and read in data
with open('./data/budget_data.csv', 'r') as f:
    file_data = csv.reader(f, delimiter=',')
    next(file_data)
    for row in file_data:
        dates.append(row[0])
        pnl.append(float(row[1]))
pnl_dict=dict(zip(dates, pnl))


pnl_len=len(pnl_dict)
pnl_high_key=dates[0]
pnl_low_key=dates[0]

#cycle through dictionary, summing P&L values and find the lowest and highest value
pnl_sum=0
for key in pnl_dict:
    pnl_sum=+(pnl_dict[key])
    if (pnl_dict[pnl_high_key])<(pnl_dict[key]):
        pnl_high_key=key
    if (pnl_dict[pnl_low_key])>(pnl_dict[key]):
        pnl_low_key=key
pnl_ave=pnl_sum/pnl_len

#print results
print('Financial Analysis')
print('-'*20)
print(f'P&L for {pnl_len} month inclusive of {dates[0]} to {dates[-1]}')
print(f'Total P&L change: ${pnl_sum:.0f}')
print(f'Average Change in P&L: ${pnl_ave:.2f}')
print(f'Greatest Increase in Profits: ${pnl_dict[pnl_high_key]:.0f} on {pnl_high_key}')
print(f'Greatest Decrease in Profits: ${pnl_dict[pnl_low_key]:.0f} on {pnl_low_key}')
