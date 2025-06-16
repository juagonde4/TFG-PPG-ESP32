import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Datos del proyecto
actividades = [
    ("Estudio preliminar sobre fotopletismografía", "14/04/2025", "21/04/2025"),
    ("Adquisición e instalación de hardware", "22/04/2025", "23/04/2025"),
    ("Programación inicial en Arduino", "24/04/2025", "30/04/2025"),
    ("Detección de estrés a partir de BPM", "01/05/2025", "03/05/2025"),
    ("Migración del sistema a ESP32", "04/05/2025", "07/05/2025"),
    ("Conexión Wifi en ESP32", "08/05/2025", "09/05/2025"),
    ("Implementación de servidor web", "10/05/2025", "12/05/2025"),
    ("Validación y depuración del sistema", "13/05/2025", "16/05/2025"),
    ("Documentación técnica", "17/05/2025", "23/05/2025"),
    ("Preparación de presentación y defensa", "24/05/2025", "27/05/2025")
]

# Convertimos fechas a objetos datetime
fechas_inicio = [datetime.strptime(i[1], "%d/%m/%Y") for i in actividades]
fechas_fin = [datetime.strptime(i[2], "%d/%m/%Y") for i in actividades]

# Cálculo de duración para cada tarea
duraciones = [(fin - ini).days for ini, fin in zip(fechas_inicio, fechas_fin)]

# Preparar la figura
fig, ax = plt.subplots(figsize=(12, 6))

# Crear barras horizontales
for i, (nombre, ini, dur) in enumerate(zip(actividades, fechas_inicio, duraciones)):
    ax.barh(i, dur, left=ini, height=0.4, align='center', color='skyblue', edgecolor='black')

# Configuraciones del eje
ax.set_yticks(range(len(actividades)))
ax.set_yticklabels([act[0] for act in actividades])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.xticks(rotation=45)
plt.title("Diagrama de Gantt - Proyecto de Medición de Estrés")
plt.xlabel("Fecha")
plt.tight_layout()

# Mostrar el gráfico
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.show()