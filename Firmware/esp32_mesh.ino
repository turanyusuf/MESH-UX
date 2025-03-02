#include "BLEDevice.h"

void setup() {
  Serial.begin(115200);
  BLEDevice::init("MESH UX Beacon");
}

void loop() {
  Serial.println("Mesh Ağı Çalışıyor");
  delay(1000);
}
