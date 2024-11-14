import tkinter as tk
from tkinter import messagebox

# Função para converter a palavra
def converter_palavra():
    palavra = entrada_palavra.get()  # Obter a palavra digitada
    palavra_minuscula = palavra.lower()  # Converter para minúsculas
    palavra_maiuscula = palavra.upper()  # Converter para maiúsculas
    
    # Exibir o resultado em labels na interface
    resultado_min["text"] = f"Minúsculas: {palavra_minuscula}"
    resultado_mai["text"] = f"Maiúsculas: {palavra_maiuscula}"

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Palavra")
janela.geometry("400x300")
janela.configure(bg="#ADD8E6")  # Cor de fundo azul-claro

# Título da aplicação
titulo = tk.Label(janela, text="Conversor de Letras", font=("Arial", 18, "bold"), bg="#4682B4", fg="white")
titulo.pack(pady=10, fill="x")

# Entrada de texto
entrada_label = tk.Label(janela, text="Digite uma palavra:", font=("Arial", 12), bg="#ADD8E6")
entrada_label.pack(pady=5)
entrada_palavra = tk.Entry(janela, font=("Arial", 12), width=30)
entrada_palavra.pack(pady=5)

# Botão para converter a palavra
botao_converter = tk.Button(janela, text="Converter", font=("Arial", 12, "bold"), bg="#32CD32", fg="white", command=converter_palavra)
botao_converter.pack(pady=15)

# Resultados das conversões
resultado_min = tk.Label(janela, text="", font=("Arial", 12), bg="#ADD8E6", fg="#333333")
resultado_min.pack(pady=5)

resultado_mai = tk.Label(janela, text="", font=("Arial", 12), bg="#ADD8E6", fg="#333333")
resultado_mai.pack(pady=5)

# Executa o programa
janela.mainloop()
