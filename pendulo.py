# Import the motor module and prepare to draw
import motor

def draw(image, pen_down_val, pen_up_val, half_period, belay_time):
    motor.initalize()
    alternate = False
    for line in image:
        if alternate:
            line.reverse()
        draw_line(1, line, pen_down_val, pen_up_val, half_period)
        step_lock(2, belay_time, 'for')
    return True

if __name__ == "__main__":
    print "Wrapper for motor controls."
    print "TODO: Get fancy about the transforms."

