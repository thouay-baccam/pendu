import pygame
import os
import random
import sys

# Initialisation de Pygame
pygame.init()

# Déclaration des constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Déclaration des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialisation de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# Charger les images du pendu
pendu_images = [pygame.image.load(os.path.join("penduimg", f"pendu{i}.png")) for i in range(1, 6)]
winner_image = pygame.image.load(os.path.join("penduimg", "winner.png"))

# Charger les mots depuis le fichier mots.txt
with open("mots.txt", "r") as file:
    mots = [mot.strip().lower() for mot in file.readlines()]

# Pour afficher le mot a la fin (game over)
mot_a_deviner_actuel = ""

# Fonction pour choisir un mot aléatoire
def choisir_mot():
    return random.choice(mots)

# Fonction pour afficher le mot avec des espaces entre les lettres
def afficher_mot(mot, lettres_decouvertes):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_decouvertes:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage.strip()

# Fonction pour afficher le fond d'écran du menu principal
def afficher_fond_menu_principal():
    # Charger l'image de fond pour le menu principal
    fond_menu_principal = pygame.image.load(os.path.join("penduimg", "bgmenu.png"))
    screen.blit(fond_menu_principal, (0, 0))

# Fonction pour afficher le menu principal
def afficher_menu_principal():
    afficher_fond_menu_principal()

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Menu Principal", True, BLACK)
    screen.blit(titre_texte, (SCREEN_WIDTH // 2 - titre_texte.get_width() // 2, 50))

    font = pygame.font.Font(None, 36)

    # Bouton "Jouer"
    jouer_rect = pygame.Rect(250, 200, 300, 50)
    pygame.draw.rect(screen, GRAY, jouer_rect)
    jouer_texte = font.render("Jouer au Pendu", True, BLACK)
    screen.blit(jouer_texte, (jouer_rect.centerx - jouer_texte.get_width() // 2, jouer_rect.centery - jouer_texte.get_height() // 2))

    # Bouton "Ajouter un mot"
    ajouter_rect = pygame.Rect(250, 300, 300, 50)
    pygame.draw.rect(screen, GRAY, ajouter_rect)
    ajouter_texte = font.render("Ajouter un mot", True, BLACK)
    screen.blit(ajouter_texte, (ajouter_rect.centerx - ajouter_texte.get_width() // 2, ajouter_rect.centery - ajouter_texte.get_height() // 2))

    # Bouton "Quitter"
    quitter_rect = pygame.Rect(250, 400, 300, 50)
    pygame.draw.rect(screen, GRAY, quitter_rect)
    quitter_texte = font.render("Quitter", True, BLACK)
    screen.blit(quitter_texte, (quitter_rect.centerx - quitter_texte.get_width() // 2, quitter_rect.centery - quitter_texte.get_height() // 2))

    pygame.display.flip()

    return jouer_rect, ajouter_rect, quitter_rect

# Fonction pour afficher le fond d'écran du menu ajout de mot
def afficher_fond_ajout_mot():
    # Charger l'image de fond pour le menu ajout de mot
    fond_ajout_mot = pygame.image.load(os.path.join("penduimg", "bgmots.png"))
    screen.blit(fond_ajout_mot, (0, 0))

# Fonction pour ajouter un mot au fichier mots.txt
def ajouter_mot():
    afficher_fond_ajout_mot()

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Ajouter un Mot", True, BLACK)
    screen.blit(titre_texte, (SCREEN_WIDTH // 2 - titre_texte.get_width() // 2, 50))

    font = pygame.font.Font(None, 36)

    input_rect = pygame.Rect(250, 200, 300, 50)
    pygame.draw.rect(screen, GRAY, input_rect)
    input_texte = font.render("", True, BLACK)
    screen.blit(input_texte, (input_rect.centerx - input_texte.get_width() // 2, input_rect.centery - input_texte.get_height() // 2))

    ajouter_rect = pygame.Rect(250, 300, 300, 50)
    pygame.draw.rect(screen, GRAY, ajouter_rect)
    ajouter_texte = font.render("Ajouter", True, BLACK)
    screen.blit(ajouter_texte, (ajouter_rect.centerx - ajouter_texte.get_width() // 2, ajouter_rect.centery - ajouter_texte.get_height() // 2))

    pygame.display.flip()

    input_active = True
    input_text = ""
    clock = pygame.time.Clock()

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(WHITE)
        screen.blit(titre_texte, (SCREEN_WIDTH // 2 - titre_texte.get_width() // 2, 50))

        pygame.draw.rect(screen, GRAY, input_rect)
        input_texte = font.render(input_text, True, BLACK)
        screen.blit(input_texte, (input_rect.centerx - input_texte.get_width() // 2, input_rect.centery - input_texte.get_height() // 2))

        pygame.draw.rect(screen, GRAY, ajouter_rect)
        screen.blit(ajouter_texte, (ajouter_rect.centerx - ajouter_texte.get_width() // 2, ajouter_rect.centery - ajouter_texte.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

    if input_text:
        with open("mots.txt", "a") as file:
            if file.tell() != 0:
                file.write("\n")  # Ajouter une nouvelle ligne seulement si le fichier n'est pas vide
            file.write(input_text)

# Fonction pour afficher le fond d'écran du jeu
def afficher_fond_jeu():
    # Charger l'image de fond pour le jeu
    fond_jeu = pygame.image.load(os.path.join("penduimg", "bgjeu.png"))
    screen.blit(fond_jeu, (0, 0))

# Fonction pour afficher le mot avec des espaces entre les lettres
def afficher_victoire():
    afficher_fond_jeu()

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Félicitations!", True, BLACK)
    screen.blit(titre_texte, (SCREEN_WIDTH // 2 - titre_texte.get_width() // 2, 50))

    # Charger l'image spécifique pour l'écran de victoire
    screen.blit(winner_image, (SCREEN_WIDTH // 2 - winner_image.get_width() // 2, 150))

    pygame.display.flip()

    pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter

# Fonction principale du jeu
def jouer():
    global mot_a_deviner_actuel  

    afficher_fond_jeu()
    
    mot_a_deviner = choisir_mot().lower()
    mot_a_deviner_actuel = mot_a_deviner 
    lettres_decouvertes = set()
    erreurs = 0

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    lettre = chr(event.key).lower()
                    if lettre not in lettres_decouvertes:
                        lettres_decouvertes.add(lettre)
                        if lettre not in mot_a_deviner:
                            erreurs += 1

        screen.fill(WHITE)

        # Afficher le mot
        font = pygame.font.Font(None, 36)
        mot_affiche = font.render(afficher_mot(mot_a_deviner, lettres_decouvertes), True, BLACK)
        screen.blit(mot_affiche, (SCREEN_WIDTH // 2 - mot_affiche.get_width() // 2, 50))

        # Afficher l'image du pendu correspondante
        if erreurs < 5:
            screen.blit(pendu_images[erreurs], (SCREEN_WIDTH // 2 - pendu_images[erreurs].get_width() // 2, 150))
        else:
            afficher_mot_correct()  # Afficher le mot correct en cas de défaite
            pygame.display.flip()
            pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter
            return

        pygame.display.flip()

        # Vérifier la condition de victoire/défaite
        if set(mot_a_deviner) <= lettres_decouvertes or erreurs >= 5:
            afficher_victoire() if set(mot_a_deviner) <= lettres_decouvertes else pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter
            running = False

        clock.tick(FPS)

# Fonction pour afficher le mot correct en cas de défaite
def afficher_mot_correct():
    afficher_fond_jeu()

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Dommage!", True, BLACK)
    screen.blit(titre_texte, (SCREEN_WIDTH // 2 - titre_texte.get_width() // 2, 50))

    font = pygame.font.Font(None, 36)

    mot_correct_texte = font.render(f"Le mot était : {mot_a_deviner_actuel}", True, BLACK)
    screen.blit(mot_correct_texte, (SCREEN_WIDTH // 2 - mot_correct_texte.get_width() // 2, 200))

    pygame.display.flip()

# Fonction pour afficher le menu principal
def menu_principal():
    jouer_rect, ajouter_rect, quitter_rect = afficher_menu_principal()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if jouer_rect.collidepoint(mouse_pos):
                    jouer()
                    afficher_menu_principal()
                elif ajouter_rect.collidepoint(mouse_pos):
                    ajouter_mot()
                    afficher_menu_principal()
                elif quitter_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

# Lancer le menu principal
menu_principal()