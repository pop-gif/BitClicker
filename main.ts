//  reset button
input.onButtonPressed(Button.A, function reset() {
    
    score = 0
    autoclick = 0
    autoclick_speed = 1
    autoclickV2 = 0
    autoclickV2_speed = 1
    autoclickV3 = 0
    autoclickV3_speed = 0
})
//  self explanitory
function autoclickersman() {
    
    if (input.buttonIsPressed(Button.B)) {
        if (autoclick == 0 && score >= 100) {
            score -= 100
            autoclick += 1
        } else if (autoclick > 0 && score >= 100) {
            score -= 100
            autoclick_speed += 1
        }
        
    }
    
    if (pins.digitalReadPin(DigitalPin.P16) == 1) {
        if (autoclickV2 == 0 && score >= 500) {
            score -= 500
            autoclickV2 += 1
        } else if (autoclickV2 > 0 && score >= 500) {
            score -= 500
            autoclickV2_speed += 1
        }
        
    }
    
    if (pins.digitalReadPin(DigitalPin.P12) == 1) {
        if (autoclickV3 == 0 && score >= 1000) {
            score -= 1000
            autoclickV3 += 1
        } else if (autoclickV3 > 0 && score >= 1000) {
            score -= 1000
            autoclickV3_speed += 1
        }
        
    }
    
}

// game variables
let autoclickV3_speed = 0
let autoclickV3 = 0
let autoclickV2_speed = 0
let autoclickV2 = 0
let autoclick_speed = 0
let autoclick = 0
let score = 0
autoclick = 0
autoclick_speed = 1
autoclickV2 = 0
autoclickV2_speed = 1
autoclickV3 = 0
autoclickV3_speed = 0
basic.forever(function pointclicker() {
    
    basic.showNumber(score, 50)
    //  pointclick button
    if (pins.digitalReadPin(DigitalPin.P0) == 1) {
        score += 1
    }
    
    //  easter egg
    if (pins.analogReadPin(AnalogPin.P1) == 1010 && pins.analogReadPin(AnalogPin.P11) == 4) {
        basic.showString("Black Hispanic, Cybersecurity", 75)
    }
    
    //  win
    if (score >= 10000) {
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.showString("YOU WIN!!!", 50)
        basic.showString("Alexander Mariacuevas, Black Hispanic, Cybersecurity", 75)
        basic.pause(1000)
        pins.digitalWritePin(DigitalPin.P2, 0)
        score = 0
        autoclick = 0
        autoclick_speed = 1
        autoclickV2 = 0
        autoclickV2_speed = 1
        autoclickV3 = 0
        autoclickV3_speed = 0
    }
    
})
//  separate forever function for convenience
basic.forever(function autoclickers() {
    
    autoclickersman()
    while (autoclick > 0) {
        score += 1
        basic.pause(1000 / autoclick_speed)
    }
    while (autoclickV2 > 0) {
        score += 1
        basic.pause(750 / autoclickV2_speed)
    }
    while (autoclickV3 > 0) {
        score += 1
        basic.pause(500 / autoclickV3_speed)
    }
})
