import microbit
import radio

radio.config(power=1, channel=33)
radio.on()

THIS_DEVICE = "A" # arbitrary device ID

print("Starting")

while True:
    radio.send(THIS_DEVICE) # keep pinging
