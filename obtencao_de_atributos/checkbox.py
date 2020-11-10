import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QPushButton, QLabel

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 300 ) 
janela.setWindowTitle("Primeira Janela")
label = QLabel("Selecione uma ou mais opções", janela) 
label.move(50,20)
label.resize(200,20)
checkbox_1 = QCheckBox("Opção 1", janela)
checkbox_1.move(50,40)
checkbox_2 = QCheckBox("Opção 2", janela)
checkbox_2.move(50,60)
checkbox_3 = QCheckBox("Opção 3", janela)
checkbox_3.move(50,80)
checkbox_3.setChecked(True)

label_resultado = QLabel("Opções selecionadas: ", janela)
label_resultado.move(50, 190)
label_resultado.resize(200,30)

resultado = QLabel("", janela)
resultado.move(50, 210)
resultado.resize(200,60)

def onButtonClicked():
    checked = ""
    # verifica quais checkboxes estão selecionados e
    # atribui a variavel checked o texto correspondente
    if(checkbox_1.isChecked()):
        checked += "\n" + checkbox_1.text()
    if(checkbox_2.isChecked()):
        checked += "\n" + checkbox_2.text()
    if(checkbox_3.isChecked()):
        checked += "\n" + checkbox_3.text()
    # atribui a label resultado o valor dos checkboxes button selecionado
    resultado.setText(checked)
    
botao = QPushButton("Obter opções selecionadas", janela)
botao.move(50, 140)
botao.resize(200, 30)
botao.clicked.connect(onButtonClicked)

janela.show()

aplicacao.exec_()
sys.exit()
