#include <DHT.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27,16,2); // set the LCD address to 0x27 for a 16 chars and 2 line display
//Constants
const int DHTPIN = A3;     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
//Variables
//int chk;
int h;  //Stores humidity value
int t; //Stores temperature value
const int soil_moisture_sensor = A1;
const int relay_pump = 7;

float soil_moisture_value;
float moisture_percentage;
void setup(){
    Serial.begin(9600);
    Serial.println("Temperature and Humidity Sensor Test");
    dht.begin();
    lcd.init(); //initialize the lcd
    lcd.backlight(); //open the backlight
    pinMode(soil_moisture_sensor, INPUT);
    pinMode(relay_pump, OUTPUT);
    digitalWrite(relay_pump, LOW);
    // lcd.print("Welcome");
}
void loop(){
    //Read data and store it to variables h (humidity) and t (temperature)
    // Reading temperature or humidity takes about 250 milliseconds!
    soil_moisture_value = analogRead(soil_moisture_sensor);
    moisture_percentage = (float)(soil_moisture_value/1023) * 100;
    // soil_moisture_value = (soil_moisture_value / 1023) * 100;
    Serial.print("Moisture raw: ");
    Serial.print(soil_moisture_value);
    Serial.print(" Moisture percent: ");
    Serial.print(moisture_percentage);
  
    h = dht.readHumidity();
    t = dht.readTemperature();
    //Print temp and humidity values to serial monitor
    // > 32 && h < 40 && moisture_percentage < 65)
    if(t > 26 && h > 40 && moisture_percentage > 65){
      digitalWrite(relay_pump, HIGH);
    }
    // else{
    //   digitalWrite(relay_pump, LOW);//32 && h < 40 && moisture_percentage < 65)
    // }
    if(moisture_percentage < 45){
      digitalWrite(relay_pump, LOW);
    }
    
    Serial.print(" Humidity: ");
    Serial.print(h);
    Serial.print(" %, Temp: ");
    Serial.print(t);
    Serial.println(" ° Celsius");
// set the cursor to (0,0):
// print from 0 to 9:
    lcd.setCursor(0, 0);
    lcd.print("MP: ");
    lcd.print(moisture_percentage);
    lcd.print("%");
    lcd.setCursor(0, 1);
    lcd.print(" T:");
    lcd.print(t);
    lcd.print("C");
    lcd.setCursor(11, 1);
    lcd.print("H:");
    lcd.print(h);
    lcd.print("%");
  
  delay(1000); 
}