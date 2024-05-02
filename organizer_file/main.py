import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione a pasta para organizar")

lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Documentos": [".pdf", ".docx", ".xlsx", ".txt", ".pptx"],
    "Executaveis": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Audios": [".mp3", ".wav", ".flac", ".wma"],
    "Outros": [
        ".py",
        ".c",
        ".cpp",
        ".java",
        ".html",
        ".css",
        ".js",
        ".php",
        ".json",
        ".xml",
        ".yml",
        ".yaml",
        ".md",
    ],

}

for arquivo in lista_arquivos:
    for local, extensoes in locais.items():
        if arquivo.endswith(tuple(extensoes)):
            if not os.path.exists(os.path.join(caminho, local)):
                os.mkdir(os.path.join(caminho, local))
            os.rename(
                os.path.join(caminho, arquivo),
                os.path.join(caminho, local, arquivo),
            )
            break
    else:
        if not os.path.exists(os.path.join(caminho, "Outros")):
            os.mkdir(os.path.join(caminho, "Outros"))
        os.rename(
            os.path.join(caminho, arquivo),
            os.path.join(caminho, "Outros", arquivo),
        )
print("Organização concluída")