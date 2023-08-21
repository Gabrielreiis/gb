import os

def clean_lines(input_file_path):
    try:
        # Extrair o nome do arquivo sem extensão
        project_name = os.path.splitext(os.path.basename(input_file_path))[0]

        # Criar uma pasta para o projeto, se ela não existir
        os.makedirs(project_name, exist_ok=True)

        # Ler as linhas do arquivo de entrada
        with open(input_file_path, "r", encoding="utf-8") as f:
            input_data = f.read()

        # Dividir as linhas e manter apenas a parte antes do primeiro espaço
        cleaned_lines = [line.split(" ")[0] for line in input_data.split("\n")]

        # Juntar as linhas limpas em uma string
        cleaned_data = "\n".join(cleaned_lines)

        # Criar o caminho para o arquivo de saída
        output_file_path = os.path.join(project_name, f"{project_name}_limpo.txt")

        # Escrever os resultados limpos no novo arquivo txt
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(cleaned_data)

        print(f"As linhas limpas foram salvas no arquivo: {output_file_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    input_file_path = input("Digite o caminho do arquivo de entrada (txt): ")

    if os.path.exists(input_file_path):
        clean_lines(input_file_path)
    else:
        print("Arquivo de entrada não encontrado.")

if __name__ == "__main__":
    main()
