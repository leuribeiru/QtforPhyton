import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
# cria uma instancia de um grupo de seleção dentro da janela
label = QLabel("Selecione uma ou mais opções", janela) 
label.move(30,30)
label.resize(200,20)
# cria os checkbox dentro do grupo de seleção
checkbox_1 = QCheckBox("Opção 1", janela)
checkbox_1.move(30,60)
checkbox_2 = QCheckBox("Opção 2", janela)
checkbox_2.move(30,80)
checkbox_3 = QCheckBox("Opção 3", janela)
checkbox_3.move(30,100)
janela.show()

aplicacao.exec_()
sys.exit()
