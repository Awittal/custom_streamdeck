import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Tap, Delay
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

# Enable Macro Extension
macros = Macros()
keyboard.modules.append(macros)

# Hardware Matrix Config
keyboard.row_pins = (board.D0, board.D1)
keyboard.col_pins = (board.D2, board.D3, board.D4, board.D5, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- DEFINE YOUR MACROS HERE ---
#EMAIL_MACRO = KC.MACRO("awittal@gmail.com")
#TEXT_CTRC = KC.LCTL(KC.C)
#TEXT_CTRV = KC.LCTL(KC.V)
#QUIT_APP = KC.LALT(KC.F4)
#TASK_MGR = KC.LCTL(KC.LSFT(KC.ESC))
#NIGHT_MODE_WIN = KC.MACRO(Tap(KC.LWIN(KC.A)), Delay(100), Tap(KC.DOWN), Delay(50), Tap(KC.ENTER), Delay(50), Tap(KC.ESCAPE))
#POWER_DOWN_WIN = KC.MACRO(Tap(KC.LWIN(KC.X)), Delay(150), Tap(KC.U), Delay(100), Tap(KC.U))

SWITCH_TO_SPEAKER_WIN = KC.MACRO(Tap(KC.LWIN(KC.LCTL(KC.V))), Delay(150), Delay(50), Tap(KC.ENTER), Delay(50), Tap(KC.ESCAPE))
SWITCH_TO_HEADSET_WIN = KC.MACRO(Tap(KC.LWIN(KC.LCTL(KC.V))), Delay(200), Tap(KC.DOWN), Delay(150), Tap(KC.DOWN), Delay(150), Tap(KC.ENTER), Delay(50), Tap(KC.ESCAPE))

EXTRACT_TEXT_WIN = KC.LWIN(KC.LSHIFT(KC.T))
#KEYBOARD-MAP
keyboard.keymap = [
    [
        # Row 1: 
        #KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN,
        #SWITCH_TO_HEADSET_WIN, SWITCH_TO_SPEAKER_WIN, KC.F15, KC.F14, KC.F13,
        KC.F17, KC.F16, KC.F15, KC.F14, KC.F13, 
        
        # Row 2:
         KC.F22, EXTRACT_TEXT_WIN, KC.F20, KC.F19, KC.F18
         #KC.F22, KC.F21, KC.F20, KC.F19, KC.F18
    ]
]

if __name__ == '__main__':
    keyboard.go()
    
