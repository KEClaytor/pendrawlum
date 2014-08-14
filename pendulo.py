# Import the motor module and prepare to draw
import motor

def draw(image, pen_down_val, pen_up_val, half_period, belay_time):
    motor.initalize()
    alternate = False
    motor.wait_for_start()
    for line in image:
        if alternate:
            line.reverse()
        motor.draw_line(1, line, pen_down_val, pen_up_val, half_period)
        motor.step_lock(2, belay_time, 'rev')
    # Lift up the pen and return the walker to start
    motor.step_lock(1, 0, motor.get_motor_dirn(pen_up_val, pen_down_val, pen_up_val))
    rewind_time = belay_time * len(line)
    motor.step_lock(2, rewind_time, 'for')
    return True

if __name__ == "__main__":
    print "Wrapper for motor controls."
    print "TODO: Get fancy about the transforms."

