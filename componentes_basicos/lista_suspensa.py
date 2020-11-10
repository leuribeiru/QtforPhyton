import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
# cria uma lista suspensa
lista_suspensa = QComboBox(janela)
lista_suspensa.move(100,90)
lista_suspensa.resize(100, 20)
# adiciona um item à lista suspensa
lista_suspensa.addItem("Opção 1")
# adiciona vários itens de uma vez na lista suspensa
lista_suspensa.addItems(["Opção 2", "Opção 3", "Opção 4"])

janela.show()

aplicacao.exec_()
sys.exit()
