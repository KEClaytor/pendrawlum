# Import the motor module and prepare to draw
import motor

def draw(image, pen_down_val, pen_up_val, half_period, belay_time):
    motor.initalize()
    alternate = False
    for line in image:
        if alternate:
            line.reverse()
        motor.draw_line(1, line, pen_down_val, pen_up_val, half_period)
        motor.step_lock(2, belay_time, 'rev')
    # Return the motors to the off position
    motor.step_lock(1, 0, 'for')
    motor.step_lock(2, 0, 'for')
    return True

if __name__ == "__main__":
    print "Wrapper for motor controls."
    print "TODO: Get fancy about the transforms."

