from mindstorms import MSHub, Motor, MotoPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

hub = MSHub()
wheels = MotoPair('E','A') # can be changed
left_motor = Motor('A')

###### Tune #########
kp = 11
ki = 4.2
kd = 92
roll_target = 87.358

integral = 0
error = 0
start_target = 0
derivative = 0
prev_error = 0
result = 0
ks = -0.6
start = 0
start_target = 0
left_motor.set_degrees_counted(0)
while hub.motion_sensor.get_roll_angle()<120 and hub.motion_sensor.get_roll_angle()>60:
    error = roll_target - hub.motion_sensor.get_roll_angle()
    integral = integral +(error*0.25)
    derivative = error -prev_error
    prev_error = error
    start = (start_target - left_motor.get_degrees_counted()) # this can be modify
    result = (error*kp) + (integral*ki) + (derivative*kd) + (start*ks)
    wheels.start_at_power(math.floor(result),0)
wheels.stop()