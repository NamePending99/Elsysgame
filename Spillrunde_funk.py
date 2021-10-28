from random import randint
from gpiozero import Button
from signal import pause

# I koden antar vi at vi har en dictionary over lister med dagens ord fra forskjellige episoder i nytt på nytt. på formen: main_word_dict = {1 : [ord 1, ord 2, ord 3], 2: [ord 1, ord 2, ord 3], 3: ...}
# Vi antar også at vi har en definert meny funksjon
# Vi antar at vi har en fungerende programleder_ordvalg funksjon
 
p1_button = Button(a) #her definerer man knappene for programlederen, a og b må henholdsvis at pin nummer
p2_button = Button(b)


main_word_dict = {1:["ord 1", "ord 2", "ord 3"]} #dummy variabler
def meny(liste):
    print("valg utført") #dummy variabler

def programleder_ordvalg(): #Hjelpefunksjon
    if p1_button.when_pressed():
        return "p1"
    if p2_button.when_pressed():
        return "p2"
    return vinner_valg

def update_score(string): #Hjelpefunksjon
    if string == "p1":
        player_score[0] += 1
    if string == "p2":
        player_score[1] += 1

def spillrunde(antall_runder): #Hovedfunksjon

    player_score = [0,0] #scoren til spiller 1 og 2 henholdsvis for gjeldende runde
    
    for i in range(antall_runder):

        random_tall = random.randint(1, len(main_word_dict)) #lager et tall mellom 0 til antall_ordlister vi har 
        ordliste = main_word_dict[random_tall] #velger ut EN liste med ord fra alle mulige

        p1_valg = meny(ordliste)
        p2_valg = meny(ordliste) #valg av ord for henholdsvis spille

        score = programleder_ordvalg() #her returneres enten "p1" eller "p2" som strings
        
        update_score(score)

    return player_score
