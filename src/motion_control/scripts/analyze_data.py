#! /usr/bin/env python2.7
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

def readDataFromTXT(file_path):
    times = []
    errors = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                try:
                    time, error = float(parts[0]), float(parts[1])
                    times.append(time)
                    errors.append(error)
                except ValueError:
                    print(f"Error converting data: {parts}")
    return times, errors


def plotData(times, errors):
    plt.figure(figsize=(10, 5))
    plt.plot(times, errors, marker="o")
    plt.title("Error over Time")
    plt.xlabel("Time")
    plt.ylabel("Error")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    file_path = (
        "/home/eaibot/motion_control_ws/src/motion_control/data/data_to_analyze.txt"
    )

    times, errors = readDataFromTXT(file_path)
    plotData(times, errors)