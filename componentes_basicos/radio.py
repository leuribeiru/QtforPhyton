import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGroupBox, QRadioButton

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")
# cria uma instancia de um grupo de seleção dentro da janela
group_box = QGroupBox("Selecione uma opção", janela) 
group_box.move(50,50)
group_box.resize(200,100)
group_box.setStyleSheet('QGroupBox \
{background-color: yellow}')
# cria os radio buttons dentro do grupo de seleção
radio_btn_1 = QRadioButton("Opção 1", group_box)
radio_btn_1.move(10,20)
radio_btn_2 = QRadioButton("Opção 2", group_box)
radio_btn_2.move(10,40)
radio_btn_3 = QRadioButton("Opção 3", group_box)
radio_btn_3.move(10,60)
radio_btn_3.setChecked(True)
janela.show()

aplicacao.exec_()
sys.exit()
