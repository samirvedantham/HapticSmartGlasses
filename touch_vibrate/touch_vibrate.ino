#include <Adafruit_DRV2605.h>
#include <Wire.h>

Adafruit_DRV2605 drv;

// Constants for the pushbutton.
const int TOUCH_BUTTON_PIN = 2;
const int LED_PIN = 13;

// some variables for the state of the button.
int buttonState = 0;

void setup() {
  Serial.begin(9600);
  drv.begin();
  
  drv.selectLibrary(1);
  
  // I2C trigger by sending 'go' command 
  // default, internal trigger when sending GO command
  drv.setMode(DRV2605_MODE_INTTRIG);

  pinMode(TOUCH_BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT); 
}

uint8_t effect = 1;

void loop() {

  buttonState = digitalRead(TOUCH_BUTTON_PIN);

  if (buttonState == HIGH)  {
    drv.setWaveform(0, effect);
    drv.setWaveform(1, 0);
    drv.go();
    effect++;
    Serial.print(effect);
    digitalWrite(LED_PIN, HIGH);
    delay(500);
  } else  {
    digitalWrite(LED_PIN, LOW);
  }
  
//  Serial.print("Effect #"); Serial.println(effect);
//
//  // set the effect to play
//  drv.setWaveform(0, effect);  // play effect 
//  drv.setWaveform(1, 0);       // end waveform
//
//  // play the effect!
//  drv.go();
//
//  // wait a bit
//  delay(500);
//
//  effect++;
//  if (effect > 117) effect = 1;
}
