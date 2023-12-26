from PIL import Image

# Função para carregar as imagens de acordo com o padrão fornecido
def carregar_imagens(prefixo):
    imagens = []
    for i in range(1, 6):
        caminho = f"C:/Users/mathe/OneDrive/Programação/Python/Projeto/BMC.py/{prefixo}{i}.png"
        imagem = Image.open(caminho)
        imagens.append(imagem)
    return imagens

# Carregando as imagens correspondentes aos diferentes prefixos
imagens_prefixo1 = carregar_imagens("imagem1_")
imagens_prefixo2 = carregar_imagens("imagem2_")
imagens_prefixo3 = carregar_imagens("imagem3_")
imagens_prefixo4 = carregar_imagens("imagem4_")
imagens_prefixo5 = carregar_imagens("imagem5_")

# Função para encontrar e sobrepor as imagens baseadas nos valores de entrada
def sobrepor_imagens_por_prefixo(valores, imagens):
    imagens_selecionadas = []
    indice = 1
    for valor in valores:
        if valor == 1:
            if indice <= len(imagens):
                imagens_selecionadas.append(imagens[indice - 1])
        indice += 1

    return imagens_selecionadas

# Função para solicitar valores para cada conjunto de imagens
def solicitar_valores_e_combinar(imagens, prefixo):
    valor_input = input(f"Insira os valores (0 e 1 separados por espaços) para as imagens {prefixo}: ")
    valores = list(map(int, valor_input.split()))

    return sobrepor_imagens_por_prefixo(valores, imagens)

# Obtendo os valores para cada conjunto de imagens
valores_combinados = []
valores_combinados.extend(solicitar_valores_e_combinar(imagens_prefixo1, "imagem1_"))
valores_combinados.extend(solicitar_valores_e_combinar(imagens_prefixo2, "imagem2_"))
valores_combinados.extend(solicitar_valores_e_combinar(imagens_prefixo3, "imagem3_"))
valores_combinados.extend(solicitar_valores_e_combinar(imagens_prefixo4, "imagem4_"))
valores_combinados.extend(solicitar_valores_e_combinar(imagens_prefixo5, "imagem5_"))

# Combinando todas as imagens selecionadas
img_combinada = valores_combinados[0].copy()
for img in valores_combinados[1:]:
    img_combinada.paste(img, (0, 0), img)

# Exibindo a imagem final sobreposta
img_combinada.show()
