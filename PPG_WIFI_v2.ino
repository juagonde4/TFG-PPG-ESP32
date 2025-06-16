#include <WiFi.h>
#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

const char* ssid = "Livebox6-A2E3";
const char* password = "GoXrhT4R6TF6";

WiFiServer server(80);

MAX30105 particleSensor;
const byte RATE_SIZE = 4;
byte rates[RATE_SIZE];
byte rateSpot = 0;
long lastBeat = 0;
float beatsPerMinute;
int beatAvg;
String lastMessage = "Esperando datos válidos...";

// Buffer para almacenar las últimas 50 lecturas
const int BUFFER_SIZE = 200;
int bpmBuffer[BUFFER_SIZE];
int bufferIndex = 0;

int sampleCount = 0;
String rawBPMData = "";
String filteredBPMData = "";


void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }

  Serial.println("Conectado a WiFi!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  server.begin();

  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30105 no detectado. Verifica conexiones.");
    while (1);
  }

  particleSensor.setup();
  particleSensor.setPulseAmplitudeRed(0x0A);
  particleSensor.setPulseAmplitudeGreen(0);
}

void loop() {
  long irValue = particleSensor.getIR();

  if (irValue > 50000) {
    if (checkForBeat(irValue)) {
      long delta = millis() - lastBeat;
      lastBeat = millis();
      beatsPerMinute = 60 / (delta / 1000.0);

       // Guardar el valor crudo en la cadena
      rawBPMData += String(beatsPerMinute) + ", ";

      if (beatsPerMinute < 255 && beatsPerMinute > 50) {
        filteredBPMData += String(beatsPerMinute) + ", ";

        rates[rateSpot++] = (byte)beatsPerMinute;
        rateSpot %= RATE_SIZE;

        beatAvg = 0;
        for (byte x = 0; x < RATE_SIZE; x++) beatAvg += rates[x];
        beatAvg /= RATE_SIZE;

        if (beatAvg >= 55) {
          bpmBuffer[bufferIndex++] = beatAvg;
          if (bufferIndex >= BUFFER_SIZE) bufferIndex = 0;
        }

        if (beatAvg >= 85 && beatAvg < 100) {
          lastMessage = "Tus pulsaciones están empezando a subir, es posible que tengas estrés.";
        } else if (beatAvg >= 100 && beatAvg <= 150) {
          lastMessage = "Cuidado, tus pulsaciones han subido mucho. Alta probabilidad de estrés alto.";
        } else if (beatAvg > 150) {
          lastMessage = "¡Peligro! Necesita relajarse.";
        } else if (beatAvg >= 55 && beatAvg < 85) {
          lastMessage = "Pulsaciones normales.";
        } else {
           lastMessage = "Esperando datos válidos.";
          }
      }
      // Imprimir cada 20 muestras
      sampleCount++;
      if (sampleCount >= 20) {
        Serial.println("=== Raw BPM Data ===");
        Serial.println(rawBPMData);
        Serial.println("=== Filtered BPM Data ===");
        Serial.println(filteredBPMData);
        Serial.println("====================");
        
        // Reiniciar conteo
        rawBPMData = "";
        filteredBPMData = "";
        sampleCount = 0;
      }
    }
  }

  // Imprimir el buffer cada 10 segundos
  static unsigned long lastPrintTime = 0;
  if (millis() - lastPrintTime > 10000) {
    lastPrintTime = millis();
    Serial.println("=== BPM Data ===");
    for (int i = 0; i < BUFFER_SIZE; i++) {
      Serial.print(bpmBuffer[i]);
      if (i < BUFFER_SIZE - 1) Serial.print(", ");
    }
    Serial.println("\n================");
  }

  WiFiClient client = server.available();
  if (client) {
    Serial.println("Cliente conectado");
    String request = client.readStringUntil('\r');
    client.read(); // Consume '\n'

    if (request.indexOf("GET /bpm") >= 0) {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/plain");
      client.println("Connection: close");
      client.println();
      client.println("BPM: " + String(beatAvg) + "\n" + lastMessage);
    } else {
      // Página HTML con JavaScript que se actualiza automáticamente
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/html");
      client.println("Connection: close");
      client.println();

client.println();
client.println(R"rawliteral(
<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8'>
  <title>Monitor de Estrés</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    h1 {
      color: #333;
    }
    #bpm {
      background: white;
      padding: 20px 40px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      font-size: 24px;
      color: #222;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Monitor de Estrés</h1>
  <div id='bpm'>Esperando datos...</div>
  <script>
    setInterval(() => {
      fetch('/bpm')
        .then(res => res.text())
        .then(data => {
          document.getElementById('bpm').innerText = data;
        });
    }, 2000);
  </script>
</body>
</html>
)rawliteral");
    }
    delay(1);
    client.stop();
    Serial.println("Cliente desconectado");
  }
}
