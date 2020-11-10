import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QGroupBox, QCheckBox, QLabel

aplicacao = QApplication(sys.argv)

janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")

label = QLabel("Checkboxes selecionados", janela)
label.move(50,120)
label.resize(130, 30)

result = QLabel("", janela)
result.move(50,140)
result.resize(100,60)

group_box = QGroupBox("Selecione uma ou mais opções", janela) 
group_box.move(50,20)
group_box.resize(200,100)

checkbox_1 = QCheckBox("Opção 1", group_box)
checkbox_1.move(10,20)
checkbox_2 = QCheckBox("Opção 2", group_box)
checkbox_2.move(10,40)
checkbox_3 = QCheckBox("Opção 3", group_box)
checkbox_3.move(10,60)

def onClickCheckBox():
    text = ""
    text += "checkbox 1: " + str(checkbox_1.isChecked())
    text += "\ncheckbox 2: " + str(checkbox_2.isChecked())
    text += "\ncheckbox 3: " + str(checkbox_3.isChecked())
    result.setText(text)

checkbox_1.clicked.connect(onClickCheckBox)
checkbox_2.clicked.connect(onClickCheckBox)
checkbox_3.clicked.connect(onClickCheckBox)

onClickCheckBox()
janela.show()

aplicacao.exec_()
sys.exit()
