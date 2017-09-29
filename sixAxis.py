from approxeng.input.selectbinder import ControllerResource
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

while True:
    try:
        with ControllerResource() as joystick:
            print('Found a joystick and connected')
            p = GPIO.PWM(26,100)
            p.start(0)
            while joystick.connected:
                print("%.2f" % joystick['lx'], "%.2f" % joystick['ly'], "    ", "%.2f" % joystick['rx'], "%.2f" % joystick['ry'])
                p.ChangeDutyCycle(((abs(joystick['ly'])*(-1))+1)*100)
        # Joystick disconnected...
        print('Connection to joystick lost')
    except IOError:
        # No joystick found, wait for a bit before trying again
        print('Unable to find any joysticks')
        sleep(1.0)
