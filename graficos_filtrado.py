import matplotlib.pyplot as plt

# Datos BPM
raw_bpm = [93.31, 93.31, 90.50, 1.58, 64.94, 71.09, 74.63, 1.12, 71.09, 76.63,
           4.79, 71.09, 16.23, 66.37, 67.87, 67.87, 66.37, 66.37, 67.87, 66.37]

filtered_bpm = [93.31, 93.31, 90.50, 64.94, 71.09, 74.63, 71.09, 76.63,
                71.09, 66.37, 67.87, 67.87, 66.37, 66.37, 67.87, 66.37]

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(raw_bpm, marker='o', linestyle='--', color='gray', label='Raw BPM Data')
plt.plot(filtered_bpm, marker='o', linestyle='-', color='green', label='Filtered BPM Data')

plt.title('Comparación de BPM sin filtrar y filtrado')
plt.xlabel('Muestras')
plt.ylabel('BPM')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()