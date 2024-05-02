import PyPDF2
import os
from tkinter.filedialog import askdirectory

# Inicializar o mesclador de PDF
merger = PyPDF2.PdfMerger()

# Pedir ao usuário para selecionar o diretório
caminho = askdirectory(title="Selecione a pasta para juntar PDF")
if not caminho:
    print("Nenhum diretório selecionado. Operação cancelada.")
    exit()

# Listar e ordenar os arquivos no diretório
lista_arquivos = sorted([f for f in os.listdir(caminho) if f.lower().endswith('.pdf')])
print("Arquivos a serem mesclados:", lista_arquivos)
print("Diretório atual:", os.getcwd())

# Processar cada arquivo
for arquivo in lista_arquivos:
    try:
        filepath = os.path.join(caminho, arquivo)
        merger.append(filepath)
        print(f"Adicionado: {arquivo}")
    except PyPDF2.errors.PdfReadError as e:
        print(f"Erro ao ler o arquivo {arquivo}: {e}")
    except Exception as e:
        print(f"Erro desconhecido com o arquivo {arquivo}: {e}")

# Escrever o PDF mesclado
output_path = os.path.join(caminho, "merge_file.pdf")
merger.write(output_path)
merger.close()

print(f"Merge concluído. Arquivo salvo em {output_path}")
