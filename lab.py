import random

from tkinter import *

# константы
WIDTH = 640
HEIGHT = 640
SEG_SIZE = 15
IN_GAME = True
lvl = 0.5
"список м помощью которого делаю лабиринт"
lst = []


def massiv(lst):
    for i in range(4):
        lst.append(random.randint(0, 7))


massiv(lst)


def main():
    
    global IN_GAME
    if IN_GAME:
        s.move(lvl)
        s.oo()
        ''' а 2 строчки внизу координаты шарика передают'''
        head_coords = c.coords(s.segment.instance)
        x1, y1, x2, y2 = head_coords

        
        if y2 > 0 and y1 < 105:
            if x1 > (lst[0]) * 80 and x2 < (lst[0] + 1) * 80:
                IN_GAME = True
            else:
                IN_GAME = False

        if y2 > 105 and y1 < 160:
            if lst[0] > lst[1]:
                if x1 > (lst[1]) * 80 and x2 < (lst[0] + 1) * 80:
                    IN_GAME = True
                else:
                    IN_GAME = False
            else:
                if x1 > (lst[0]) * 80 and x2 < (lst[1] + 1) * 80:
                    IN_GAME = True
                else:
                    IN_GAME = False
        if y2 > 415 and y1 < 480:
            if lst[2] > lst[3]:
                if x1 > (lst[3]) * 80 and x2 < (lst[2] + 1) * 80:
                    IN_GAME = True
                else:
                    IN_GAME = False
            else:
                if x1 > (lst[2]) * 80 and x2 < (lst[3] + 1) * 80:
                    IN_GAME = True
                else:
                    IN_GAME = False

        if y2 > 240 and y1 < 320:
            if lst[1] > lst[2]:
                if x1 > (lst[2]) * 80 and x2 < (lst[1] + 1) * 80:
                    IN_GAME = True
                else:
                    IN_GAME = False
            else:
                if x1 > (lst[1]) * 80 and x2 < (lst[2] + 1) * 80:
                    IN_GAME = True
                else:
                    IN_GAME = False

        if y2 > 160 and y1 < 240:
            if x1 > (lst[1]) * 80 and x2 < (lst[1] + 1) * 80:
                IN_GAME = True
            else:
                IN_GAME = False

        elif y2 > 320 and y1 < 400:
            if x1 > lst[2] * 80 and x2 < (lst[2] + 1) * 80:
                IN_GAME = True
            else:
                IN_GAME = False

        elif y2 > 6 * 80 and y1 < 560:
            if x1 > lst[3] * 80 and x2 < (lst[3] + 1) * 80:
                IN_GAME = True
            else:
                IN_GAME = False
        elif y2 > 7 * 80 and y1 < 640:
            if x1 > lst[3] * 80 and x2 < (lst[3] + 1) * 80:
                IN_GAME = True
            else:
                IN_GAME = False
        ''' а тут гейм обрывается если шарик залетает за окно'''
        if x1 < 0 or x2 > WIDTH or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False

        root.after(10, main)

    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
                      text="GAME OVER!",
                      font="Arial 20",
                      fill="red")

#класс создает шарик, я сначал хотел сделать  несколько шариков в зависимости от урованя шоб они крутились друг за другом но чет сложно
class Segment(object):

    def __init__(self, x, y):
        self.instance = c.create_oval(x, y,
                                      x + SEG_SIZE, y + SEG_SIZE,
                                      fill="pink")


class Kek(object):


    def __init__(self, segment, lvl):
        self.segment = segment
        self.lvl = lvl

        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}

        self.vector = self.mapping["Up"]

    # функиця отвечает за движение шарика
    def move(self, lvl):
        x1, y1, x2, y2 = c.coords(self.segment.instance)

        c.coords(self.segment.instance,
                 x1 + self.vector[0] * SEG_SIZE * self.lvl * 0.1,
                 y1 + self.vector[1] * SEG_SIZE * self.lvl * 0.1,
                 x2 + self.vector[0] * SEG_SIZE * self.lvl * 0.1,
                 y2 + self.vector[1] * SEG_SIZE * self.lvl * 0.1)
#а эта отвечает за переключение напрвалений
    def change_direction(self, event):
        """ Changes direction of snake """
        global lvl
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
        if event.keysym == 'Escape':
            lvl=0.5
            retry(0.5)
#ут условие типо доходишь до финиша перекидываешься на след уровень
    def oo(self):
        head_coords = c.coords(s.segment.instance)
        x1, y1, x2, y2 = head_coords
        global lvl
        if y1 < 80:
            lvl += 0.3
            retry(lvl )


# вва окна
root = Tk()
root.title("kek")

#ну это все это декораци прост
def paint(x, y,color):
    c.create_rectangle(80 * x, 80 * y, 80 * (x + 1), 80 * (y + 1), fill=color, outline='black',
                       width=10)


c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#c613d6")


def rect(lst,color):
    for i in range(lst[0], lst[1] + 1):
        paint(i, 1,color)
    for i in range(lst[1], lst[0] + 1):
        paint(i, 1,color)
    paint(lst[1], 2,color)
    for i in range(lst[1], lst[2] + 1):
        paint(i, 3,color)
    for i in range(lst[2], lst[1] + 1):
        paint(i, 3,color)
    paint(lst[2], 4,color)
    for i in range(lst[3], lst[2] + 1):
        paint(i, 5,color)
    for i in range(lst[2], lst[3] + 1):
        paint(i, 5,color)
    paint(lst[3], 6,color)
    paint(lst[3], 7,color)


rect(lst,'yellow')

c.create_rectangle(80 * lst[0], 0, 80 * (lst[0] + 1), 80, fill='red', outline='white',
                   width=10)

c.create_text(WIDTH / 2, 620,
              text="для перезапуска нажмите Esk",
              font="Arial 20",
              fill="black")
c.create_text(80 * (2*lst[0] + 1) / 2, 40,
              text="1",
              font="Arial 50",
              fill="black")

#эта функция удаляет старый шарик добавляет новый в нужной позиции на клавишу еск
def retry(i):
    global lst
    lst = []
    massiv(lst)
    global s
    global IN_GAME
    if (i-0.5)/0.3+1<4:
        c.create_rectangle(0, 0, 640, 640, fill='#c613d6', outline='white',
                       width=0)
        rect(lst,'yellow')
    else:
        if (i-0.5)/0.3+1<8:
            c.create_rectangle(0, 0, 640, 640, fill='#c613d6', outline='#868a87',
                               width=0)
            rect(lst, '#2d13d6')
        else:
            c.create_rectangle(0, 0, 640, 640, fill='#c613d6', outline='#4d4f4d',
                               width=0)
            rect(lst, '#0fdb50')



    c.create_rectangle(80 * lst[0], 0, 80 * (lst[0] + 1), 80, fill='red', outline='white',
                       width=10)

    c.create_text(WIDTH / 2, 620,
                  text="для перезапуска нажмите Esk",
                  font="Arial 20",
                  fill="black")
    c.create_text(80 * (2 * lst[0] + 1) / 2, 40,
                  text="{}".format(int((i-0.5)/0.3+1)),
                  font="Arial 50",
                  fill="black")
    segments = Segment((2 * lst[3] + 1) * 40, 610)
    s = Kek(segments, i)

    IN_GAME = True
    c.bind("<KeyPress>", s.change_direction)
    main()
    root.mainloop()


c.grid()

c.focus_set()

segments = Segment((2 * lst[3] + 1) * 40, 610)
s = Kek(segments, lvl)


c.bind("<KeyPress>", s.change_direction)

main()
root.mainloop()
