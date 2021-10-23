#import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library


#def button_callback(channel):
    #return True


#GPIO.setwarnings(False)  # Ignore warning for now
#GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup event on pin 10 rising edge
#GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

#message = input("Press enter to quit\n\n")  # Run until someone presses enter
#GPIO.cleanup()  # Clean up


#if button_callback() == True:
    print('Spillet har startet!')

def button_pushed(knapp):
    if GPIO.input(knapp) == GPIO.HIGH:
        return True
   # else: 
        ##return False

## Start side for spill med innstruks!

def spill_instruks():
    print('Velkommen til Nytt på Nytt mini game show!\n')
    print('\nDette spillet er svært enkelt! Dere må være tre deltagere der en tar programlederrollen og to tar gjesterollen.')
    print('Spørsmålene vil basere seg på "ukens ord", akkurat som i nytt på nytt. Her skal hver av deltagerene sette sammen')
    print('hvert sitt ord. Ordet gjesten har satt sammen må begrunnes og forklares. Når begge gjestene har fokrlart hver sitt ord')
    print('vil det være opptil prograleder om hvem som hadde "rett"! Dette går over 3 runder og, vinneren blir kåret av spillet etter 3 spilte runder!')

    print('For å starte spillet trykk på knappen "start"!')
    while True:
        if button_pushed(start_knapp) == True:
            spill_runde()
            break

def spill_runde():
