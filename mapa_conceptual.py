from graphviz import Digraph

dot = Digraph(comment='Mapa Conceptual - Monitor de Estrés')
dot.attr(rankdir='TB', size='8,10')
dot.attr('node', shape='box', style='filled', fontname='Arial')

# Nodos
dot.node('A', 'Sensor PPG\n(MAX30102)\n↓ Señal IR/Roja', fillcolor='#A2D5F2')
dot.node('B', 'Lectura de señal IR\n(Microcontrolador)\n↓ Valores brutos', fillcolor='#B6E3A5')
dot.node('C', 'Filtrado de señales\n- IR > 50000\n- BPM > 55', fillcolor='#FDFD96')
dot.node('D', 'Cálculo de BPM\n- Detección de latidos\n- Algoritmo HR', fillcolor='#FFB347')
dot.node('E', 'Clasificación de estrés\n- Normal (55–85)\n- Leve(86–100)\n- Elevado (101–150)\n- Crítico (>150)', fillcolor='#FF6961')
dot.node('F', 'Servidor web en ESP32\n- IP local\n- Página HTML', fillcolor='#D6A2E8')
dot.node('G', 'Usuario (PC o móvil)\n- Navegador web\n- Visualiza BPM/Estrés', fillcolor='#C0C0C0')

# Conexiones
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'])

# Guardar
dot.render('mapa_conceptual_monitor_estres', format='png', cleanup=True)
print("Diagrama generado como: mapa_conceptual_monitor_estres.png")