from time import sleep     # RasPiO Inspiring scripts
import apa                 # http://rasp.io/inspiring

numleds = 24               # number of LEDs in our display
delay = 0.5                # seconds between frames
brightness = 1            # 0=OFF (224 or 0xE0), 31=FULL (255 or 0xFF)
ledstrip = apa.Apa(numleds)

#ledstrip.reset_leds()

#pacman(0,150,255)      # Yellow pacman
#food(255,255,255)      # food dots

def setpills(b,g,r):
    for led in range(numleds):
        ledstrip.led_set(led, brightness, b, g, r)
        ledstrip.write_leds()



def pacmove(b,g,r):
    for led in range(numleds):
        ledstrip.led_set(led, brightness, b, g, r)
        ledstrip.led_set(led-1, brightness, 0,0,0)
        if led == numleds-1:
            setpills(255,255,255)
        ledstrip.write_leds()
        sleep(delay)

setpills(255,255,255)

try:
    while True:
        pacmove(0,150,255)



finally:
    print("/nAll LEDs OFF - BYE!/n")
    ledstrip.reset_leds()


