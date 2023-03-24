from machine import Pin
import utime
#
# définir la broche de sortie pour le buzzer
buzzer_pin = machine.Pin(16, machine.Pin.OUT)

pinNumber = 14 # declaration d'une variable pinNumber à 17
led = Pin(pinNumber, mode=Pin.OUT)

pinNumber2 = 10 # declaration d'une variable pinNumber à 17
led2 = Pin(pinNumber2, mode=Pin.OUT)

pinNumber3 = 6 # declaration d'une variable pinNumber à 17
led3 = Pin(pinNumber3, mode=Pin.OUT)

pinNumber4 = 2 # declaration d'une variable pinNumber à 17
led4 = Pin(pinNumber4, mode=Pin.OUT)

# créer une fonction pour jouer une note
def play_tone(frequency, duration):
    # calculer la période pour la fréquence donnée
    period = 1.0 / frequency
    # calculer le nombre de cycles complets pour la durée donnée
    cycles = int(duration * frequency)

    for i in range(cycles):
        # activer la broche de sortie pour produire un son
        buzzer_pin.value(1)
        # attendre la moitié de la période
        utime.sleep(period / 2)
        # désactiver la broche de sortie pour produire un silence
        buzzer_pin.value(0)
        # attendre l'autre moitié de la période
        utime.sleep(period / 2)

# boucle principale pour lire les entrées clavier
while True:
    # lire l'entrée clavier
    key = input()
    # jouer une note en fonction de la touche appuyée
    if key == "a":
        led.toggle()
        play_tone(440, 0.5)
        utime.sleep(0.1)
        led.off()
    elif key == "b":
        led2.toggle()
        play_tone(150, 0.5)
        utime.sleep(0.1)
        led2.off()
    elif key == "c":
        led3.toggle()
        play_tone(180, 0.5)
        utime.sleep(0.1)
        led3.off()
    elif key == "d":
        led4.toggle()
        play_tone(250, 0.5)
        utime.sleep(0.1)
        led4.off()
    