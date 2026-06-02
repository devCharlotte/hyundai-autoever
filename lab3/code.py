# ============================================================
# File: 최종 3


# ------------------------------------------------------------
# Color sensor values stored in original blocks
# ------------------------------------------------------------
COLOR_GREEN = 5
COLOR_YELLOW = 7
COLOR_RED = 9


# ------------------------------------------------------------
# Abstract LEGO/Scratch block wrapper functions

def set_movement_pair(pair: str):
    pass


def set_movement_speed(speed: int):
    pass


def start_steer(steering: int):
    pass


def stop_move():
    pass


def move(direction: str, value: int, unit: str):
    pass


def wait(seconds: float):
    pass


def motor_set_speed(port: str, speed: int):
    pass


def motor_start_direction(port: str, direction: str):
    pass


def motor_stop(port: str):
    pass


def play_sound(sound_selector: str):
    pass


def stop_program(option: str):
    pass


def reflectivity(port: str) -> int:

    pass


def color_is(port: str, color_value: int) -> bool:

    pass


def ml_prediction_is(class_name: str) -> bool:

    pass


def start_parallel(*functions):

    pass


# ============================================================
# Custom block definition
# 원본 사용자 정의 블록: lin
# mutation:
#   proccode = "lin"
#   argumentids = []
#   warp = false


def lin():
    # original block:
    # if color sensor A reflected light < 55
    #     start steering -50
    # else
    #     start steering 50

    if reflectivity("A") < 55:
        start_steer(-50)
    else:
        start_steer(50)


# ============================================================
# Top-level stack 1
# Original top-level block:
#   opcode = flipperevents_whenProgramStarts
#   x = 14
#   y = -79


def when_program_starts_stack_1_main():
    set_movement_pair("DC")
    set_movement_speed(30)
  
    motor_set_speed("F", 100)
    motor_start_direction("F", "clockwise")

    while True:
        while not color_is("B", COLOR_RED):
            lin()

        if color_is("B", COLOR_RED):
            stop_move()
            motor_stop("F")
            move(
                direction="forward",
                value=6,
                unit="cm",
            )

        if color_is("B", COLOR_YELLOW):
            wait(5)
            motor_stop("F")
            stop_move()
            wait(1)

            move(
                direction="clockwise",
                value=10,
                unit="cm",
            )

            move(
                direction="back",
                value=10,
                unit="cm",
            )

            wait(3)

            play_sound(
                '{"name":"Celebrate","location":"hub","path":"/extra_files/Celebrate"}'
            )

            move(
                direction="forward",
                value=10,
                unit="cm",
            )

            move(
                direction="counterclockwise",
                value=10,
                unit="cm",
            )

            move(
                direction="forward",
                value=7,
                unit="cm",
            )

        if color_is("B", COLOR_GREEN):
            wait(3)

            motor_start_direction(
                port="F",
                direction="clockwise",
            )

        motor_set_speed("F", 100)

        while not ml_prediction_is("클래스 1"):
            lin()

        if ml_prediction_is("클래스 1"):
            stop_move()
            motor_stop("F")

        stop_move()
        stop_program("all")


# ============================================================
# Disconnected top-level block 1
# Original top-level block:
#   opcode = flippermotor_motorSetSpeed
#   x = 702
#   y = 713


def disconnected_top_level_block_1_motor_speed_15():
    motor_set_speed("F", 15)


# ============================================================
# Disconnected top-level block 2
# Original top-level block:
#   opcode = control_repeat_until
#   x = -261
#   y = 1512


def disconnected_top_level_block_2_empty_repeat_until():
    pass


# ============================================================
# Original project start structure


def run_final_3():
    start_parallel(
        when_program_starts_stack_1_main,
    )
