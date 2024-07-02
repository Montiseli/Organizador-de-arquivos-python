import os
from tkinter.filedialog import askdirectory
#Variavel para mostrar um caminho para algum arquivo
caminho = askdirectory(title="Selecione uma pasta")
#Variavel para dizer todos arquivos que estão neste caminho
lista_arquivos = os.listdir(caminho)
#Variavel que decide para qual pasta e quais arquivos serao organizados
locais = {
    "imagens":[".jpg", ".png", ".jfif" ],
    "planilhas":[".xlsx"],
    "pdf":[".pdf"],
    "csv":[".csv"]
}

for arquivo in lista_arquivos:
    #A variavel nome é o nome do arquivo, e a extencao é o tipo do arquivo ex:.pdf, .png
    nome, extensao = os.path.splitext(f"{caminho}q{arquivo}")

#Verificando se as extencoens estao dentro das pastas/locais
    for pasta in locais:
        if extensao in locais[pasta]:
            #Verificando se a pasta selecionada ja possui uma pasta separando os arquivos, se não houver, irá criar uma
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
                #Movendo o arquivo para a nova pasta criada
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

print("Seus arquivos foram organizados com sucesso!")