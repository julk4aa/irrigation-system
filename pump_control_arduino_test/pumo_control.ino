#define pump 32
#define led 2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(pump, OUTPUT);
  pinMode(led, OUTPUT);
  digitalWrite(pump, LOW);
  digitalWrite(led, LOW);
  Serial.println("setup ok");
}

void pump_on() {
  digitalWrite(pump, HIGH);
  digitalWrite(led, HIGH);
  Serial.println("pompa dziala");
}

void pump_off() {
  digitalWrite(pump, LOW);
  digitalWrite(led, LOW);
  Serial.println("pompa stop");
}

void loop() {
  //put your main code here, to run repeatedly:
  pump_on();
  delay(10000);

  pump_off();
  delay(10000);
}
