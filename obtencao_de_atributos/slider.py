import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider, QPushButton, QLabel
from PySide2.QtCore import Qt

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 200 )
janela.setWindowTitle("Primeira Janela")

slider = QSlider(janela)
slider.resize(100,30)
slider.move(100, 20)
slider.setOrientation(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)

label = QLabel("Valor do slider", janela)
label.move(100,90)
label.resize(100,20)

resultado = QLabel("", janela)
resultado.move(100,120)
label.resize(100,20)

def onButtonClicked():
    resultado.setText(str(slider.value()))

botao = QPushButton("Obter valor", janela)
botao.move(100, 60)
botao.resize(100,20)
botao.clicked.connect(onButtonClicked)

janela.show()

aplicacao.exec_()
sys.exit()