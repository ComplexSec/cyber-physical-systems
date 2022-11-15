# Cyber Physical Systems Security

This repo contains source code for analyzing and gathering data from different Modbus devices in an ICS network.

## gather-register-data.py

This code gathers 100 samples from the first 10 holding registers of Modbus devices in an ICS network and outputs them to a CSV file for further analysis. It also utilizes multithreading to run each function simultaneously, eliminating time discrepancies in the analysis between the varying CSV files.

## graph-plot.py

This code reads CSV files that contain data from scraping Holding Registers of Modbus devices in an ICS network. It plots these values into a graph
in order to visualize the values increasing or decreasing in real-time. These graphs are also saved locally into a PNG format for offline analysis.

[![Test](https://github.com/ComplexSec/cyber-physical-systems/blob/main/images/Holding-10.png)](https://github.com/ComplexSec/cyber-physical-systems/blob/main/images/Holding-10.png)
