// NodeMCU_Nokia_5510_Hello_nn
// microprocessor board: Lolin ESP8266 NodeMCU 
// display Nokia 5510
// prints "hello World! to screen
// January 13, 2021
// Floris Wouterlood
// public domain

#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#include <ArduinoJson.h>

#define CLK D4
#define DIN D3
#define DC  D2
#define CE  D1
#define RST D0

Adafruit_PCD8544 display = Adafruit_PCD8544 (CLK,DIN,DC,CE,RST);

//#define LF          0x0A 
//char json[255];
//int idx;

void setup()   {
 
    Serial.begin (9600);
    //Serial.println ("Hello World!");
    //Serial.println ("on NodeMCU ESP8266 and Nokia 5510");
    
    display.begin ();
    display.setContrast (60);                        
    display.clearDisplay ();                     
    display.setRotation (2);  
    display.setTextSize (1);
    display.setTextColor (BLACK);

    display.setCursor (0,0);
    display.println ("Remote Control");
    //display.setCursor (10,20);
    display.println ("connecting...");
    display.display ();       
}


void loop() 
{
    Serial.println ("GET_DATA");
    if (Serial.available() > 0) 
    {     
      
      display.clearDisplay();
      String json = Serial.readStringUntil('\n');
      
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, json);
  
      // {"ID": 3521, "EXP": 0, "VOL_M": 0, "VOL_L": 42, "VOL_R": 42, "APP": "Firefox", "TITLE": "Best Nightcore Songs Mix 2024 \u266b 1 Hour Gaming Mix \u266b Nightcore Mix 2024 - YouTube"}
  
      int ID = doc["ID"];
  
      if (ID == 0)
      {
        display.println ("No data available");
        display.display ();      
        return;
      }
      
      int VOL = doc["VOL"];
      String APP = doc["APP"];
  
      display.println (APP);
      display.println ("VOL:" + String(VOL));
  
      display.display ();      
      delay(1000);

    }    
}
