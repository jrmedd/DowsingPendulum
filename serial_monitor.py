import serial

mb = serial.Serial('/dev/tty.usbmodem1412', baudrate=115200)

while True:
    incoming = mb.readline().strip()
    print(incoming.decode('utf-8'))
