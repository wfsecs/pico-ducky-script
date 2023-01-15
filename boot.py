from board import *
import digitalio
import storage

noStorageStatus = False
noStoragePin = digitalio.DigitalInOut(GP15)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = not noStoragePin.value

if(noStorageStatus == True):
    storage.disable_usb_drive()
else:
    print("USB drive enabled")