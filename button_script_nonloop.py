#Button function
import RPi.GPIO as GPIO #må importeres i hovedfilen

def button(pin_number):
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    while True: # Run forever
        if GPIO.input(pin_number) == GPIO.HIGH:
            return True


#Her velger man knapp utifra hvilken pin den er koblet til (pin_number)
