import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
label = QLabel("Opção selecionada", janela)
label.move(100,60)
label.resize(100,30)
resultado = QLabel("", janela)
resultado.move(100,90)
resultado.resize(100,30)
lista_suspensa = QComboBox(janela)
lista_suspensa.move(100,30)
lista_suspensa.resize(100, 20)
lista_suspensa.addItem("Opção 1")
lista_suspensa.addItems(["Opção 2", "Opção 3", "Opção 4"])
def onCurrentTextChanged():
    resultado.setText(lista_suspensa.currentText())
lista_suspensa.currentTextChanged.connect(onCurrentTextChanged)

onClickComboBox()
janela.show()

aplicacao.exec_()
sys.exit()
