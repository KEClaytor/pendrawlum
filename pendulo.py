# Import the motor module and prepare to draw
import motor

def fake_draw_line(dummy_motor, line, pen_down_val, pen_up_val, half_period):
    debug_string = ''
    for elem in line:
        if elem == pen_down_val:
            debug_string += '#'
        else:
            debug_string += ' '
    print debug_string

def draw(image, pen_down_val, pen_up_val, half_period, total_belay_time):
    motor.initalize()
    alternate = False
    pritn "Release button to start."
    motor.wait_for_button('falling')
    #(row, col) = image.shape()
    # Adjust belay time based on how many lines we have
    belay_time = total_belay_time / 1
    for line in image:
        if alternate:
            line.reverse()
        motor.draw_line(1, line, pen_down_val, pen_up_val, half_period)
        motor.step_lock(2, belay_time, motor.M_FOR)
        # Do some ASCII art so we can see how far we are
        fake_draw_line(1, line, pen_down_val, pen_up_val, half_period)

    # Lift up the pen and return the walker to start
    motor.set_motor_state(1, motor.M_FOR)
    # Rewind the motor until an interrupt on the switch
    motor.set_motor_state(2, motor.M_REV)
    print "Rewinding. Press button to stop."
    motor.wait_for_button('rising')
    motor.set_motor_state(2, motor.M_OFF)
    return True

if __name__ == "__main__":
    print "Wrapper for motor controls."
    print "TODO: Get fancy about the transforms."
    motor.initalize()
    print "Press button to rewind."
    motor.wait_for_button('rising')
    print "Release button to stop."
    motor.set_motor_state(2, motor.M_REV)
    motor.wait_for_button('rising')
    motor.set_motor_state(2, motor.M_OFF)

