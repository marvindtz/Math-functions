import numpy as np
import matplotlib.pyplot as plt

# Bildgröße
size = 63
radius = size // 2
center = (radius, radius)

# Erstelle ein leeres RGB-Bild
image = np.zeros((size, size, 3), dtype=np.uint8)

# Zeichne den Kreisrand
y, x = np.ogrid[:size, :size]
dist = np.sqrt((x - center[0])**2 + (y - center[1])**2)
circle = np.abs(dist - radius) < 0.5
image[circle] = [200, 200, 200]  # grauer Rand

# Zeichne 64 Linien für die Sektoren
for i in range(64):
    angle = 2 * np.pi * i / 64
    end_x = int(center[0] + radius * np.cos(angle))
    end_y = int(center[1] + radius * np.sin(angle))

    # Bresenham-Linie oder einfache Interpolation
    num_points = 100
    x_vals = np.linspace(center[0], end_x, num_points).astype(int)
    y_vals = np.linspace(center[1], end_y, num_points).astype(int)

    # Begrenzung auf das Bild
    for x_p, y_p in zip(x_vals, y_vals):
        if 0 <= x_p < size and 0 <= y_p < size:
            image[y_p, x_p] = [255, 0, 0]  # rot

# Bild anzeigen
plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.axis("off")
plt.title("63x63 Kreis in 64 Sektoren")
plt.show()