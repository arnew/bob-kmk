print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

keyboard.debug_enabled = True

keyboard.row_pins = (
        board.GP17,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
        board.GP22,
    )
keyboard.col_pins = (
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15,
        board.GP16,
    )
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
keyboard.extensions.append(StringyKeymaps())
macros = Macros()
keyboard.modules.append(macros)

# Make this for better looking formatting...
______ = 'NO'
_____ = 'TRANS'

MOLYR = KC.MO(1)

STAR = KC.MACRO('⭐')
BOAT = KC.MACRO('⛵')
GRUMP = KC.MACRO('🥴')

keyboard.keymap = [
    [
  # Layer 0 QWERTY
     'ESC',           'F1',   'F2',   'F3',   'F4', ______,   'F5',   'F6',   'F7',   'F8',   'F9',  'F10',        'F11',  'F12', 'PSCR', 'SLCK', 'PAUS',
     'GRV',           'N1',   'N2',   'N3',   'N4',   'N5',   'N6',   'N7',   'N8',   'N9',   'N0', 'MINS',        'EQL', 'BSPC',  'INS', 'HOME', 'PGUP',
     'TAB',            'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',    'P', 'LBRC',       'RBRC', 'BSLS',  'DEL',  'END', 'PGDN',
   'LCTRL',            'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L', 'SCLN', 'QUOT',        'ENT', ______,KC.MUTE,KC.VOLD,KC.VOLU,
    'LSFT', 'NONUS_BSLASH',    'Z',    'X',    'C',    'V',    'B',    'N',    'M', 'COMM',  'DOT', 'SLSH', 'NONUS_HASH', 'RSFT', 'PGUP',   'UP', 'PGDN',
    'LCTL',         'LGUI', ______, 'LALT',  'SPC',  MOLYR, 'BSPC', ______,  'SPC', ______, 'RALT', 'RGUI',        'APP', 'RCTL', 'LEFT', 'DOWN', 'RGHT'
],
    [
  # Layer 1
KC.RESET,   _____,   _____,   _____,   _____, KC.MPRV, KC.MPLY, KC.MNXT,   _____,   _____,   _____,   _____,   _____, KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
   'ESC',    'F1',    'F2',    'F3',    'F4',    'F5',    'F6',    'F7',    'F8',    'F9',   'F10',   'F11',   'F12',   _____,   KC.P7,   KC.P8,   KC.P9,
   _____,   _____,  'UP'  ,     'Y',     'U',     'I',   _____,   _____,   _____,   _____,   _____,   _____,   _____, KC.PPLS,   KC.P4,   KC.P5,   KC.P6,
   _____,   'LEFT', 'DOWN', 'RIGHT',     'H',     'J',  'LEFT',   'DOWN',   'UP', 'RIGHT',   _____,   _____,   _____,   _____,   KC.P1,   KC.P2,   KC.P3,
   _____,   _____,   _____,     'B',     'N',     'M',   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   KC.P0, KC.PDOT, KC.PENT,
   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____,   _____, KC.PENT,
  ]
]

if __name__ == '__main__':
    keyboard.go()
