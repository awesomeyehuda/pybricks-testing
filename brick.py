from pybricks.robotics import GyroDriveBase
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor,ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch


hub = InventorHub()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
c_motor = Motor(Port.C)
d_motor = Motor(Port.D)


gyro_drive_base = GyroDriveBase(left_motor, right_motor)

