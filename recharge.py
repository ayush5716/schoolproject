# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:32:38 2020

@author: ayush class 12B
"""
import csv
with open('RECHARGE.csv','a',newline='') as afile:
    write=csv.writer(afile,lineterminator='\n')
    write.writerow(["Customer_Mobile","Recharge_Date","Recharge_Amount","Service_provider"])
def enter():
    with open('RECHARGE.csv','a+',newline='') as bfile:
        write=csv.writer(bfile,lineterminator='\n')
        write.writerow([Customer_Mobile,Recharge_Date,Recharge_Amount,Service_Provider])
def collection():
    p=('|  {:^15s}  |  {:^15s}  |  {:^16s}  |  {:^15s}  |'.format(Recharge_Date,Customer_Mobile,Service_Provider,Recharge_Amount)+"\n")
    with open('collect.txt','a+') as pfile:
        pfile.write(p)
    pfile.close()
def printbill():
    with open('collect.txt','r') as rfile:
        cont=rfile.readlines()
        print("-"*86)
        print('{:^80s}'.format("AYUSH CELLPHONE LTD."))
        print('{:^80s}'.format("BHILAI"))
        print("-"*86)
        print("  "+'|  {:^15s}  |  {:^15s}  |  {:^16s}  |  {:^15s}  |'.format('recharge date','cumtomer mobile','service provider','recharge amount'))
        print("-"*86)
        for content in cont:
            content=content.rstrip('\n').split('#')
            print(content)
        print('-'*86)
add_recharge="yes"
packs=["10","20","50","100","200"]
while add_recharge=="yes":
    add_recharge=input("Do you want to enter one more recharge info. (yes/no):")
    if add_recharge=="yes":
        Customer_Mobile=input("Enter mobile number:")
        Recharge_Date=input("Enter date(dd/mm/yy):")
        Recharge_Amount=input("Enter the recharge amount:")
        while Recharge_Amount not in packs:
            print("there is no pack available in this amount")
            Recharge_Amount=input("Please anter a valid recharge amount:")
        Service_Provider=input("Enter you service provider name:")
        enter()
        collection()
    else:
        print("your recharge details have been noted.")
        break
printbill()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
