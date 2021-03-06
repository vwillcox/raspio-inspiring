from time import sleep     # RasPiO Inspiring scripts
import apa                 # http://rasp.io/inspiring
numleds = 24               # number of LEDs in our display
delay = 0.04               # seconds between frames
brightness = 6             # 0=OFF (224 or 0xE0), 31=FULL (255 or 0xFF)
ledstrip = apa.Apa(numleds)

def updown(b,g,r):
    for led in range(numleds):
        ledstrip.led_set(led, brightness, b, g, r) 
        ledstrip.write_leds()
        sleep(delay)    

    for led in range(numleds -1, -1, -1):
        ledstrip.led_set(led, brightness, 0, 0, 0) 
        ledstrip.write_leds()
        sleep(delay)         
try:
    while True:
        updown(255,0,0)        # Blue
        updown(0,255,0)        # Green
        updown(0,0,255)        # Red
        updown(255,150,0)      # Cyan
        updown(0,150,255)      # Yellow
        updown(150,0,255)      # Magenta
        updown(255,255,255)    # White
        #delay = delay * 0.9    # speeds up each iteration

finally:
    print("/nAll LEDs OFF - BYE!/n")
    ledstrip.reset_leds()