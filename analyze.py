import numpy
import matplotlib.pyplot as plt

# load the sensor values from the file
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles = numpy.load("data/targetAngles.npy")
targetAngles1 = numpy.load("data/targetAngles1.npy")

# plot the sensor values
# plt.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=2)
# plt.plot(frontLegSensorValues, label="Front Leg Sensor", linewidth = 2)
plt.plot(targetAngles, label="Back Leg Motor Values")
plt.plot(targetAngles1, label="Front Leg Motor Values")
plt.title("Sensor and Target Angles Plot")
plt.xlabel("Time Steps")
plt.ylabel("Sensor and Target Angles Values")
plt.legend()
plt.show()