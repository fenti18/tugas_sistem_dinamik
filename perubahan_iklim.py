import numpy as np
import matplotlib.pyplot as plt

# Parameter
T0 = 15  # Suhu awal dalam derajat Celcius
C0 = 400  # Konsentrasi CO2 awal dalam ppm
k = 0.01  # Sensitivitas suhu
r = 0.02  # Laju pertumbuhan konsentrasi CO2
t = np.linspace(0, 100, 500)  # Waktu dalam tahun

# Fungsi untuk konsentrasi CO2
C = C0 * np.exp(r * t)

# Fungsi untuk suhu global
T = T0 + k * (C - C0)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, T, label='Suhu Global (T)', color='orange')
plt.title('Model Perubahan Suhu Global akibat Kenaikan CO2')
plt.xlabel('Waktu (tahun)')
plt.ylabel('Suhu (°C)')
plt.grid()
plt.axhline(T0, color='gray', linestyle='--', label='Suhu Awal (15°C)')
plt.legend()
plt.show()