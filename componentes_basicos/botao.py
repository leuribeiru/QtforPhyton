import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

aplicacao = QApplication(sys.argv)
janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
# instância de um botão dentro da janela
botao = QPushButton("Meu Botão", janela)
# posição dentro da janela (esquerda, topo)
botao.move(50,50) 
# tamanho (largura, altura)
botao.resize(200,100) 
# estilo do botão
botao.setStyleSheet("QPushButton \
{background-color: blue; color: white; font-size: 32px}")
janela.show()
aplicacao.exec_()
sys.exit()
