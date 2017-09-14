# Author: Lim Heng
# TicTacToe Game with a tkinter GUI

from tkinter import *


class TicTacToe():

    def __init__(self, master):
        """When the TicTacToe class is initiated declare variables."""
        self.moves = dict()
        self.xoro = 'O'
        self.buttons = []
        self.clearMoves()

        row = [0,0,0,1,1,1,2,2,2]
        col = [0,1,2,0,1,2,0,1,2]

        frame = Frame(master)
        frame.pack()

        self.button_restart = Button(frame, text='Restart', font = "Verdana 10", state='disabled')
        self.button_restart.bind('<Button-1>', self.onRestart)
        self.button_restart.pack(side=BOTTOM)
        self.label_caption = Label(frame, text='Welcome! Good Luck!', font="Verdana 10")
        self.label_caption.pack(side=BOTTOM)
        frame_button = Frame(frame)
        frame_button.pack()

        for i in range(9):
            but = Button(frame_button, text='', font = "Verdana 20 bold", command=lambda i=i: self.onClick(i), width=4, height=2)
            but.grid(row=row[i], column=col[i])
            self.buttons.append(but)

    def clearMoves(self):
        """Clears all saved moves in moves array."""
        self.moves['O'] = set()
        self.moves['X'] = set()
        self.xoro = 'O'

    def buttonsAll(self, onoroff=False, clear=False):
        """Disable all buttons if onoroff is False,
           enable all buttons if onoroff is True.
           Clears board of moves and color if clear is True."""
        for but in self.buttons:
            if clear:
                but['text'] = ''
                but['bg'] = 'SystemButtonFace'
            but['state'] = 'normal' if onoroff else 'disabled'
        self.label_caption['text'] = 'Welcome! Good Luck!'

    def onWin(self, winning):
        """When a winning move is made, highlight tiles."""
        for i in winning:
            self.buttons[i]['bg'] ='yellow'
        self.buttonsAll()
        self.clearMoves()
        return True

    def checkWon(self, arr):
        """Check if the last move was a winning move."""
        win = [{0,1,2},{0,3,6},{0,4,8},{3,4,5},{6,7,8},{1,4,7},{2,5,8},{2,4,6}]
        if len(arr) > 2:
            for x in win:
                sect = arr & x
                if len(sect) > 2:
                    return self.onWin(x)
        if len(arr) > 4:
            self.label_caption['text'] = 'No Winners! Try Again?'
        return False

    def onClick(self, i):
        """Check which button was clicked and mark it with X or O."""
        self.buttons[i]['text'] = self.xoro
        self.button_restart['state'] = 'normal'
        self.buttons[i]['state'] = 'disabled'
        self.moves[self.xoro].add(i)
        if self.checkWon(self.moves[self.xoro]):
            self.label_caption['text'] = '{} Wins! Try Again?'.format(self.xoro)
        else:
            self.xoro = 'X' if self.xoro == 'O' else 'O'

    def onRestart(self, event):
        """Restarts the game and clears everything."""
        self.clearMoves()
        self.buttonsAll(True, True)
        self.button_restart['state'] = 'disabled'

if __name__ == '__main__':
    window = Tk()
    window.title("TicTacToe Game")
    window.resizable(width=False, height=False)
    app = TicTacToe(window)
    window.mainloop()
