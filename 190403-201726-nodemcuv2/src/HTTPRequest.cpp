#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFiMulti.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>
#ifndef STASSID
#define STASSID "ULSA ITIT"
#define STAPSK  "Cosco123"
#endif

ESP8266WiFiMulti WiFiMulti;
const char* ssid = STASSID;
const char* password = STAPSK;

#define LED D1
void  setup () {
  pinMode(LED, OUTPUT);
  Serial.begin(115200);
  Serial.print("Connecting.");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {

    delay(500);
    Serial.print(".");

  }
  Serial.print(WiFi.localIP());
}

void loop () {
  while (true){
    WiFiClient client;
    HTTPClient http;
    String url = "http://192.168.11.43:8080/vacante/programador";
    String change_state = "http://192.168.11.43:8080/vacante/programador/status";
    if (http.begin(client, url)) {
      int httpCode = http.GET();
      if (httpCode == 200){
        String line = http.getString();
        DynamicJsonDocument doc(1024);
        deserializeJson(doc, line);
        JsonObject json = doc.as<JsonObject>();
        int value = json.getMember("status");
        if (value == 0){
          digitalWrite(LED, LOW);
          delay(100);
        }else{
          digitalWrite(LED, HIGH);
          delay(1000);
          if(http.begin(client, change_state)){
            int httpCode = http.GET();
            if(httpCode == 200){
              Serial.println("Apagado");
            }else{
              Serial.println("No se pudo conecctar");
            }
          };
          http.end();
        }
      }
      http.end();
    }else{
      Serial.println("No se pudo conecctar");
    }
  }
}
