import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

from kmk.extensions.oled import Oled, TextEntry


def pick(*names):
    for n in names:
        if hasattr(board, n):
            return getattr(board, n)
    raise ValueError("Missing pin names: " + ", ".join(names))


COL0 = pick("GP0", "D0")
COL1 = pick("GP1", "D1")

ROW0 = pick("GP2", "D2")
ROW1 = pick("GP3", "D3")
ROW2 = pick("GP4", "D4")

ENC_A = pick("GP26", "A0")
ENC_B = pick("GP27", "A1")

OLED_SDA = pick("GP6", "SDA", "D6")
OLED_SCL = pick("GP7", "SCL", "D7")


keyboard = KMKKeyboard()

keyboard.col_pins = (COL0, COL1)
keyboard.row_pins = (ROW0, ROW1, ROW2)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

layers = Layers()
keyboard.modules.append(layers)

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (ENC_A, ENC_B, None, False, 4),
)

encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),  
    ((KC.MPRV, KC.MNXT, KC.NO),),    
]

oled = Oled(
    sda=OLED_SDA,
    scl=OLED_SCL,
    width=128,
    height=32,
    entries=[
        TextEntry(text="Alistair HackPad", x=0, y=0),
        TextEntry(text="L0: EDIT", x=0, y=16, layer=0),
        TextEntry(text="L1: MEDIA", x=0, y=16, layer=1),
    ],
    dim_time=20,
    off_time=60,
)
keyboard.extensions.append(oled)

_______ = KC.TRNS

keyboard.keymap = [
    [
        KC.LGUI(KC.C),              KC.LGUI(KC.V),
        KC.LGUI(KC.Z),              KC.LGUI(KC.LSFT(KC.Z)),
        KC.LGUI(KC.SPC),            KC.MO(1),
    ],

    [
        KC.MPLY,                    KC.MUTE,
        KC.MPRV,                    KC.MNXT,
        KC.VOLD,                    _______,
    ],
]

if __name__ == "__main__":
    keyboard.go()