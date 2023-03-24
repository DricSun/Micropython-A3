from machine import Pin , I2C
import utime

from lcd_api import LcdApi , 
from pico_i2c_lcd import I2cLcd
#
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)



 
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
        lcd.backlight_on()
        lcd.putstr("bleu")
        lcd.move_to(3,1)
        #lcd.putstr("freva.com")
        play_tone(440, 0.5)
        utime.sleep(0.1)
        led.off()
        lcd.clear()
    elif key == "b":
        led2.toggle()
        lcd.backlight_on()
        lcd.putstr("vert")
        lcd.move_to(3,1)
        play_tone(150, 0.5)
        utime.sleep(0.1)
        led2.off()
        lcd.clear()
    elif key == "c":
        led3.toggle()
        lcd.backlight_on()
        lcd.putstr("blanc")
        lcd.move_to(3,1)
        play_tone(180, 0.5)
        utime.sleep(0.1)
        led3.off()
        lcd.clear()
    elif key == "d":
        led4.toggle()
        lcd.backlight_on()
        lcd.putstr("rouge")
        lcd.move_to(3,1)
        play_tone(250, 0.5)
        utime.sleep(0.1)
        led4.off()
        lcd.clear()
    