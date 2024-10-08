#!/usr/bin/env python3
import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import time
import os

# Define the history file and simulation command
history_file = 'history.csv'  # Update with your actual history file name
su2_command = ['SU2_CFD', 'config.cfg']  # Update with your actual config file name

# Start the SU2 simulation process
process = subprocess.Popen(su2_command)

# Set up the initial plot
fig, ax = plt.subplots()
iterations = []
cl_values = []
cd_values = []
cl_line, = ax.plot([], [], label='CL', color='blue')
cd_line, = ax.plot([], [], label='CD', color='red')

# Set axis limits
ax.set_xlim(0, 100)  # Set x-limits according to expected iterations
ax.set_ylim(0, 1.5)  # Adjust y-limits according to expected CL and CD ranges
ax.set_xlabel('Iterations')
ax.set_ylabel('Coefficient Values')
ax.set_title('Real-time CL and CD Update')
ax.legend()

# Function to read the latest CL and CD values
def read_history():
    if os.path.exists(history_file):
        data = pd.read_csv(history_file)
        # Clean up the column names
        data.columns = data.columns.str.replace('"', '', regex=True).str.strip()
        return data['Inner_Iter'].tolist(), data['CL'].tolist(), data['CD'].tolist()
    return [], [], []

# Real-time plotting loop
while process.poll() is None:  # Continue until the process is running
    iterations, cl_values, cd_values = read_history()

    # Update the plot with new data
    if iterations:
        cl_line.set_data(iterations, cl_values)
        cd_line.set_data(iterations, cd_values)

        # Adjust x-limits based on the number of iterations
        ax.set_xlim(0, max(iterations) + 10)  # Extend x-limit for future iterations
        ax.set_ylim(0, max(max(cl_values), max(cd_values)) + 0.5)  # Adjust y-limits based on data

        plt.draw()
        plt.pause(1)  # Pause to allow the plot to update


# Keep the plot open until user closes it
plt.show()  # Show the plot window