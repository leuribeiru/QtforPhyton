import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGroupBox, QRadioButton, QPushButton, QLabel

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 300 ) 
janela.setWindowTitle("Primeira Janela")
group_box = QGroupBox("Selecione uma opção", janela) 
group_box.move(50,20)
group_box.resize(200,100)
radio_btn_1 = QRadioButton("Opção 1", group_box)
radio_btn_1.move(10,20)
radio_btn_2 = QRadioButton("Opção 2", group_box)
radio_btn_2.move(10,40)
radio_btn_3 = QRadioButton("Opção 3", group_box)
radio_btn_3.move(10,60)
radio_btn_3.setChecked(True)

label = QLabel("Opção selecionada: ", janela)
label.move(50, 190)
label.resize(200,30)

resultado = QLabel("", janela)
resultado.move(50, 210)
resultado.resize(200,30)

def onButtonClicked():
    checked = ""
    # verifica qual radiobutton esta selecionado e
    # atribui a variavel checked o texto correspondente
    if(radio_btn_1.isChecked()):
        checked = radio_btn_1.text()
    elif(radio_btn_2.isChecked()):
        checked = radio_btn_2.text()
    elif(radio_btn_3.isChecked()):
        checked = radio_btn_3.text()
    # atribui a label resultado o valor do radio button selecionado
    resultado.setText(checked)
    
botao = QPushButton("Obter opção selecionada", janela)
botao.move(50, 140)
botao.resize(200, 30)
botao.clicked.connect(onButtonClicked)

janela.show()

aplicacao.exec_()
sys.exit()
