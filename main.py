import RPi.GPIO as GPIO
import time
import picamera

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)

# Set up the relay
relay_pin = 21
GPIO.setup(relay_pin, GPIO.OUT)

# Set up the camera
camera = picamera.PiCamera()

try:
    # Wait for the camera to initialize
    time.sleep(2)

    # Take a picture
    camera.capture('/home/pi/Desktop/image.jpg')
    print('Image captured')

    # Activate the relay
    GPIO.output(relay_pin, GPIO.HIGH)
    print('Relay activated')

    # Wait for 5 seconds
    time.sleep(5)

    # Deactivate the relay
    GPIO.output(relay_pin, GPIO.LOW)
    print('Relay deactivated')

finally:
    # Clean up the GPIO pins
    GPIO.cleanup()

    # Release the camera resources
    camera.close()