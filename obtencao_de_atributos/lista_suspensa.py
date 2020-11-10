import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
lista_suspensa = QComboBox(janela)
lista_suspensa.move(100,20)
lista_suspensa.resize(100, 20)
lista_suspensa.addItem("Opção 1")
lista_suspensa.addItems(["Opção 2", "Opção 3", "Opção 4"])

label = QLabel("Opção selecionada: ", janela)
label.move(100,80)
label.resize(100,20)

resultado = QLabel("", janela)
resultado.move(100,110)
resultado.resize(100,20)

def onButtonClicked():
    resultado.setText(lista_suspensa.currentText())

botao = QPushButton("Obter opção selecionada", janela)
botao.move(80, 50)
botao.resize(140,20)
botao.clicked.connect(onButtonClicked)

janela.show()

aplicacao.exec_()
sys.exit()
