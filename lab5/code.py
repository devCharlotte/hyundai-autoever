# ============================================================
# File: 프로젝트 8


# ------------------------------------------------------------
# Color sensor values stored in original blocks

COLOR_BLACK = 0
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


def wait(seconds: float):
    pass


def motor_turn_for_direction(port: str, direction: str, value: int, unit: str):
    pass


def motor_stop(port: str):
    pass


def stop_sound():
    pass


def set_volume(volume: int):
    pass


def play_sound_until_done(sound_selector: str):
    pass


def led_image(matrix: str):
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
# 원본 사용자 정의 블록: line
# mutation:
#   proccode = "line"
#   argumentids = []
#   warp = false

def line():
    # original block:
    # if color sensor F reflected light < 54
    #     start steering -50
    # else
    #     start steering 50

    if reflectivity("F") < 54:
        start_steer(-50)
    else:
        start_steer(50)


# ============================================================
# Top-level stack 1
# Original top-level block:
#   opcode = flipperevents_whenProgramStarts
#   x = 520
#   y = -81
#

def when_program_starts_stack_1_B_motor_loop():
    while True:
        set_movement_speed(45)

        motor_turn_for_direction(
            port="B",
            direction="clockwise",
            value=45,
            unit="degrees",
        )

        motor_turn_for_direction(
            port="B",
            direction="counterclockwise",
            value=45,
            unit="degrees",
        )

        motor_turn_for_direction(
            port="B",
            direction="counterclockwise",
            value=45,
            unit="degrees",
        )

        motor_turn_for_direction(
            port="B",
            direction="clockwise",
            value=45,
            unit="degrees",
        )


# ============================================================
# Top-level stack 2
# Original top-level block:
#   opcode = flipperevents_whenProgramStarts
#   x = 24
#   y = -43
#


def when_program_starts_stack_2_main():
    set_movement_pair("DC")
    set_movement_speed(30)
    start_steer(0)

    while not ml_prediction_is("멈춰"):
        line()

    stop_move()
    wait(1)

    while not color_is("A", COLOR_RED):
        set_movement_pair("DC")
        set_movement_speed(30)
        line()

    stop_move()

    for _ in range(2):
        motor_turn_for_direction(
            port="CD",
            direction="clockwise",
            value=85,
            unit="degrees",
        )

        motor_turn_for_direction(
            port="CD",
            direction="counterclockwise",
            value=85,
            unit="degrees",
        )

        motor_turn_for_direction(
            port="CD",
            direction="counterclockwise",
            value=85,
            unit="degrees",
        )

        motor_turn_for_direction(
            port="CD",
            direction="clockwise",
            value=85,
            unit="degrees",
        )

        stop_move()

    stop_sound()
    set_volume(100)

    play_sound_until_done(
        '{"name":"Hi 5","location":"hub","path":"/extra_files/Hi 5"}'
    )

    set_movement_pair("DC")
    set_movement_speed(30)
    start_steer(0)

    while not color_is("A", COLOR_BLACK):
        line()

    if color_is("A", COLOR_BLACK):
        motor_stop("B")
        stop_move()


# ============================================================
# Top-level stack 3
# Original top-level block:
#   opcode = flipperevents_whenProgramStarts
#   x = 699
#   y = 793
#


def when_program_starts_stack_3_led_loop():
    while True:
        led_image("9909999099000009000909990")


# ============================================================
# Original project start structure


def run_project_8():
    start_parallel(
        when_program_starts_stack_1_B_motor_loop,
        when_program_starts_stack_2_main,
        when_program_starts_stack_3_led_loop,
    )
