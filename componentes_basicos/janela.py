import sys
from PySide2.QtWidgets import QApplication, QMainWindow

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
janela.show()

aplicacao.exec_()
sys.exit()
