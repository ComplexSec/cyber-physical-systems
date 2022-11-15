"""
Created on Tue Nov 15 15:31:33 2022

@author: Complexity
@description: This code reads CSV files that contain data from scraping Holding Registers of Modbus devices in an ICS network. It plots these values into a graph
in order to visualize the values increasing or decreasing in real-time.
"""


import pandas as pd
from matplotlib import pyplot as plt

def holding_10():
    data = pd.read_csv('/home/kali/192.168.95.10-holding.csv',header=None)
         
    ###### PLOT 192.168.95.10
        
    fig0 = plt.figure(0)
    plt.plot(data[1])
    plt.xlabel("Time [s]",fontsize=13)
    plt.ylabel("Register value",fontsize=13)
    plt.title("Holding Registers for 192.168.95.10")
    fig0.savefig("Holding-11.png")
    plt.show()

def holding_11():
    data = pd.read_csv('/home/kali/192.168.95.11-holding.csv',header=None)
         
    ###### PLOT 192.168.95.10
        
    fig0 = plt.figure(0)
    plt.plot(data[1])
    plt.xlabel("Time [s]",fontsize=13)
    plt.ylabel("Register value",fontsize=13)
    plt.title("Holding Registers for 192.168.95.11")
    fig0.savefig("Holding-11.png")
    plt.show()
    
def holding_12():
    data = pd.read_csv('/home/kali/192.168.95.12-holding.csv',header=None)
         
    ###### PLOT 192.168.95.10
        
    fig0 = plt.figure(0)
    plt.plot(data[1])
    plt.xlabel("Time [s]",fontsize=13)
    plt.ylabel("Register value",fontsize=13)
    plt.title("Holding Registers for 192.168.95.12")
    fig0.savefig("Holding-12.png")
    plt.show()
    
def holding_13():
    data = pd.read_csv('/home/kali/192.168.95.13-holding.csv',header=None)
         
    ###### PLOT 192.168.95.10
        
    fig0 = plt.figure(0)
    plt.plot(data[1])
    plt.xlabel("Time [s]",fontsize=13)
    plt.ylabel("Register value",fontsize=13)
    plt.title("Holding Registers for 192.168.95.13")
    fig0.savefig("Holding-13.png")
    plt.show()
    
def holding_14():
    data = pd.read_csv('/home/kali/192.168.95.14-holding.csv',header=None)
         
    ###### PLOT 192.168.95.10
        
    fig0 = plt.figure(0)
    plt.plot(data[1])
    plt.xlabel("Time [s]",fontsize=13)
    plt.ylabel("Register value",fontsize=13)
    plt.title("Holding Registers for 192.168.95.14")
    fig0.savefig("Holding-14.png")
    plt.show()
    
def holding_15():
    data = pd.read_csv('/home/kali/192.168.95.15-holding.csv',header=None)
         
    ###### PLOT 192.168.95.10
        
    fig0 = plt.figure(0)
    plt.plot(data[1])
    plt.xlabel("Time [s]",fontsize=13)
    plt.ylabel("Register value",fontsize=13)
    plt.title("Holding Registers for 192.168.95.15")
    fig0.savefig("Holding-15.png")
    plt.show()
    
holding_10()
holding_11()
holding_12()
holding_13()
holding_14()
holding_15()
