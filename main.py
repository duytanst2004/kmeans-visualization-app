import pygame
from random import randint
import math
from sklearn.cluster import KMeans

class text_btn:
	def __init__(self,text, x, y, width, height):
		self.text = text
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		# print(mouse_x, mouse_y)
		if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
			return True
		return False

	def draw(self):
		text_render = font.render(self.text, True, WHITE)
		pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))
		screen.blit(text_render, (self.x + self.width / 10, self.y + self.height / 10))

def fix(buttons):
	buttons[0].width = 40
	# Button "-"
	btn_text_minus = text_btn("-", X + 80, Y, 40, 40)
	btn_text_minus.draw()

	# Text "K"
	text_k = font.render("K = " + str(K), True, BLACK)
	screen.blit(text_k, (X + 80 * 2, Y))

	# Text "Error"
	buttons[3].width, buttons[3].height = 0, 0
	text_error = font.render("Error = " + str(Error), True, BLACK)
	screen.blit(text_error, (X, Y + 75 * 3))
	buttons.insert(1, btn_text_minus)

	return buttons

def distance(p1, p2):
	return math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]))

pygame.init()

screen = pygame.display.set_mode((16 * 70, 9 * 70))

pygame.display.set_caption("kmeans visualization")

running = True

clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRASS = (55, 155, 65)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRASS]

BACKGROUND_PANEL = (249, 255, 230)
X, Y, WIDTH, HEIGHT = 800, 50, 120, 40
P = (55, 55, 690, 490)
font = pygame.font.SysFont('sans', 28)
font_mouse = pygame.font.SysFont('sans', 14)

# text_plus, text_minus, text_k, text_run, text_random, text_error text_algorithm, text_reset
K, Error = 0, 0
points = []
clusters = []
labels = []

while running:
	clock.tick(60)
	screen.fill(BACKGROUND)

	# Draw interface

	# Draw panel

	pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
	pygame.draw.rect(screen, BACKGROUND_PANEL, P)

	# Button
	buttons = []
	btn_names = ["+", "Run", "Random", "", "Algorithm", "Reset"]
	for i in range(len(btn_names)):
		button = text_btn(btn_names[i], X, Y + i * 75, WIDTH, HEIGHT)
		buttons.append(button)

	buttons = fix(buttons)
	btn_names.insert(1, "-")
	for i in range(len(buttons)):
		buttons[i].draw()

	# End draw interface
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if P[0] < mouse_x < P[0] + P[2] and P[1] < mouse_y < P[1] + P[3]:
		text_mouse = font_mouse.render("({0}, {1})".format(mouse_x - P[0], mouse_y - P[1]), True, BLACK)
		screen.blit(text_mouse, (mouse_x + 10, mouse_y - 5))
 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button:
				if P[0] < mouse_x < P[0] + P[2] and P[1] < mouse_y < P[1] + P[3]:
					labels = []
					point = [mouse_x - P[0], mouse_y - P[1]]
					points.append(point)

				if buttons[0].is_mouse_on_text() and K < len(COLORS):
					K += 1

				if buttons[1].is_mouse_on_text() and 0 < K:
					K -= 1

				if buttons[2].is_mouse_on_text() and clusters != []:
					labels = []
					# Assign points to closet clusters
					for i in range(len(points)):
						min_distance, min_idx = distance(points[i], clusters[0]), 0
						for j in range(1, len(clusters)):
							if distance(points[i], clusters[j]) <  min_distance:
								min_distance = distance(points[i], clusters[j])
								min_idx = j
						labels.append(min_idx)

					# Update clusters
					for i in range(K):
						sum_x, sum_y, count = 0, 0, 0
						for j in range(len(points)):
							if labels[j] == i:
								sum_x += points[j][0]
								sum_y += points[j][1]
								count += 1
						if count > 0:
							new_cluster = [sum_x / count, sum_y / count]
							clusters[i] = new_cluster

				if buttons[3].is_mouse_on_text():
					clusters = []
					labels = []
					Error = 0
					for i in range(K):
						random_points = [randint(0, P[2]), randint(0, P[3])]
						clusters.append(random_points)

				try:
					if buttons[5].is_mouse_on_text():
						kmeans = KMeans(n_clusters=K, n_init=10).fit(points)
						clusters = kmeans.cluster_centers_
						print(clusters)
						labels = kmeans.predict(points)
				except:
					print("Eroor")

				if buttons[6].is_mouse_on_text():
					K = 0
					Error = 0
					points = []
					clusters = []
					labels = []

	# Draw cluster col
	for i in range(len(clusters)):
		pygame.draw.circle(screen, COLORS[i], (clusters[i][0] + P[0], clusters[i][1] + P[1]), 6)

	# Draw point
	for i in range(len(points)):
		if len(labels):
			pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + P[0], points[i][1] + P[1]), 4)
		else:
			pygame.draw.circle(screen, BLACK, (points[i][0] + P[0], points[i][1] + P[1]), 4)	
			pygame.draw.circle(screen, WHITE, (points[i][0] + P[0], points[i][1] + P[1]), 3)

	# Calculate and draw error
	if len(clusters) and len(labels):
		Error = 0
		for i in range(len(points)):
			Error += int(distance(points[i], clusters[labels[i]]))

	pygame.display.flip()

pygame.quit()