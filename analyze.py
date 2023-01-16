import numpy
import matplotlib.pyplot as plt

import os
import numpy as np
import matplotlib.pyplot as plt

def plot_values(directory):
    sensor_values = {}
    motor_values = {}

    # load all sensor values from the data directory
    for file in os.listdir(directory):
        if file.endswith("SensorValues.npy"):
            sensor_name = file.split("SensorValues.npy")[0]
            sensor_values[sensor_name] = np.load(f"{directory}/{file}")

    # load all motor values from the data directory
    for file in os.listdir(directory):
        if file.endswith("MotorValues.npy"):
            motor_name = file.split("MotorValues.npy")[0]
            motor_values[motor_name] = np.load(f"{directory}/{file}")

    # plot all sensor values
    plt.figure()
    for sensor_name, values in sensor_values.items():
        plt.plot(values, label=sensor_name)
    plt.title("Sensor Values")
    plt.xlabel("Time Steps")
    plt.ylabel("Sensor Value")
    plt.legend()

    # plot all motor values
    plt.figure()
    for motor_name, values in motor_values.items():
        plt.plot(values, label=motor_name)
    plt.title("Motor Values")
    plt.xlabel("Time Steps")
    plt.ylabel("Motor Value")
    plt.legend()
    plt.show()
    
plot_values("data")