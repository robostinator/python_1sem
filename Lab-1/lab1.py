import time
import os
import sys


BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'
YELLOW = "\x1B[48;2;253;185;19m"
GREEN = "\x1B[48;2;0;106;68m"
RED= "\x1B[48;2;193;39;45m"


def flag():
    pixel = '  '
    size=3 
    length=size*5
    height= size*3

    for color in [YELLOW,GREEN,RED]:
        for i in range(size):
            print(color+pixel*length+RESET)


def loading():
    for i in range(100):
        print(f'\u001b[20DLoading... {i + 1}%', end='', flush=True)
        time.sleep(0.1)
    print(" Done!")


def multiple_progressbar(num_tasks):
    bar_width = 25
    for task in range(1, num_tasks + 1):
        for progress in range(1, bar_width + 1):
            bar = '#' * progress + '_' * (bar_width - progress)
            print(
                f'{BEGIN}Task {task}/{num_tasks} [{bar}] {progress * 4}%', end='', flush=True)
            time.sleep(0.1)
    print(" Done")

def pattern():
    pixel="  "
    print(WHITE+pixel*3+RESET+pixel*9+WHITE+pixel*3+RESET)
    print(pixel*3+WHITE+pixel*2+RESET+pixel*5+WHITE+pixel*2+RESET+pixel*3)
    print(pixel*5+WHITE+pixel*1+RESET+pixel*3+WHITE+pixel*1+RESET+pixel*5)
    print(pixel*6+WHITE+pixel*1+RESET+pixel*1+WHITE+pixel*1+RESET+pixel*5)
    print(pixel*6+WHITE+pixel*1+RESET+pixel*1+WHITE+pixel*1+RESET+pixel*5)
    print(pixel*7+WHITE+pixel*1+RESET+pixel*7)
    print(pixel*7+WHITE+pixel*1+RESET+pixel*7)

def diamond():
    height = 15
    center = height // 2
    offset = height // 2
    step = 1
    lenght = 1
    colors = [87, 196, 226]

    while True:
        for color in colors:
            for line in range(height):
                print(
                    f'{' ' * offset}\u001b[48;5;{color}m{' ' * lenght}{RESET}')
                if line < center:
                    offset -= step
                    lenght += step * 2
                else:
                    offset += step
                    lenght -= step * 2
            print(f'\u001b[{height + 2}A')
            print(f'\u001b[{offset + 1}D')
            lenght = 1
            offset = height // 2
            time.sleep(2)


def sequence():
    file=open('sequence.txt',"r")
    lines = file.readlines()
    odds = []
    evens = []
    for i in range(len(lines)):
        val=float(lines[i])
        if i%2==0:
            evens.append(abs(val))
        else: 
            odds.append(abs(val))
        # print(val,type(val))
        
    file.close()
    mean_odds=sum(odds)/len(odds)
    mean_evens=sum(evens)/len(evens)
    sm=mean_odds+mean_evens
    print(RED+"  "*(int((mean_evens*10)/sm))+RESET,mean_evens)
    print(WHITE+"  "*(int((mean_evens*10)/sm))+RESET,mean_odds)


def draw_function(size=10):
    for y in range(size-1,-1,-1):
        line=["  "]*size
        line[int(y)]="*"
        print(line)

def animation():
    while True:
        for i in range(4):
            os.system("cls")
            print("\033[1;1H")
            print(i*"*")
            time.sleep(0.3)



flag()
pattern()
sequence()
draw_function()
# animation()
