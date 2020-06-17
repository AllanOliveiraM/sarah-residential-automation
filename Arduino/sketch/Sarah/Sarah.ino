#include <SPI.h>
#include <MFRC522.h>


#define SS_PIN 10
#define RST_PIN 9


MFRC522 rfid(SS_PIN, RST_PIN);


int pinReleOne = 2;
int pinReleTwo = 3;

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();


  pinMode(pinReleOne, OUTPUT);
  pinMode(pinReleTwo, OUTPUT);
  digitalWrite(pinReleOne, HIGH);
  digitalWrite(pinReleTwo, HIGH);
}

void loop() {

  int readSerial = 0;
  if (Serial.available() > 0) {
    readSerial = Serial.read();
    if (readSerial == 97) {           // a
      Serial.println("RELE-1-ON");
      digitalWrite(pinReleOne, LOW);
    } else if (readSerial == 98) {    // b
      Serial.println("RELE-1-OFF");
      digitalWrite(pinReleOne, HIGH);
    } else if (readSerial == 99) {    // c
      Serial.println("RELE-2-ON");
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
  }
}
