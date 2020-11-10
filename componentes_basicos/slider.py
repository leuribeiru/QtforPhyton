import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider
from PySide2.QtCore import Qt

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")

# cria um objeto slider dentro da janela
slider = QSlider(janela)
slider.resize(100,30)
slider.move(100, 85)
# modifica a orientação do slider
slider.setOrientation(Qt.Horizontal)

janela.show()

aplicacao.exec_()
sys.exit()
