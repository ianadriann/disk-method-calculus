import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


"""
sebuah kurva yang didefinisikan oleh fungsi y=f(x) pada interval [a,b]. Jika kita memutar kurva ini mengelilingi sumbu x
"""

# Definisikan fungsi y = f(x)
def f(x):
    return np.sin(x)  # Misalnya, kita gunakan fungsi sin(x)

# Interval [a, b]
a, b = 0, np.pi

# Buat grid untuk x dan θ (untuk rotasi)
x = np.linspace(a, b, 100)
theta = np.linspace(0, 2 * np.pi, 100)

# Buat meshgrid untuk rotasi
X, Theta = np.meshgrid(x, theta)

# Tentukan koordinat y dan z setelah rotasi
Y = f(X) * np.cos(Theta)
Z = f(X) * np.sin(Theta)

# Buat plot
fig = plt.figure(figsize=(14, 6))

# Plot 3D
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, color='cyan', alpha=0.6, rstride=10, cstride=10)
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.set_zlabel('Z-axis')
ax1.set_title('Volume Benda Putar Mengelilingi Sumbu X (3D)')

# Plot 2D (samping)
ax2 = fig.add_subplot(122)
ax2.plot(x, f(x), 'b', label=r'$y = f(x)$')
ax2.plot(x, -f(x), 'r--', label=r'$y = -f(x)$')
ax2.fill_between(x, f(x), -f(x), color='cyan', alpha=0.3)
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.set_title('Volume Benda Putar Dilihat dari Samping (2D)')
ax2.axhline(0, color='black', linewidth=0.5)
ax2.legend()

plt.show()

