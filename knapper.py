from gpiozero import Button

Start_knapp = Button(8)
Spiller1 = Button(2)
Spiller2 = Button(3)

spiller1_neste = Button(4)
spiller1_valg = Button(5)

spiller2_neste = Button(6)
spiller2_valg = Button(7)

if Start_knapp.when_pressed:
    print('Startspillet!')