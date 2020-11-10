import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QPushButton, QFileDialog
from PySide2.QtCore import Qt
import csv

def calcular_sus(nome_arquivo):
    arquivo_csv = open(nome_arquivo, 'r')
    conteudo_csv = csv.reader(arquivo_csv, delimiter=',')
    somatorio = 0
    num_entrevistados = 0
    for index_linha, linha in enumerate(conteudo_csv):
        if index_linha != 0:
            num_entrevistados += 1
            for index_coluna, coluna in enumerate(linha):
                if index_coluna != 0:
                    if coluna == "": coluna = "3"
                    if index_coluna % 2 == 0:
                        somatorio += 5-int(coluna)
                    else:
                        somatorio += int(coluna)-1
    res = (somatorio/num_entrevistados)*2.5
    return int(round(res, 0))


aplicacao = QApplication(sys.argv)

janela = QMainWindow()
# setGeometry(esquerda, topo, largura, altura)
janela.setGeometry( 100, 50, 300, 250 ) 
janela.setWindowTitle("Calculo de usabilidade")

label = QLabel("Informe a nota que você acredita que \no teste de usabilidade irá resultar: ", janela)
label.move(20,20)
label.resize(200,40)

label_slider_0 = QLabel("0", janela)
label_slider_0.move(20, 60)
label_slider_0.resize(20, 20)

label_slider_100 = QLabel("100", janela)
label_slider_100.move(260, 60)
label_slider_100.resize(20, 20)

slider = QSlider(janela)
slider.move(20, 80)
slider.resize(260, 20)
slider.setOrientation(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)

text_hipotese = QLabel("Hipótese: ", janela)
text_hipotese.move(20, 110)
text_hipotese.resize(60, 20)

result_hipotese = QLabel("", janela)
result_hipotese.move(70, 110)
result_hipotese.resize(60, 20)

botao = QPushButton("Importar CSV", janela)
botao.move(20, 140)

resultado = QLabel("", janela)
resultado.move(20, 180)
resultado.resize(120,20)

diferenca = QLabel("", janela)
diferenca.move(20, 210)
diferenca.resize(260,20)

def onClickedBotao():
    fileDialog = QFileDialog()
    nome_arquivo, tipo_arquivo = fileDialog.getOpenFileName(
        filter="Comma Separated Values (*.csv)")
    if nome_arquivo != "":
        res_sus = calcular_sus(nome_arquivo)
        resultado.setText("Resultado: " + str(res_sus) + " pontos")
        diferenca.setText(
            "Diferença entre o Resultado e a Hipótese: "+ str( 
                round(res_sus - slider.value(),2) ) + " pontos")

botao.clicked.connect(onClickedBotao)

def onSliderChanged():
    result_hipotese.setText(str(slider.value()) + " pontos")
    resultado.setText("")
    diferenca.setText("")

slider.valueChanged.connect(onSliderChanged)

onSliderChanged()
janela.show()

aplicacao.exec_()
sys.exit()
