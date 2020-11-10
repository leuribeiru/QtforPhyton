import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit

aplicacao = QApplication(sys.argv)
janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
# cria um campo de entrada de texto na janela
texto_entrada = QLineEdit(janela)
# posição (esquerda, topo)
texto_entrada.move(50, 75)
# tamanho (largura, altura)
texto_entrada.resize(200, 50)
# estilo da caixa de texto
texto_entrada.setStyleSheet('QLineEdit \
{font-size: 22px; font-style: italic; padding: 15px}')
janela.show()
aplicacao.exec_()
sys.exit()
