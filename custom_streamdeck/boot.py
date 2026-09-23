import board
import digitalio
import storage
import supervisor
import usb_cdc
import usb_hid

# --- HARDWARE BRIDGE DETECT (D0 -> D5) ---
# Drive D0 LOW and read D5 with an internal pull-up resistor
pin_out = digitalio.DigitalInOut(board.D0)  
pin_out.direction = digitalio.Direction.OUTPUT
pin_out.value = False

pin_in = digitalio.DigitalInOut(board.D5)   
pin_in.direction = digitalio.Direction.INPUT
pin_in.pull = digitalio.Pull.UP

# If D0 and D5 are connected, pin_in reads LOW (False)
is_connected = not pin_in.value

# CRITICAL: Release pins so KMK can scan them in code.py
pin_out.deinit()
pin_in.deinit()

# --- CONDITIONAL BOOT BEHAVIOR ---
if not is_connected:
    # Stealth Mode: Hide USB drive and serial debug console
    storage.disable_usb_drive()
    usb_cdc.disable()
else:
    # Dev Mode: Rename drive to STREAMDECK when connected
    storage.remount("/", readonly=False)
    m = storage.getmount("/")
    m.label = "STREAMDECK"
    storage.remount("/", readonly=True)

# --- USB HID IDENTIFICATION ---
supervisor.set_usb_identification(
    manufacturer="Baruck",
    product="StreamDeck MacroPad",
)

usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        usb_hid.Device.CONSUMER_CONTROL,
        #usb_hid.Device.MOUSE,
    )
)