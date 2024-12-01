import board

from kmk.bootcfg import bootcfg

bootcfg(
    # sense=board.GP28_A2, 
    sense=board.GP16,
    source=board.GP8,
    midi=False,
    mouse=False,
    storage=False,
    cdc_console=False,
    usb_id=('Arne\'s KMK', 'Bob'),
)
