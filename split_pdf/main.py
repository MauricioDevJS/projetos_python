import PyPDF2
import os
from tkinter.filedialog import askopenfilename

# Pedir ao usuário para selecionar o arquivo PDF
caminho_arquivo = askopenfilename(title="Selecione o arquivo PDF", filetypes=[("PDF files", "*.pdf")])
if not caminho_arquivo:
    print("Nenhum arquivo selecionado. Operação cancelada.")
    exit()

# Abrir o arquivo PDF original
pdf_file = open(caminho_arquivo, "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Criar um arquivo PDF para cada página
output_folder = os.path.dirname(caminho_arquivo)
for i in range(len(pdf_reader.pages)):
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(pdf_reader.pages[i])
    
    output_filename = os.path.join(output_folder, f"page_{i+1}.pdf")
    with open(output_filename, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Página {i+1} salva como {output_filename}")

# Fechar o arquivo PDF original
pdf_file.close()
print("Processo concluído. Cada página foi salva como um arquivo separado.")
