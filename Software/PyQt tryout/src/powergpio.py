import time
import pigpio

_MAX: int = 100_0000
_MIN: int = 350_000
_OFF: int = 0
#_FREQUENCY = 100_000
class PowerGPIO():
    def __init__(self, pi, POWERGPIOpin: int) -> None:
        self._powergpiopin: int = POWERGPIOpin
        self._pigpio = pi
    
    def TurnOn(self):
         self._pigpio.hardware_PWM(self._POWERGPIOpin, _MAX, _MAX)

    def TurnOff(self):
        self._pigpio.hardware_PWM(self._POWERGPIOpin, _MIN, _MIN)

    def SetValue(self, DutyCycle: int, Frequency: int):
        self._pigpio.hardware_PWM(self._POWERGPIOpin, Frequency, DutyCycle)

if __name__ == "__main__":
    
    
    powergpio1 = PWM(pi = pigpio.pi(), GPIOPin = 12)
    print("On/Off test")
    x = powergpio1.TurnOn()
    print(x)
    time.sleep(1)
    x = powergpio1.TurnOff()
    print(x) 
    time.sleep(1)
    x = powergpio1.TurnOn()
    print(x)
    time.sleep(1)
    x = powergpio1.TurnOff()
    print(x) 
    time.sleep(1)

    print("Sweep test")
    for x in range(_MIN, _MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = powergpio1.SetValue(Frequency = 100_000, DutyCycle = x)

    x = powergpio1.TurnOff()
    print(x)
    print("test complete")        