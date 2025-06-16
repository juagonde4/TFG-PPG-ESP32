import matplotlib.pyplot as plt

# Lista real de BPM
bpm_values = [
    72, 69, 67, 68, 68, 70, 71, 75, 78, 77, 76, 70, 67, 68, 70, 71, 72, 72, 72, 76, 77, 77, 76, 71,
    69, 70, 69, 62, 61, 66, 70, 69, 70, 67, 64, 65, 66, 67, 65, 64, 65, 67, 68, 73, 70, 67, 66, 63,
    64, 66, 68, 70, 70, 70, 66, 62, 63, 63, 65, 67, 66, 66, 66, 65, 64, 62, 61, 59, 59, 59, 61, 64,
    65, 69, 73, 71, 70, 67, 60, 58, 58, 59, 62, 65, 68, 70, 73, 73, 69, 70, 66, 66, 68, 65, 65, 66,
    81, 79, 89, 84, 75, 102, 91, 91, 83, 57, 68, 69, 87, 88, 92, 109, 105, 117, 104, 106, 110, 112,
    129, 123, 123, 125, 124, 129, 126, 125, 124, 121, 120, 119, 120, 119, 124, 128, 128, 130, 121,
    117, 115, 115, 119, 119, 117, 116, 115, 113, 113, 112, 110, 108, 105, 104, 104, 108, 112, 113,
    110, 109, 109, 107, 110, 108, 106, 112, 114, 109, 104, 93, 85, 87, 90, 95, 100, 96, 99, 97, 95,
    96, 90, 86, 81, 77, 73, 71, 71, 72, 75, 75, 80, 80, 79, 85, 81, 79, 76, 69, 67, 70, 73, 73
]

# Colores según niveles de estrés
colors = []
for bpm in bpm_values:
    if bpm < 80:
        colors.append('blue')      # Estrés nulo
    elif 80 <= bpm < 100:
        colors.append('green')     # Estrés bajo
    elif 100 <= bpm <= 140:
        colors.append('orange')    # Estrés moderado
    else:
        colors.append('red')       # Estrés alto

# Crear gráfico
plt.figure(figsize=(14, 6))
plt.scatter(range(len(bpm_values)), bpm_values, c=colors, s=40, edgecolors='black')

# Líneas horizontales para los umbrales
plt.axhline(60, color='blue', linestyle='--', label='Límite estrés nulo/bajo (60 BPM)')
plt.axhline(100, color='green', linestyle='--', label='Límite estrés bajo/moderado (100 BPM)')
plt.axhline(140, color='red', linestyle='--', label='Límite estrés moderado/alto (140 BPM)')

plt.title('Niveles de Estrés Basados en BPM')
plt.xlabel('Muestra')
plt.ylabel('BPM')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()