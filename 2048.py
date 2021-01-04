#!/usr/local/bin/python3.6
import sys,random
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

class UI(QMainWindow):
    keyPressed = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2048')
        self.setFixedSize(550,550)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self._centralWidget.setStyleSheet("background-color:black;")
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # self.keyPressed = keyPressed
        self._createDisplay()
        self._createGrid()
    def _createDisplay(self):
        self.display = QLabel('0')
        self.display.setStyleSheet("background-color:white;")
        self.generalLayout.addWidget(self.display)
    def _createGrid(self):
        gridLayout = QGridLayout()
        self.buttons={}
        buttons={
            '0':(0,0),
            '1':(0,1),
            '2':(0,2),
            '3':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '7':(1,3),
            '8':(2,0),
            '9':(2,1),
            '10':(2,2),
            '11':(2,3),
            '12':(3,0),
            '13':(3,1),
            '14':(3,2),
            '15':(3,3)
        }
        for key,value in buttons.items():
            self.buttons[key]=QLabel('')
            self.buttons[key].setFixedSize(100,100)
            self.buttons[key].setAlignment(Qt.AlignCenter)
            self.buttons[key].setStyleSheet("border: 1px solid black;")
            self.buttons[key].setStyleSheet("background-color:white;")
            gridLayout.addWidget(self.buttons[key],value[0],value[1])
        self.generalLayout.addLayout(gridLayout)
    def keyPressEvent(self,event):
        super(UI,self).keyPressEvent(event)
        if event.key() == Qt.Key_Escape:
            self.close()
        self.keyPressed.emit(event.key())
    def updateView(self,data):
        if(data[0]==['GAME OVER']):
            for i in range(4):
                for j in range(4):
                    self.buttons[str(4*i+j)].setText('')
            self.display.setText('GAME OVER, SCORE: {}'.format(data[1]))
            self.keyPressed.disconnect()
        else:
            for i in range(4):
                for j in range(4):
                    if data[0][i][j]==0:
                        self.buttons[str(4*i+j)].setText('')
                    else:
                        self.buttons[str(4*i+j)].setText(str(data[0][i][j]))
            self.display.setText(str(data[1]))
class Controller:
    def __init__(self,model,view):
        self._model = model
        self._view = view
        self._connectSignals()
        self._view.updateView([self._model.state,0])
    def _connectSignals(self):
        self._view.keyPressed.connect(self._model.modifyState)
        self._model.stateGenerated.connect(self._view.updateView)
class Model(QObject):
    stateGenerated = pyqtSignal(list)
    def __init__(self):
        super(Model,self).__init__()
        self.state=[
            [2,2,4,8],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        self.unused=set()
        self.score=0
        for i in range(4):
            for j in range(4):
                self.unused.add((i,j))
    def add_tile(self):
        if len(self.unused) == 0:
            self.state = ['GAME OVER']
        else:
            i,j = random.choice(list(self.unused))
            value = random.choices([2,4],[0.9,0.1])
            self.state[i][j]=value[0]
            self.unused.discard((i,j))
            print('Added {} at {} {}'.format(value,i,j))
            # print(len(self.unused))

    def move(self):
        score=0
        if self.key_pressed == 'LEFT':
            for i in range(4):
                # l = [0]
                l=[]
                canMerge=True
                for j in range(4):
                    if self.state[i][j]==0:
                        continue
                    # if l[-1]==0 or l[-1]==self.state[i][j]:
                    #     if l[-1]==self.state[i][j]:
                    #         self.score+=self.state[i][j]
                    #     l[-1]+=self.state[i][j]
                    elif len(l)!=0 and l[-1]==self.state[i][j] and canMerge:
                            self.score+=self.state[i][j]
                            l[-1]+=self.state[i][j]
                            # print(self.state[i][j])
                            canMerge=False
                    else:
                        l.append(self.state[i][j])
                l.extend([0]*(4-len(l)))
                self.state[i]=l
        elif self.key_pressed=='RIGHT':
            for i in range(4):
                # l=[0]
                l=[]
                canMerge=True
                for j in range(4):
                    if self.state[i][3-j]==0:
                        continue
                    # if l[-1]==0 or l[-1]==self.state[i][3-j]:
                    #     if l[-1]==self.state[i][3-j]:
                    #         self.score+=self.state[i][3-j]
                    #     l[-1]+=self.state[i][3-j]
                    elif len(l)!=0 and l[-1]==self.state[i][3-j] and canMerge:
                        self.score+=self.state[i][3-j]
                        l[-1]+=self.state[i][3-j]
                        canMerge=False
                    else:
                        l.append(self.state[i][3-j])
                l.extend([0]*(4-len(l)))
                l.reverse()
                self.state[i]=l
        elif self.key_pressed=='UP':
            for i in range(4):
                # l=[0]
                l=[]
                canMerge=True
                for j in range(4):
                    if self.state[j][i]==0:
                        continue
                    # if l[-1]==0 or l[-1]==self.state[j][i]:
                    #     if l[-1]==self.state[j][i]:
                    #         self.score+=self.state[j][i]
                    #     l[-1]+=self.state[j][i]
                    elif len(l)!=0 and l[-1]==self.state[j][i] and canMerge:
                        self.score+=self.state[j][i]
                        l[-1]+=self.state[j][i]
                        canMerge=False
                    else:
                        l.append(self.state[j][i])
                l.extend([0]*(4-len(l)))
                for j in range(4):
                    self.state[j][i]=l[j]
        elif self.key_pressed=='DOWN':
            for i in range(4):
                # l=[0]
                l=[]
                canMerge=True
                for j in range(4):
                    if self.state[3-j][i]==0:
                        continue
                    # if l[-1]==0 or l[-1]==self.state[3-j][i]:
                    #     if l[-1]==self.state[3-j][i]:
                    #         self.score+=self.state[3-j][i]
                    #     l[-1]+=self.state[3-j][i]
                    elif len(l)!=0 and l[-1]==self.state[3-j][i] and canMerge:
                        self.score+=self.state[3-j][i]
                        l[-1]+=self.state[3-j][i]
                        canMerge=False
                    else:
                        l.append(self.state[3-j][i])
                l.extend([0]*(4-len(l)))
                for j in range(4):
                    self.state[3-j][i]=l[j]                
        for i in range(4):
            for j in range(4):
                if self.state[i][j]==0:
                    self.unused.add((i,j))
                else:
                    self.unused.discard((i,j))
    def modifyState(self,key):
        key_pressed = ''
        if key == Qt.Key_Up:
            key_pressed = 'UP'
        elif key == Qt.Key_Down:
            key_pressed = 'DOWN'
        elif key == Qt.Key_Left:
            key_pressed = 'LEFT'
        elif key == Qt.Key_Right:
            key_pressed = 'RIGHT'
        else:
            return
        self.key_pressed = key_pressed
        self.move()        
        self.add_tile() 
        self.stateGenerated.emit([self.state,self.score])

def main():
    game = QApplication(sys.argv)
    view = UI()
    view.show()
    model=Model()
    Controller(model=model,view=view)
    sys.exit(game.exec_())

if __name__=='__main__':
    main()