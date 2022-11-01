import time
import pigpio

_MAX: int = 100_0000
_MIN: int = 0
#_FREQUENCY = 100_000

class PELTIER():
    def __init__(self, pi, GPIOpeltier_in1: int, GPIOpeltier_in2: int) -> None:
        self._GPIOpeltier_in1: int = GPIOpeltier_in1
        self._GPIOpeltier_in2: int = GPIOpeltier_in2
        self._pigpio = pi
        self.state = ''

    def SetToCooling(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MAX, _MAX)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)
        self.state = 'COLD'
        return self.state

    def SetToHeating(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MAX, _MAX)
        self.state = 'HOT'
        return self.state
        
    def TurnOff(self):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, _MIN, _MIN)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, _MIN, _MIN)
        self.state = 'OFF'
        return self.state

    def SetTemperature(self, In1DutyCycle: int, In1Frequency: int, In2DutyCycle: int, In2Frequency: int):
        self._pigpio.hardware_PWM(self._GPIOpeltier_in1, In1Frequency, In1DutyCycle)
        self._pigpio.hardware_PWM(self._GPIOpeltier_in2, In2Frequency, In2DutyCycle)
        self.state = "Custom Value"
        return self.state    



if __name__ == "__main__":
    
    
    Peltier1 = PELTIER(pi = pigpio.pi(), GPIOpeltier_in1 = 13, GPIOpeltier_in2 = 12)
    
    print("full Cool/Heat test")
    x = Peltier1.SetToCooling()
    print(x)
    time.sleep(2)
    x = Peltier1.SetToHeating()
    print(x) 
    time.sleep(2)
    
    print("SetTemperature 1 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 450_000, In1Frequency = 100_000, In2DutyCycle = _MIN, In2Frequency = _MIN) 
    print(x)
    
    print("SetTemperature 2 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 700_000, In1Frequency = 100_000, In2DutyCycle = _MIN, In2Frequency = _MIN) 
    print(x)
    
    print("SetTemperature 3 Test")
    time.sleep(1)
    x = Peltier1.SetTemperature(In1DutyCycle = 200_000, In1Frequency = 100_000, In2DutyCycle = _MIN, In2Frequency = _MIN) 
    print(x)
    
    print("Turn Off Test")
    time.sleep(1)
    x = Peltier1.TurnOff()
    print(x) 
    time.sleep(3)

    print("Sweep test HOT")
    time.sleep(1)
    for x in range(_MIN, _MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetTemperature(In1DutyCycle = _MIN, In1Frequency = _MIN, In2DutyCycle = x, In2Frequency = 100_000)

    print("Sweep test COLD") # assuming in2 is the hot side
    for x in range(_MIN, _MAX, 100): # steps of 100
        #time.sleep(0.1)
        print(x)
        x = Peltier1.SetTemperature(In1DutyCycle = x, In1Frequency = 100_000, In2DutyCycle = _MIN, In2Frequency = _MIN)

    x = Peltier1.TurnOff()
    print(x)
    print("test complete")
        