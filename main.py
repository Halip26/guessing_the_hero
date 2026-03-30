import pygame
import sys
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tebak Superhero")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 48)

# Daftar superhero (nama + file gambar)
superheroes = [
    ("Batman", "batman.png"),
    ("Superman", "superman.png"),
    ("Iron Man", "ironman.png"),
    ("Spider-Man", "spiderman.png"),
]

# Load gambar
images = []
for name, file in superheroes:
    img = pygame.image.load(file)
    img = pygame.transform.scale(img, (150, 200))  # resize biar seragam
    images.append((name, img))

# Pilih jawaban benar secara acak
correct_superhero = random.choice(superheroes)[0]


def draw_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def main():
    running = True
    result_message = ""

    while running:
        screen.fill(WHITE)

        # Tampilkan pertanyaan
        draw_text(f"Tebak: {correct_superhero}", 50, 50)

        # Tampilkan gambar berjajar
        spacing = 50
        start_x = 50
        y_pos = 200
        rects = []

        for i, (name, img) in enumerate(images):
            x_pos = start_x + i * (150 + spacing)
            rect = pygame.Rect(x_pos, y_pos, 150, 200)
            screen.blit(img, (x_pos, y_pos))
            rects.append((rect, name))

        # Tampilkan hasil jika ada
        if result_message:
            draw_text(result_message, 50, 500, (0, 128, 0))

        pygame.display.flip()

        # Event handling
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
                        else:
                            result_message = f"Salah! Itu {name}."


if __name__ == "__main__":
    main()
