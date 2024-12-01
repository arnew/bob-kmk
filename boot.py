import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP0,
    source=board.GP17,
    midi=False,
    mouse=False,
    storage=False,
    cdc_console=False,
    usb_id=('Arne\'s KMK', 'Bob'),
)
