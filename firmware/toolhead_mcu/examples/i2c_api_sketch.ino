// Minimal pseudo‑sketch for a toolhead MCU I²C API
// MCU: Arduino/Teensy/STM32; wire up to Pi I²C
#include <Wire.h>

#define I2C_ADDR 0x2A
#define CMD_SET_ENABLE 0x01
#define CMD_SET_THROTTLE 0x02
#define CMD_SET_DIR 0x03
#define CMD_SET_CHUTE 0x04
#define CMD_SET_DEFLECT 0x05
#define CMD_GET_STATUS 0x10

volatile bool enabled=false;
volatile int8_t throttle=0;     // -100..100
volatile int8_t direction=1;    // 1 fwd, -1 rev
volatile uint16_t chute_deg=0;  // 0..360
volatile uint8_t deflect_pct=0; // 0..100

void receive(int n){
  if(n<1) return;
  uint8_t cmd = Wire.read();
  switch(cmd){
    case CMD_SET_ENABLE: enabled = Wire.read(); break;
    case CMD_SET_THROTTLE: throttle = (int8_t)Wire.read(); break;
    case CMD_SET_DIR: direction = Wire.read()?1:-1; break;
    case CMD_SET_CHUTE: chute_deg = (Wire.read()<<8) | Wire.read(); break;
    case CMD_SET_DEFLECT: deflect_pct = Wire.read(); break;
  }
}

void request(){
  // Return 8 bytes: type, faults, curr_hi, curr_lo, rpm_hi, rpm_lo, temp, reserved
  uint8_t type = 2; // 1=plow,2=thrower,3=brush (demo)
  uint8_t faults = 0;
  uint16_t curr = 123; // mA demo
  uint16_t rpm  = 2500;
  uint8_t tempC = 30;
  Wire.write(type);
  Wire.write(faults);
  Wire.write((uint8_t)(curr>>8)); Wire.write((uint8_t)(curr&0xFF));
  Wire.write((uint8_t)(rpm>>8));  Wire.write((uint8_t)(rpm&0xFF));
  Wire.write(tempC);
  Wire.write(0);
}

void setup(){
  Wire.begin(I2C_ADDR);
  Wire.onReceive(receive);
  Wire.onRequest(request);
  // init drivers/ESC/servos here
}
void loop(){
  // apply throttle/dir to drivers
  // jam detect & clear
}
