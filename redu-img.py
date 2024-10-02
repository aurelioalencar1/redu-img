from PIL import Image
import os

# Função para converter imagem para WebP com ajuste de qualidade
def converter_para_webp(nome_arquivo, pasta_origem, pasta_destino, tamanho_maximo_kb):
    # Abrir a imagem original
    imagem = Image.open(os.path.join(pasta_origem, nome_arquivo))

    # Definir o nome do arquivo de destino sem a extensão
    nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]

    # Converter para WebP com ajuste de qualidade para alcançar o tamanho máximo desejado
    quality = 85  # Exemplo inicial de qualidade, ajuste conforme necessário
    while True:
        # Salvar a imagem como WebP com a qualidade atual
        imagem.save(os.path.join(pasta_destino, f"{nome_arquivo_sem_extensao}.webp"), "WEBP", quality=quality)

        # Verificar o tamanho do arquivo
        tamanho_arquivo = os.path.getsize(os.path.join(pasta_destino, f"{nome_arquivo_sem_extensao}.webp"))
        tamanho_arquivo_kb = tamanho_arquivo / 1024  # Converter para KB

        # Verificar se o tamanho do arquivo está dentro do limite desejado
        if tamanho_arquivo_kb <= tamanho_maximo_kb:
            print(f"Imagem {nome_arquivo} convertida para WebP com qualidade {quality} e tamanho {tamanho_arquivo_kb:.2f} KB")
            break
        else:
            # Reduzir a qualidade e tentar novamente
            quality -= 5
            if quality < 10:
                # Se a qualidade ficar muito baixa, ajustar o método de controle
                print(f"Aviso: A qualidade está muito baixa para atingir o tamanho máximo de {tamanho_maximo_kb} KB.")
                break

# Função principal para percorrer arquivos na pasta de origem
def main():
    pasta_origem = r"/home/devlinux/pasta-python/redu-img/img-4k"  # Substitua pelo caminho da sua pasta de origem
    pasta_destino = r"/home/devlinux/pasta-python/redu-img/img"  # Substitua pelo caminho da sua pasta de destino
    tamanho_maximo_kb = 290  # Tamanho máximo desejado em KB

    # Verificar se a pasta de destino existe, senão criar
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Percorrer todos os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        try:
            # Processar apenas arquivos de imagem
            if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(f"Processando {nome_arquivo}...")
                converter_para_webp(nome_arquivo, pasta_origem, pasta_destino, tamanho_maximo_kb)
        except Exception as e:
            print(f"Erro ao processar {nome_arquivo}: {str(e)}")

if __name__ == "__main__":
    main()
