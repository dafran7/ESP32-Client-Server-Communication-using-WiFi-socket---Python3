#include <WiFi.h>
#include <ESPAsyncWebServer.h>
 
const char* ssid = "RedmiQ";
const char* password =  "daffa347";

AsyncWebServer server(80);
AsyncWebSocket ws("/ws");

const uint16_t port = 8090;
const char * host = "192.168.43.240";

void onWsEvent(AsyncWebSocket * server, AsyncWebSocketClient * client, AwsEventType type, void * arg, uint8_t *data, size_t len){
 
  if(type == WS_EVT_CONNECT){
 
    Serial.println("Websocket client connection received");
 
  } else if(type == WS_EVT_DISCONNECT){
    Serial.println("Client disconnected");
 
  } else if(type == WS_EVT_DATA){
 
    Serial.println("Data received: ");
 
    for(int i=0; i < len; i++) {
          Serial.print((char) data[i]);
    }
 
    Serial.println();
  }
}

void setup()
{
 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());

  ws.onEvent(onWsEvent);
  server.addHandler(&ws);

  server.begin();
}
float send_data[3] = {10, 1, 10};

void loop()
{
    
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 
    Serial.println("Connected to server successful!");
 
    //client.print(String("Hello! x = [") + x[0] + ", " + x[1] + "]");
    client.print(String(send_data[0]));
    delay(500);
    client.print(String(send_data[1]));
    delay(500);
    client.print(String(send_data[2]));
    delay(500);
 
    Serial.println("Disconnecting...");
    client.stop();
 
    delay(10000);
}
