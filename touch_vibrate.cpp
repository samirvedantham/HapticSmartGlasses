#include <Adafruit_DRV2605.h>
#include <Wire.h>

Adafruit_DRV2605 drv;

int ledPin = 13;
int sensorValue = 0;
int sensorPin = A0;
  
void setup() {
  Serial.begin(9600);
  Serial.println("DRV test");
  drv.begin();
  Serial.println("finished drv.begin()");
  
  drv.selectLibrary(1);
  Serial.println("finished drv.selectLibrary()");
  
  // I2C trigger by sending 'go' command 
  // default, internal trigger when sending GO command
  drv.setMode(DRV2605_MODE_INTTRIG);
  Serial.println("finished drv.setMode()");
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println("finished pinMode()");
  
  
}

uint8_t effect = 1;

void loop() {
  Serial.print("Effect #"); Serial.println(effect);

//  delay(1000);
  sensorValue = analogRead(sensorPin);
  Serial.print("sensoralue: ");
  Serial.println(sensorValue);

  if (sensorValue > 1000) {
    digitalWrite(LED_BUILTIN, HIGH);
    
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(1000);

  
  
  // set the effect to play
//  drv.useERM();
//  drv.setWaveform(0, effect);  // play effect 
//  drv.setWaveform(1, 0);       // end waveform
//
//  // play the effect!
//  drv.go();
//
//  // wait a bit
//  delay(500);

  effect++;
  if (effect > 117) effect = 1;
}
