import microbit
import radio
import neopixel


radio.config(power=1, channel=33, queue=1)
radio.on()

last_receive = 0

print("Starting")
NP = neopixel.NeoPixel(microbit.pin2, 1) # one neopixel on pin 2

while True:
    incoming = radio.receive_full() # get everything
    if incoming:
        msg, strength, time = incoming
        msg = str(msg[3:], 'utf-8') # lop off prepending characters, convert to string
        strength = strength+255 # make strength run from 0 to 255
        NP[0] = ((strength),)*3 # signal strength as brightness
        NP.show() # refresh
        microbit.display.show(msg) # show device ID
        last_receive = microbit.running_time() # get time of last receive for comparison
    if microbit.running_time() - last_receive > 3000: # no messages for three seconds
        NP.clear()
        NP.show()
        microbit.display.clear()
