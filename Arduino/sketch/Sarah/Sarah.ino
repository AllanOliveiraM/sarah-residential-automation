#include <SPI.h>
#include <MFRC522.h>
#include <Ultrasonic.h>

#define SS_PIN 10
#define RST_PIN 9


MFRC522 rfid(SS_PIN, RST_PIN);

const int ultrasonicTrigPin = 5;
const int ultrasonicEchoPin = 6;
Ultrasonic ultrasonic(ultrasonicTrigPin, ultrasonicEchoPin);
int distanciaUltrasonic;
int controlUltrasonic;

const int pinoFalante = 4;
int frequenciaSom = 3000;
int tempoSom = 100;

const int pinReleOne = 2;
const int pinReleTwo = 3;

int readSerial = 0;

int serverOnline = 0;

int loopController = 0;

void bip() {
  tone(pinoFalante, frequenciaSom, tempoSom);
  delay(90);
}

void bipTwo() {
  tone(pinoFalante, frequenciaSom, tempoSom);
  delay(90);
}

void startUltrasonic() {
  digitalWrite(ultrasonicTrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonicTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonicTrigPin, LOW);
  distanciaUltrasonic = (ultrasonic.Ranging(CM));
}

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();


  pinMode(pinReleOne, OUTPUT);
  pinMode(pinReleTwo, OUTPUT);
  pinMode(pinoFalante, OUTPUT);

  pinMode(ultrasonicTrigPin, OUTPUT);
  pinMode(ultrasonicEchoPin, INPUT);

  digitalWrite(pinReleOne, HIGH);
  digitalWrite(pinReleTwo, HIGH);

  Serial.println("SERVER");

}

void loop() {

  startUltrasonic();
  delay(50);
  if (controlUltrasonic < distanciaUltrasonic - 20 || controlUltrasonic > distanciaUltrasonic + 20) {
    if (distanciaUltrasonic < 50) {
      Serial.println("US-INF");
      controlUltrasonic = distanciaUltrasonic;
    } else {
      Serial.println("US-SUP");
      controlUltrasonic = distanciaUltrasonic;
    }
  }
  delay(50);




  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;
  String strID = "";
  for (byte i = 0; i < 4; i++) {
    strID +=
      (rfid.uid.uidByte[i] < 0x10 ? "0" : "") +
      String(rfid.uid.uidByte[i], HEX) +
      (i != 3 ? ":" : "");
  }
  strID.toUpperCase();
  Serial.println(strID);
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
  bip();
  if (serverOnline == 0) {
    if (strID == "A5:A9:9C:73" || strID == "D0:E5:6D:C1" || strID == "5A:2C:77:89") {
      delay(100);
      bipTwo();
      digitalWrite(pinReleOne, LOW);
      delay(400);
      digitalWrite(pinReleOne, HIGH);
    }
  }
}
