#include <Adafruit_DRV2605.h>
#include <Wire.h>

Adafruit_DRV2605 drv;


const int TOUCH_BUTTON_PIN_A = 2;
const int TOUCH_BUTTON_PIN_B = 3;
const int PIN_A = 4;
const int PIN_B = 5;


int buttonStateA = 0;
int buttonStateB = 0;

char blueToothVal;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  drv.begin();
  drv.selectLibrary(1);

  drv.setMode(DRV2605_MODE_EXTTRIGLVL);

  pinMode(TOUCH_BUTTON_PIN_A, INPUT);
  pinMode(TOUCH_BUTTON_PIN_B, INPUT);
  pinMode(PIN_A, OUTPUT);
  pinMode(PIN_B, OUTPUT);
}

uint8_t effect = 52;

void loop() {
  // put your main code here, to run repeatedly:
  buttonStateA = digitalRead(TOUCH_BUTTON_PIN_A);
  buttonStateB = digitalRead(TOUCH_BUTTON_PIN_B);
  

  if (Serial.available()){
    blueToothVal = Serial.read();
  }
  if (blueToothVal == 'B') {
    digitalWrite(PIN_A, HIGH);
    delay(100);
  } else if (blueToothVal == 'R') {
    digitalWrite(PIN_B, HIGH);
    delay(100);

  }
    
  if (buttonStateA == HIGH) {
//    digitalWrite(PIN_A, HIGH);
    delay(100);
    Serial.println("B");

//  }else if(buttonStateA == LOW || blueToothVal == 'y'){
////    Serial.println(F("A is LOW"));
//    digitalWrite(PIN_A, LOW);
//    Serial.println("N");
  }
  else if (buttonStateB == HIGH) {
//    digitalWrite(PIN_B, HIGH);
    delay(100);
    Serial.println("R");

    
  } else{
//    Serial.println(F("B is LOW"));
    digitalWrite(PIN_A, LOW);
    digitalWrite(PIN_B, LOW);
    delay(100);
    Serial.println("N");
  }


//  drv.go();
//  effect++;

//  delay(500);
  
  
}
