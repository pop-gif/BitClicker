# reset button
def reset():
    global score, autoclick, autoclick_speed, autoclickV2, autoclickV2_speed, autoclickV3, autoclickV3_speed
    score = 0
    autoclick = 0
    autoclick_speed = 1
    autoclickV2 = 0
    autoclickV2_speed = 1
    autoclickV3 = 0
    autoclickV3_speed = 0
input.on_button_pressed(Button.A, reset)
# self explanitory
def autoclickersman():
    global score, autoclick, autoclick_speed, autoclickV2, autoclickV2_speed, autoclickV3, autoclickV3_speed
    if input.button_is_pressed(Button.B):
        if autoclick == 0 and score >= 100:
            score -= 100
            autoclick += 1
        elif autoclick > 0 and score >= 100:
                score -= 100
                autoclick_speed += 1
    if pins.digital_read_pin(DigitalPin.P16) == 1:
        if autoclickV2 == 0 and score >= 500:
            score -= 500
            autoclickV2 += 1
        elif autoclickV2 > 0 and score >= 500:
            score -= 500
            autoclickV2_speed += 1
    if pins.digital_read_pin(DigitalPin.P12) == 1:
        if autoclickV3 == 0 and score >= 1000:
            score -= 1000
            autoclickV3 += 1
        elif autoclickV3 > 0 and score >= 1000:
            score -= 1000
            autoclickV3_speed += 1
#game variables
autoclickV3_speed = 0
autoclickV3 = 0
autoclickV2_speed = 0
autoclickV2 = 0
autoclick_speed = 0
autoclick = 0
score = 0
autoclick = 0
autoclick_speed = 1
autoclickV2 = 0
autoclickV2_speed = 1
autoclickV3 = 0
autoclickV3_speed = 0
def pointclicker():
    global score, autoclick, autoclick_speed, autoclickV2, autoclickV2_speed, autoclickV3, autoclickV3_speed
    basic.show_number(score, 50)
    # pointclick button
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        score += 1
    # easter egg
    if pins.analog_read_pin(AnalogPin.P1) == 1010 and pins.analog_read_pin(AnalogPin.P11) == 4:
        basic.show_string("Black Hispanic, Cybersecurity", 75)
    # win
    if score >= 10000:
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.show_string("YOU WIN!!!", 50)
        basic.show_string("Alexander Mariacuevas, Black Hispanic, Cybersecurity", 75)
        basic.pause(1000)
        pins.digital_write_pin(DigitalPin.P2, 0)
        score = 0
        autoclick = 0
        autoclick_speed = 1
        autoclickV2 = 0
        autoclickV2_speed = 1
        autoclickV3 = 0
        autoclickV3_speed = 0
basic.forever(pointclicker)
# separate forever function for convenience
def autoclickers():
    global score
    autoclickersman()
    while autoclick > 0:
        score += 1
        basic.pause(1000 / autoclick_speed)
    while autoclickV2 > 0:
        score += 1
        basic.pause(750 / autoclickV2_speed)
    while autoclickV3 > 0:
        score += 1
        basic.pause(500 / autoclickV3_speed)
basic.forever(autoclickers)