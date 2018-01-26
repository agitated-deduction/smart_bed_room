##made 김시라
import RPi.GPIO as GPIO
import time
import smbus2 as smbus

    # Define some constants from the datasheet

 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.

# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

class cds :

    def __init__(self):
        self.bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        #self.DEVICE = 0x23

        
    def convertToNumber(self,data):
        # Simple function to convert 2 bytes of data
        # into a decimal number
        return ((data[1] + (256 * data[0])) / 1.2)


    def readLight(self, addr=0x23):
        data = self.bus.read_i2c_block_data(addr, self.ONE_TIME_HIGH_RES_MODE_1, 2)
        return self.convertToNumber(data)


 


        
## main
#cds_led()




class led :
    led_pin1 = 14
    led_pin2 = 15
    
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.led_pin1, GPIO.OUT)
        GPIO.setup(self.led_pin2, GPIO.OUT)
    
    

    def ledCheck(self, value):
        if value <= 400:
            GPIO.output(self.led_pin1, True)
            GPIO.output(self.led_pin2, True)
        else :
            GPIO.output(self.led_pin1, False)
            GPIO.output(self.led_pin2, False)
    def ledOn(self, on = True):
        GPIO.output(self.led_pin1, on)
        GPIO.output(self.led_pin2, on)

