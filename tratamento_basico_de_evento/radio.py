import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGroupBox, QRadioButton, QLabel

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 220 ) 
janela.setWindowTitle("Primeira Janela")

label = QLabel("Radio button clicada", janela)
label.move(50,120)
label.resize(100, 30)

result = QLabel("", janela)
result.move(50,150)
result.resize(100,60)

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

def onClickRadio():
    text = ""
    text += "radio button 1: " + str(radio_btn_1.isChecked())
    text += "\nradio button 2: " + str(radio_btn_2.isChecked())
    text += "\nradio button 3: " + str(radio_btn_3.isChecked())
    result.setText(text)

radio_btn_1.clicked.connect(onClickRadio)
radio_btn_2.clicked.connect(onClickRadio)
radio_btn_3.clicked.connect(onClickRadio)

onClickRadio()
janela.show()

aplicacao.exec_()
sys.exit()
