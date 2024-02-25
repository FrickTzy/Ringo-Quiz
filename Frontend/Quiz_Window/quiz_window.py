from pygame import draw, Rect, image, transform
import sys
from Backend import AnimeCharacterImageRetriever, AnimeCharacterSearcher
from Frontend.Helper_Files import Display
from Frontend.Settings import Colors
from io import BytesIO


font = pygame.font.Font(None, 36)
question_font = pygame.font.Font(None, 48)

# Quiz data
questions = ["What is the capital of France?",
             "Who painted the Mona Lisa?",
             "What is the powerhouse of the cell?"]

answers = [["Paris", "London", "Berlin", "Rome"],
           ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
           ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic reticulum"]]

correct_answers = [0, 0, 0]

# Variables
current_question = 0
score = 0

# Button properties
BUTTON_HEIGHT = 100
BUTTON_MARGIN = 20
BUTTON_START_Y = SCREEN_HEIGHT // 2
BUTTON_WIDTH = (SCREEN_WIDTH - 5 * BUTTON_MARGIN) // 4

button_colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW]

ANIME_TITLE = "Bleach"
ANIME_CHARACTER = AnimeCharacterSearcher().get_random_character(anime_title=ANIME_TITLE)
response = AnimeCharacterImageRetriever().retrieve_image(anime_title=ANIME_TITLE, character_name=ANIME_CHARACTER)
img = image.load(BytesIO(response.content))
img = transform.scale(img, (200, 150))


class QuizWindow:
    __running = True

    def __init__(self, display: Display):
        self.__display = display

    def draw_buttons(self):
        for i, color in enumerate(button_colors):
            button_rect = Rect((BUTTON_WIDTH + BUTTON_MARGIN) * i + BUTTON_MARGIN, BUTTON_START_Y, BUTTON_WIDTH,
                               BUTTON_HEIGHT)
            draw.rect(self.__display.window, color, button_rect)
            answer_text = font.render(answers[current_question][i], True, Colors.BLACK)
            answer_rect = answer_text.get_rect(center=button_rect.center)
            self.__display.window.blit(answer_text, answer_rect)

    def run(self):
        while self.__running:
            self.__display.window.fill(Colors.WHITE)
            self.__display.window.blit(img, (0, 0))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, color in enumerate(button_colors):
                        button_rect = pygame.Rect((BUTTON_WIDTH + BUTTON_MARGIN) * i + BUTTON_MARGIN, BUTTON_START_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
                        if button_rect.collidepoint(mouse_pos):
                            if i == correct_answers[current_question]:
                                score += 1
                            current_question += 1
                            if current_question == len(questions):
                                running = False

            # Display question
            if current_question < len(questions):
                question_text = question_font.render(questions[current_question], True, BLACK)
                question_rect = question_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
                screen.blit(question_text, question_rect)

                # Draw buttons
                draw_buttons()

            # Display score
            score_text = font.render(f"Score: {score}/{len(questions)}", True, BLACK)
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-50))
            screen.blit(score_text, score_rect)

            pygame.display.flip()

pygame.quit()
sys.exit()
