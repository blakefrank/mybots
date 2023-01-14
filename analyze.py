import numpy
import matplotlib.pyplot as plt

# load the sensor values from the file
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

# plot the sensor values
plt.plot(backLegSensorValues, label="Back Leg Sensor", linewidth=2)
plt.plot(frontLegSensorValues, label="Front Leg Sensor")
plt.legend()
plt.show()