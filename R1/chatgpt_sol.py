import time
import pybricks.ev3devices as devices
import pybricks.parameters as parameters
import pybricks.robotics as robotics

# Initialize the motors and sensors
left_motor = robotics.Motor(devices.PORT_A)
right_motor = robotics.Motor(devices.PORT_B)
distance_sensor = devices.DistanceSensor(devices.PORT_1)

# Define the PID constants
Kp = 1.0
Ki = 0.0
Kd = 0.0

# Define the PID variables
error = 0
error_sum = 0
last_error = 0

# Define the target distance
target_distance = 10  # cm/s

# Define the maximum and minimum speed
max_speed = 500  # deg/s
min_speed = 50  # deg/s

# Define the loop rate
loop_rate = 50  # Hz

# Define the obstacle threshold
obstacle_threshold = 7  # cm

# Define the main loop
while True:
    # Read the current distance from the sensor
    current_distance = distance_sensor.distance()

    # Check for obstacles
    if current_distance <= obstacle_threshold:
        # Stop the motors
        left_motor.stop()
        right_motor.stop()
        break

    # Calculate the error
    error = target_distance - current_distance

    # Calculate the error sum
    error_sum += error

    # Calculate the error difference
    error_diff = error - last_error

    # Calculate the output speed using the PID formula
    output_speed = Kp * error + Ki * error_sum + Kd * error_diff

    # Limit the output speed to the maximum and minimum speed
    if output_speed > max_speed:
        output_speed = max_speed
    elif output_speed < -max_speed:
        output_speed = -max_speed
    elif abs(output_speed) < min_speed:
        output_speed = min_speed * (output_speed / abs(output_speed))

    # Set the motor speed
    left_motor.dc(output_speed)
    right_motor.dc(output_speed)

    # Update the last error
    last_error = error

    # Wait for the loop to complete
    time.sleep(1 / loop_rate)
