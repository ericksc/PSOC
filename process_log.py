import matplotlib.pyplot as plt
import numpy as np

with open('putty.log') as f:
    data = f.readlines()
    data = [i for i in data if not (i.startswith('=') or i.startswith('COM'))]

on_hex = [i.rstrip() for i in data]
data = [int(i, 16) for i in on_hex]

lenght = len(data)


x = range(len(data[:lenght]))
y = data[:lenght]

plt.stem(x, y, use_line_collection=True)
plt.show()

_data  = np.array(data[:lenght])

new_data = _data - (max(_data)-min(_data)) /2
y = new_data

plt.stem(x, y, use_line_collection=True)
plt.show()

from scipy.fftpack import fft
# Number of sample points
N = lenght
# sample spacing
T = 1.0 / 500.0
x = np.linspace(0.0, N*T, N)
y = y #np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//20)

plt.plot(xf, 2.0/N * np.abs(yf[0:N//20]))
plt.grid()
plt.show()

pass