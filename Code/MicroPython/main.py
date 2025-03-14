from machine import Pin, PWM, time_pulse_us
from utime import sleep
    
class Servo:
    def __init__(self, pin):
        self.pin = Pin(pin,Pin.OUT)
        self.frequency = 50
        self.minPulseMs = .5
        self.maxPulseMs = 2.5
        self.range = 180
    
    def Start(self):
        self.pwm = PWM(self.pin)
        self.pwm.freq(self.frequency)
    
    def SetPositionPercent(self, percent):
        dutyPercentRangeMs = self.maxPulseMs - self.minPulseMs;
        newDutyMs = self.minPulseMs + ( dutyPercentRangeMs/100 * percent )
        self.pwm.duty_ns(round(newDutyMs * 1000000))
                
    def SetPosition(self,newPos):
        newCyclePercent = (newPos / self.range) * 100
        self.SetPositionPercent(newCyclePercent)
            
    def Stop(self):
        self.pwm.deinit()

class PWMReader:
    def __init__(self, pin, frequency):
        self.pin = Pin(pin,mode=Pin.IN,pull=Pin.PULL_DOWN )
        self.frequencyHZ = frequency
        self.cycleWidthUS = round(1000000/frequency)
        
    def GetPulseWidth(self):
        machine.time_pulse_us(self.pin, 1, self.cycleWidthUS*5)
        return machine.time_pulse_us(self.pin, 1
                                     , self.cycleWidthUS*5)

    def GetDutyCycle(self):
        pulseWidth = self.GetPulseWidth()
        if pulseWidth == -2:
            dutyCycle = 0
        elif pulseWidth == -1:
            dutyCycle = 100
        else:
            dutyCycle=pulseWidth/self.cycleWidthUS * 100
        
        print(dutyCycle, pulseWidth)
        return dutyCycle
        

# Setup PWM Pin for servo control
servo = Servo(0)
pwmReader = PWMReader(15, 50)

servo.Start()
servoPositions = [0,50,100]
try:
        while True:
            for position in servoPositions:
                servo.SetPositionPercent(position)
                dutyCycle = pwmReader.GetDutyCycle()               
                sleep(2)
                #sleep(1)
            
except KeyboardInterrupt:
    print("Keyboard interrupt")
    #Turn off PWM
    servo.Stop()
    
