#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:21:53 2020

@author: dbrims
"""

import csv

#pull data from menu file and create a nested loop of the data

menu=[]

with open('./data/menu_data.csv') as data:
    file_data = csv.reader(data, delimiter=',')
    next(file_data)
    for row in file_data:
        menu.append(row)
        
    
sales=[]
with open('./data/sales_data.csv') as data:
    file_data = csv.reader(data, delimiter=',')
    next(file_data)
    for row in file_data:
        for item in row:
            sales.append(item)           

          
report={}
metrics=['01-count','02-revenue','03-cogs','04-profit']

    
sales_item=[]
sales_quantity=[] 
sales_len=len(sales) 

for ele in range(3, sales_len, 5):
    sales_quantity.append(int(sales[ele]))
for ele in range(4,sales_len, 5):
    sales_item.append(sales[ele])  

for item in sales_item:
    if item not in report:
        report[item]={}
        for m in metrics:
            report[item][m]=0
         
menu_item=[]
cost=[]
price=[]
for row in menu:
    for item in range(len(row)):
        if item==0:
            menu_item.append(row[item])

        elif item==3:
            price.append(float(row[item]))
    
        elif item==4:
            cost.append(float(row[item]))           
            
len_items=len(menu_item)
len_sales_item=len(sales_item)

for x in range(len_sales_item):
    match=False
    for y in range(len_items):
        if menu_item[y]==sales_item[x]:
            profit=price[y]-cost[y]
            report[sales_item[x]]["01-count"] += sales_quantity[x]
            report[sales_item[x]]["02-revenue"] += price[y] * sales_quantity[x]
            report[sales_item[x]]["03-cogs"] += cost[y] * sales_quantity[x]
            report[sales_item[x]]["04-profit"] += profit * sales_quantity[x]
            match=True
    if match==False:
        print(f"{sales_item} does not equal {menu_item}! NO MATCH!")
        

with open('pyramen2.txt','w') as f:       
    for key in report:
        f.write(str(key)+' '+str(report[key])+'\n')   

 
    

            

            
           
    
            

            

        

        
    

    
    

