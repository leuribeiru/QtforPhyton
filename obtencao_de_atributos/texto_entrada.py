import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton

aplicacao = QApplication(sys.argv)
janela = QMainWindow()
janela.setGeometry( 100, 50, 300, 200 ) 
janela.setWindowTitle("Primeira Janela")

texto_entrada = QLineEdit(janela)
texto_entrada.move(50, 10)
texto_entrada.resize(200, 30)

label = QLabel("Texto Obtido:", janela)
label.move(50, 90)
label.resize(200,30)

resultado = QLabel("", janela)
resultado.move(50, 120)
resultado.resize(200,30)

def onButtonClick():
    # atribui o valor da caixa de texto para o label resultado
    resultado.setText(texto_entrada.text())
    # texto_entrada.text() obtém o valor que está na caixa de texto

button = QPushButton("Obter texto", janela)
button.move(50, 50)
button.resize(205,30)
# determina a função que sera executada ao clicar no botão
button.clicked.connect(onButtonClick)

janela.show()
aplicacao.exec_()
sys.exit()
