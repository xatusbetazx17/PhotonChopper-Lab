/* FizeauLogger.ino
 * Logs rotor RPM (from a tach sensor) and photodiode intensity to Serial CSV.
 * Also allows marking "extinction" events with a pushbutton.
 * (c) 2025 PhotonChopper-Lab — MIT
 */

// ---- User settings ----
#define N_GAPS 300            // number of gaps in your rotor
#define PULSES_PER_REV N_GAPS // pulses per revolution from your tach sensor
#define TACH_PIN 2            // interrupt pin (D2 on Uno/Nano)
#define PHOTO_PIN A0          // analog photodiode input
#define BUTTON_PIN 4          // active LOW (to GND), uses INPUT_PULLUP
#define LED_PIN 13            // blinks on mark
#define SAMPLE_MS 200         // RPM update interval
#define BAUD 115200

volatile unsigned long pulse_count = 0;
unsigned long last_ms = 0;

void IRAM_ATTR tachISR(){
  pulse_count++;
}

void setup(){
  pinMode(TACH_PIN, INPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(TACH_PIN), tachISR, RISING);
  Serial.begin(BAUD);
  delay(200);
  Serial.println("time_ms,rpm,photo,mark");
}

void loop(){
  unsigned long now = millis();
  if (now - last_ms >= SAMPLE_MS){
    noInterrupts();
    unsigned long count = pulse_count;
    pulse_count = 0;
    interrupts();

    // pulses in window -> RPM
    float revs = (float)count / (float)PULSES_PER_REV;
    float rpm = (revs * 60000.0) / (float)(now - last_ms);

    int photo = analogRead(PHOTO_PIN);
    int mark = (digitalRead(BUTTON_PIN) == LOW) ? 1 : 0;

    if (mark){
      digitalWrite(LED_PIN, HIGH);
    } else {
      digitalWrite(LED_PIN, LOW);
    }

    Serial.print(now);
    Serial.print(",");
    Serial.print(rpm, 2);
    Serial.print(",");
    Serial.print(photo);
    Serial.print(",");
    Serial.println(mark);

    last_ms = now;
  }
}
