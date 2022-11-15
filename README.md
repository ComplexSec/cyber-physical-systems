# Cyber Physical Systems Security

This repo contains source code for analyzing and gathering data from different Modbus devices in an ICS network.

## gather-register-data.py

This code gathers 100 samples from the first 10 holding registers of Modbus devices in an ICS network and outputs them to a CSV file for further analysis. It also utilizes multithreading to run each function simultaneously, eliminating time discrepancies in the analysis between the varying CSV files.

## graph-plot.py
