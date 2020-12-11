# Transformação Gamma

from PIL import Image

# Abrir a imagem
img = Image.open('panda.jpg')

# Carregar a imagem para matriz
matrix = img.load()

# Realizar as operações pixel a pixel de transformação.
gamma = 2
for i in range(img.size[0]):
  for j in range(img.size[1]):
    r = int((matrix[i,  j][0]/255) ** gamma  * 255)
    g = int((matrix[i,  j][1]/255) ** gamma  * 255)
    b = int((matrix[i,  j][2]/255) ** gamma  * 255)
    matrix[i,  j] = (r, g, b)

# Salvar a imagem 
img.save('pandagamma2.jpg')