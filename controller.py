import pyfirmata
from pyfirmata import SERVO
port = "COM6"
board = pyfirmata.Arduino(port)
f_0= board.digital[13]
f_1= board.digital[12]
f_2= board.digital[11]
f_3= board.digital[10]
f_4= board.digital[9]
f_0.mode=SERVO
f_1.mode=SERVO
f_2.mode=SERVO
f_3.mode=SERVO
f_4.mode=SERVO
def led(total):
    if total[0]==0:
       f_0.write(0)
    else:
        f_0.write(90)
    if total[1] == 0:
        f_1.write(180)
    else:
        f_1.write(0)
    if total[2] == 0:
        f_2.write(0)
    else:
        f_2.write(180)
    if total[3]==0:
        f_3.write(180)
    else:
        f_3.write(0)
    if total[4]==0:
        f_4.write(180)
    else:
        f_4.write(37)
