# Simon says

import pygame
import sys
import random

# inisialisasi pygame
pygame.init()

# ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tebak Superhero")

# warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

# font
font = pygame.font.SysFont(None, 48)

# daftar superhero (nama + file gambar)
superheroes = [
    ("Kaya raya yg baik hati", "heroes/batman.png"),
    ("Menyamar menjadi jurnalis", "heroes/superman.png"),
    ("Millioner pake baju besi", "heroes/ironman.png"),
    ("Merayap di dinding", "heroes/spiderman.png"),
    ("Dewa petir dari khayangan", "heroes/thor.png"), 
]

# load gambar
images = []
for name, file in superheroes:
    img = pygame.image.load(file)
    img = pygame.transform.scale(img, (100, 150))  # resize biar seragam
    images.append((name, img))


def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def main():
    correct_superhero = random.choice(superheroes)[0]
    running = True
    result_message = ""
    result_color = BLACK

    while running:
        screen.fill(WHITE)

        # Tampilkan pertanyaan
        draw_text(f"Cluenya: {correct_superhero}", 50, 50)

        # Tampilkan gambar berjajar
        spacing = 10
        start_x = 20
        y_pos = 200
        rects = []

        for i, (name, img) in enumerate(images):
            x_pos = start_x + i * (150 + spacing)
            rect = pygame.Rect(x_pos, y_pos, 150, 200)
            screen.blit(img, (x_pos, y_pos))
            rects.append((rect, name))

        # tampilkan hasil jika ada
        if result_message:
            draw_text(result_message, 50, 500, result_color)

        pygame.display.flip()

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for rect, name in rects:
                    if rect.collidepoint(mouse_pos):
                        if name == correct_superhero:
                            result_message = "Benar! Kamu menebak dengan tepat!"
                            result_color = GREEN
                            # pilih superhero baru untuk ronde berikutnya
                            correct_superhero = random.choice(superheroes)[0]
                        else:
                            result_message = f"Salah! Itu {name}."
                            result_color = RED


if __name__ == "__main__":
    main()
