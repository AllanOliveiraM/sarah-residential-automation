#include <SPI.h>
#include <MFRC522.h>


#define SS_PIN 10
#define RST_PIN 9


MFRC522 rfid(SS_PIN, RST_PIN);


const int pinoFalante = 4;
int frequenciaSom = 3000;
int tempoSom = 100;

const int pinReleOne = 2;
const int pinReleTwo = 3;

int readSerial = 0;

int readSerialServer = 0;

bool serverOnline = false;

void bip() {
  tone(pinoFalante, frequenciaSom, tempoSom);
  delay(90);
}

void bipTwo() {
  tone(pinoFalante, frequenciaSom, tempoSom);
  delay(90);
}

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();


  pinMode(pinReleOne, OUTPUT);
  pinMode(pinReleTwo, OUTPUT);
  pinMode(pinoFalante, OUTPUT);
  digitalWrite(pinReleOne, HIGH);
  digitalWrite(pinReleTwo, HIGH);

  Serial.println("SERVER");

}

void loop() {
  if (Serial.available() > 0) {
    readSerial = Serial.read();

    if (readSerial == 84) {
      serverOnline = true;
    } else if (readSerial == 97) {    // a
      Serial.println("RELE-1-ON");
      delay(100);
      bipTwo();
      digitalWrite(pinReleOne, LOW);
    } else if (readSerial == 98) {    // b
      Serial.println("RELE-1-OFF");
      digitalWrite(pinReleOne, HIGH);
    } else if (readSerial == 99) {    // c
      Serial.println("RELE-2-ON");
      delay(100);
      bipTwo();
      digitalWrite(pinReleTwo, LOW);
    } else if (readSerial == 100) {   // d
      Serial.println("RELE-2-OFF");
      digitalWrite(pinReleTwo, HIGH);
    } else {
      Serial.println(readSerial);     // else
    }
  } else {

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
    if (serverOnline == false) {
      if (strID == "A5:A9:9C:73" || strID == "D0:E5:6D:C1" || strID == "5A:2C:77:89") {
        delay(100);
        bipTwo();
        digitalWrite(pinReleOne, LOW);
        delay(400);
        digitalWrite(pinReleOne, HIGH);
      }
    }
  }
}
