import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

aplicacao = QApplication(sys.argv)
janela = QMainWindow()
janela.setGeometry( 100, 50, 350, 200 ) 

label = QLabel("", janela)
label.move(100,100)
label.resize(200,50)
botao1 = QPushButton("Botão 1", janela)
botao1.move(50,30) 
botao1.resize(100,50) 
botao2 = QPushButton("Botão 2", janela)
botao2.move(200,30) 
botao2.resize(100,50) 

def onButton1Clicked():
    label.setText("Clicou no botão 1")

def onButton2Clicked():
    label.setText("Clicou no botão 2")

# define qual função será executada quando o botão 1 for clicado
botao1.clicked.connect(onButton1Clicked)
# define qual função será executada quando o botão 2 for clicado
botao2.clicked.connect(onButton2Clicked)

janela.show()
aplicacao.exec_()
sys.exit()
