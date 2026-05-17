import pygame
import pyttsx3
import random

pygame.init()

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rustige Praat App")

font = pygame.font.SysFont("arial", 30)
small_font = pygame.font.SysFont("arial", 22)
clock = pygame.time.Clock()

engine = pyttsx3.init()
voices = engine.getProperty("voices")

voice_modes = {
    "meisje": 0,
    "jongen": 1,
    "man": 2,
    "vrouw": 3,
}

current_voice = "vrouw"
current_mode = "lief"
user_text = ""
response_text = ""

lief_antwoorden = [
    "Het komt goed ❤️",
    "Adem rustig in en uit.",
    "Je bent niet alleen.",
    "Ik luister naar je."
]

boos_antwoorden = [
    "Kom op nou!!",
    "Dit laat je niet zomaar los!",
    "Laat je niet kennen.",
    "Zet door, ook al is het zwaar."
]

scheldwoord_antwoorden = [
    "Sukkel, wat ben je aan het doen?!",
    "Ben je helemaal gek geworden?!",
    "Doe even normaal, mafkees!",
    "Wakker worden, sukkel!"
]


def set_voice(voice_name):
    index = voice_modes.get(voice_name, 0)
    if 0 <= index < len(voices):
        engine.setProperty("voice", voices[index].id)
    elif voices:
        engine.setProperty("voice", voices[0].id)


def praat(text):
    set_voice(current_voice)
    engine.say(text)
    engine.runAndWait()


def krijg_antwoord():
    global response_text
    if current_mode == "lief":
        response_text = random.choice(lief_antwoorden)
    elif current_mode == "boos":
        response_text = random.choice(boos_antwoorden)
    else:
        response_text = random.choice(scheldwoord_antwoorden)
    praat(response_text)

running = True
while running:
    screen.fill((30, 30, 40))

    title = font.render("Rustige Praat App", True, (255, 255, 255))
    screen.blit(title, (300, 20))

    mode_text = small_font.render(f"Mode: {current_mode}", True, (200, 200, 255))
    screen.blit(mode_text, (50, 100))

    voice_text = small_font.render(f"Stem: {current_voice}", True, (200, 255, 200))
    screen.blit(voice_text, (50, 140))

    pygame.draw.rect(screen, (255, 255, 255), (50, 220, 800, 50), 2)
    input_surface = small_font.render(user_text, True, (255, 255, 255))
    screen.blit(input_surface, (60, 230))

    response_surface = font.render(response_text, True, (255, 200, 100))
    screen.blit(response_surface, (50, 350))

    uitleg = [
        "Typ iets en druk ENTER",
        "1 = lief",
        "2 = boos",
        "3 = scheldwoorden",
        "4 = meisje",
        "5 = jongen",
        "6 = man",
        "7 = vrouw",
        "ESC = sluit app"
    ]

    y = 450
    for line in uitleg:
        txt = small_font.render(line, True, (180, 180, 180))
        screen.blit(txt, (50, y))
        y += 28

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                krijg_antwoord()
                user_text = ""
            elif event.key == pygame.K_1:
                current_mode = "lief"
            elif event.key == pygame.K_2:
                current_mode = "boos"
            elif event.key == pygame.K_3:
                current_mode = "scheldwoorden"
            elif event.key == pygame.K_4:
                current_voice = "meisje"
            elif event.key == pygame.K_5:
                current_voice = "jongen"
            elif event.key == pygame.K_6:
                current_voice = "man"
            elif event.key == pygame.K_7:
                current_voice = "vrouw"
            else:
                user_text += event.unicode

    clock.tick(60)

pygame.quit()
