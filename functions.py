def rgb_to_gray(image):
    """
    Converte uma imagem colorida para tons de cinza.
    
    Parâmetros:
        image (list): Lista de listas representando os pixels da imagem,
                      onde cada sublista representa uma linha de pixels e
                      cada pixel é uma lista [R, G, B].
                      
    Retorna:
        list: Lista de listas representando os pixels da imagem em tons de cinza,
              onde cada sublista representa uma linha de pixels e cada pixel é
              um único valor de intensidade (de 0 a 255).
    """
    gray_image = []
    for row in image:
        gray_row = []
        for pixel in row:
            # Fórmula para converter RGB para escala de cinza: 0.2989*R + 0.5870*G + 0.1140*B
            gray_value = int(0.2989 * pixel[0] + 0.5870 * pixel[1] + 0.1140 * pixel[2])
            gray_row.append(gray_value)
        gray_image.append(gray_row)
    return gray_image

# Exemplo de uso
color_image = [
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[128, 128, 128], [64, 64, 64], [192, 192, 192]]
]

gray_image = rgb_to_gray(color_image)
for row in gray_image:
    print(row)


def rgb_to_binary(image, threshold=128):
    """
    Converte uma imagem colorida para preto e branco.
    
    Parâmetros:
        image (list): Lista de listas representando os pixels da imagem,
                      onde cada sublista representa uma linha de pixels e
                      cada pixel é uma lista [R, G, B].
        threshold (int): Limiar para converter os pixels para preto (<= threshold) ou branco (> threshold).
                         O valor padrão é 128, que está no meio da escala de intensidade de 0 a 255.
                      
    Retorna:
        list: Lista de listas representando os pixels da imagem em preto e branco,
              onde cada sublista representa uma linha de pixels e cada pixel é
              um valor binário indicando preto (0) ou branco (1).
    """
    binary_image = []
    for row in image:
        binary_row = []
        for pixel in row:
            # Calcula a intensidade média dos canais R, G e B
            intensity = (pixel[0] + pixel[1] + pixel[2]) // 3
            # Verifica se a intensidade é maior que o limiar
            if intensity <= threshold:
                binary_row.append(0)  # preto
            else:
                binary_row.append(1)  # branco
        binary_image.append(binary_row)
    return binary_image

# Exemplo de uso
color_image = [
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[128, 128, 128], [64, 64, 64], [192, 192, 192]]
]

binary_image = rgb_to_binary(color_image)
for row in binary_image:
    print(row)