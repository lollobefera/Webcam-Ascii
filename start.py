import cv2, os
import numpy as np
import pygame
from time import sleep
black = (0, 0, 0)
white = (255, 255, 255)


title = 'Webcam-Ascii'
font_path = 'C:\\Windows\\Fonts\\verdana.ttf'
fps = 60
lines = 120
cols = 150
distanza_caratteri = 8
inverti_colori = False # (nero su bianco)
backgroud = black # colore background (R, G, B)
foreground = white # colore foreground (R, G, B)

char_list = '$@BM#ZXzcft/|(}]?*-_+~<;:,"^\'`.    '
char_list = char_list[::-1]

pygame.init()
# configurazione pygame
root = pygame.display.set_mode((cols * distanza_caratteri, lines * distanza_caratteri))
pygame.display.set_caption(title)
font1 = pygame.font.Font(font_path, 10)

image = np.ndarray(shape = (lines, cols)).tolist() # crea un'array per i caratteri ascii
cam = cv2.VideoCapture(0)

if inverti_colori:
	char_list = char_list[::-1]
	background = white
	foreground = black

def save(): #salva uno screen dell'ascii art
	name = 1
	while os.path.isfile(f'Ascii{name}.jpg'): 
		name += 1
	filename = f'Ascii{name}.jpg'

	rect = pygame.Rect(0, 0, cols * distanza_caratteri, lines * distanza_caratteri)
	sub = root.subsurface(rect)
	pygame.image.save(sub, filename)

def update():
    pygame.display.update()
    pygame.time.Clock().tick(fps)
    root.fill(background)

def Ascii(lum): # ritorna l'index del carattere corrispondente all'intensità del colore
	carattere = lum / 255
	carattere = round(carattere * (len(char_list)-1))
	carattere = char_list[carattere]
	return str(carattere)

def draw_ascii(frame): # disegna i caratteri nella finestra pygame
	X, Y = 0, 0
	for line in frame:
		Y += distanza_caratteri
		for pixel in line:
			X += distanza_caratteri
			luminosita = sum(pixel) / len(pixel) # fa la media tra i valori (B, G, R) di ogni pixel
			char = Ascii(luminosita)
			char = font1.render(char, True, foreground)
			root.blit(char, (X, Y))
		X = 0

def main():
	_, frame = cam.read()
	frame = cv2.flip(frame, 1)
	frame1 = cv2.resize(frame, (cols, lines)) # riduce la qualità del frame
	draw_ascii(frame1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_s]:
			save()
	update()

if __name__ == '__main__':
	while True:
		main()