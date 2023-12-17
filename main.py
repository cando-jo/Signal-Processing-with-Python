import numpy as np
import matplotlib.pyplot as plt


Fs = 1000  
T = 1/Fs    
t = np.arange(0, 1, T)  


f1 = 50  # Frekans (Hz)
x1 = np.sin(2 * np.pi * f1 * t)


f2 = 150  # Frekans (Hz)
x2 = np.sin(2 * np.pi * f2 * t)


x = x1 + x2


N = len(x)
frequencies = np.fft.fftfreq(N, T)
X = np.fft.fft(x)


X = X / N


plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Zaman Alanında Sinyal')
plt.xlabel('Zaman (s)')
plt.ylabel('Genlik')

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(X))
plt.title('Frekans Alanında Sinyal')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')

plt.tight_layout()  
plt.show()
