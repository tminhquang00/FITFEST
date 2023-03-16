from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

car = MSHub()
movement_motors = MotorPair('A','B')
left_motor = Motor('A')

distance_sensor = DistanceSensor('D')

# Set yaw to zero
hub.motion.yaw_pitch_roll(0) 
yield 100 
left_motor.set_degrees_counted(0)

while left_motor.get_degrees_counted() < 400:
    GSPK = 1.5
    steering_speed =(0-hub.motion.yaw_pitch_roll()[0])*GSPK
    movement_motors.start_at_power(steering_speed, -30)