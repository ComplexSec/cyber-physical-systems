from pymodbus.client import ModbusTcpClient as Client
import csv
import time
import threading
import pandas as pd

# Monitors values of a set of 20 holding registers over 25 seconds
# Output is a CSV file with each column a different register

def IP_10_holding(): # define function for 192.168.95.10 Holding Registers
    with open('192.168.95.10-holding.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        client = Client('192.168.95.10') 
        for i in range(100):    #collect a total of 100 samples
            row = []
            print('sample number ' + repr(i))
            for j in range(0,10):    #scrape register addresses 0-9
                #read one register at address j
                response = client.read_holding_registers(j,1)
                #extract the value and add it to the row
                row.append(response.registers[0])
            writer.writerow(row)    #write row of data to file
            time.sleep(1)    #wait 1 seconds between samples
       
def IP_11_holding(): # define function for 192.168.95.11 Holding Registers        
    with open('192.168.95.11-holding.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        client = Client('192.168.95.11') 
        for i in range(100):    #collect a total of 100 samples
            row = []
            print('sample number ' + repr(i))
            for j in range(0,10):    #scrape register addresses 0-9
                #read one register at address j
                response = client.read_holding_registers(j,1)
                #extract the value and add it to the row
                row.append(response.registers[0])
            writer.writerow(row)    #write row of data to file
            time.sleep(1)    #wait 1 seconds between samples
        
def IP_12_holding(): # define function for 192.168.95.12 Holding Registers  
    with open('192.168.95.12-holding.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        client = Client('192.168.95.12') 
        for i in range(100):    #collect a total of 100 samples
            row = []
            print('sample number ' + repr(i))
            for j in range(0,10):    #scrape register addresses 0-9
                #read one register at address j
                response = client.read_holding_registers(j,1)
                #extract the value and add it to the row
                row.append(response.registers[0])
            writer.writerow(row)    #write row of data to file
            time.sleep(1)    #wait 1 seconds between samples
        
def IP_13_holding(): # define function for 192.168.95.13 Holding Registers  
    with open('192.168.95.13-holding.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        client = Client('192.168.95.13') 
        for i in range(100):    #collect a total of 100 samples
            row = []
            print('sample number ' + repr(i))
            for j in range(0,10):    #scrape register addresses 0-9
                #read one register at address j
                response = client.read_holding_registers(j,1)
                #extract the value and add it to the row
                row.append(response.registers[0])
            writer.writerow(row)    #write row of data to file
            time.sleep(1)    #wait 1 seconds between samples

def IP_14_holding(): # define function for 192.168.95.14 Holding Registers  
    with open('192.168.95.14-holding.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        client = Client('192.168.95.14') 
        for i in range(100):    #collect a total of 100 samples
            row = []
            print('sample number ' + repr(i))
            for j in range(0,10):    #scrape register addresses 0-9
                #read one register at address j
                response = client.read_holding_registers(j,1)
                #extract the value and add it to the row
                row.append(response.registers[0])
            writer.writerow(row)    #write row of data to file
            time.sleep(1)    #wait 1 seconds between samples
            
def IP_15_holding(): # define function for 192.168.95.15 Holding Registers  
    with open('192.168.95.15-holding.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        client = Client('192.168.95.15') 
        for i in range(100):    #collect a total of 100 samples
            row = []
            print('sample number ' + repr(i))
            for j in range(0,10):    #scrape register addresses 0-9
                #read one register at address j
                response = client.read_holding_registers(j,1)
                #extract the value and add it to the row
                row.append(response.registers[0])
            writer.writerow(row)    #write row of data to file
            time.sleep(1)    #wait 1 seconds between samples
            
################### MULTITHREADING TO CAPTURE DATA AT THE SAME TIME - NO DELAYS #######################            

thread10 = threading.Thread(target=IP_10_holding)
thread10.start()
thread11 = threading.Thread(target=IP_11_holding)
thread11.start()
thread12 = threading.Thread(target=IP_12_holding)
thread12.start()
thread13 = threading.Thread(target=IP_13_holding)
thread13.start()
thread14 = threading.Thread(target=IP_14_holding)
thread14.start()
thread15 = threading.Thread(target=IP_15_holding)
thread15.start()
