import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
# cria um label dentro da janela
label = QLabel(janela)
# configura o texto do label
label.setText("Label 1")
# posiciona o label na janela (esquerda, topo)
label.move(100, 50)
# aplica um estilo ao label
label.setStyleSheet('QLabel \
{font-size: 20px; color: green; background-color: white; }')
janela.show()
aplicacao.exec_()
sys.exit()
