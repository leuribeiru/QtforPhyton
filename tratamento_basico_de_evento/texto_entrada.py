import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel

aplicacao = QApplication(sys.argv)
janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")

texto_entrada = QLineEdit(janela)
texto_entrada.move(50, 30)
texto_entrada.resize(200, 30)

label = QLabel("Escreva algo e aperte <enter>", janela)
label.move(50, 60)
label.resize(200,30)

result = QLabel("", janela)
result.move(50,90)
result.resize(200,30)

def onReturnPressed():
    result.setText(texto_entrada.text())

# quando o usuário pressionar <enter> na caixa de texto
texto_entrada.returnPressed.connect(onReturnPressed)

janela.show()
aplicacao.exec_()
sys.exit()
