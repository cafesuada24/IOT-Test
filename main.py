from lib import AMSpi
from time import sleep

def main() -> None:
    with AMSpi() as amspi:
        amspi.set_74HC595_pins(21, 20, 16)
        amspi.set_L293D_pins(5, 6, 13, 19)

        amspi.run_dc_motors([amspi.DC_Motor_1])
        
        sleep(3)

        amspi.stop_dc_motors([amspi.DC_Motor_1])

if __name__ == '__main__':
    main()

