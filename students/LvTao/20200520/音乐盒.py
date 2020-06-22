from microbit import *
import music

notes = ['r4:2', 'g', 'g', 'g', 'b:8', 'r:2', 'f', 'f', 'f', 'd:8']
notes1 = ['rgggbrfffd']
tune = ["C4:4", "D", "E", "C", "C", "D", "E", "C", "E", "F", "G:8", "E:4", "F", "G:8"]
tune1 = ["CDECCDECEFGEFG"]
while True:
    if button_a.is_pressed():
        music.play(notes)
        display.scroll(note1)
    elif button_b.is_pressed():
        music.play(notes)
        display.scroll(note1)
