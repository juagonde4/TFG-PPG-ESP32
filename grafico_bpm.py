import matplotlib.pyplot as plt

# Datos proporcionados
bpm_data = [72, 69, 67, 68, 68, 70, 71, 75, 78, 77, 76, 70, 67, 68, 70, 71, 72, 72, 72, 76, 77, 77, 76, 71, 69, 70, 69, 62, 61, 66, 70, 69, 70, 67, 64, 65, 66, 67, 65, 64, 65, 67, 68, 73, 70, 67, 66, 63, 64, 66, 68, 70, 70, 70, 66, 62, 63, 63, 65, 67, 66, 66, 66, 65, 64, 62, 61, 59, 59, 59, 61, 64, 65, 69, 73, 71, 70, 67, 60, 58, 58, 59, 62, 65, 68, 70, 73, 73, 69, 70, 66, 66, 68, 65, 65, 66, 81, 79, 89, 84, 75, 102, 91, 91, 83, 57, 68, 69, 87, 88, 92, 109, 105, 117, 104, 106, 110, 112, 129, 123, 123, 125, 124, 129, 126, 125, 124, 121, 120, 119, 120, 119, 124, 128, 128, 130, 121, 117, 115, 115, 119, 119, 117, 116, 115, 113, 113, 112, 110, 108, 105, 104, 104, 108, 112, 113, 110, 109, 109, 107, 110, 108, 106, 112, 114, 109, 104, 93, 85, 87, 90, 95, 100, 96, 99, 97, 95, 96, 90, 86, 81, 77, 73, 71, 71, 72, 75, 75, 80, 80, 79, 85, 81, 79, 76, 69, 67, 70, 73, 73]


# Inicialización de listas
normal = []
moderado = []
alto = []

# Clasificación de los datos
for i, bpm in enumerate(bpm_data):
    if 55 <= bpm < 85:
        normal.append((i, bpm))
    elif 85 <= bpm <= 100:
        moderado.append((i, bpm))
    elif bpm > 100:
        alto.append((i, bpm))

# Generar el gráfico
plt.figure(figsize=(10, 5))
plt.plot(bpm_data, linestyle='-', color='grey', label='BPM Total')

# Dibujar los puntos correctamente
if normal:
    plt.scatter(*zip(*normal), color='green', label='Estrés Bajo (Normal)')
if moderado:
    plt.scatter(*zip(*moderado), color='orange', label='Estrés Moderado')
if alto:
    plt.scatter(*zip(*alto), color='red', label='Estrés Alto')

# Configuración del gráfico
plt.title('Evolución del BPM en el tiempo')
plt.xlabel('Muestras')
plt.ylabel('BPM')
plt.grid(True)
plt.legend()
plt.show()