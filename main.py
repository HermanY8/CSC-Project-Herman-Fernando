import pygame
import class_file

WIDTH, HEIGHT = 1000, 800  # Setting width and height of our game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Screen that we created
pygame.display.set_caption("Clicks") # The main at the top of the window of our game
pygame.init() # Initializes Pygame modules which will be used in our program


BG = pygame.transform.scale(pygame.image.load("Race_Track.jpg"), (WIDTH, HEIGHT))  # Scaling background image to fit on the screen

def intro_screen():
    intro_image = pygame.image.load("intro background .jpg")
    image_intro = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))

    font = pygame.font.SysFont("Comic Sans MS", 40)
    input_box = pygame.Rect(300,136,400,70)
    color_active = pygame.Color("black")
    color_inactive = pygame.Color("black")
    color = color_inactive

    active = False
    player_name = ""

    text_to_display_enter_name = font.render("Enter your name:", True, color)
    position_of_text = (input_box.x, input_box.y -50)


    waiting = True
    while waiting:
        WIN.blit(image_intro, (0, 0))

        WIN.blit(text_to_display_enter_name, position_of_text)
        pygame.draw.rect(WIN, color, input_box, 5)

        text_surface = font.render(player_name, True, color_active)
        WIN.blit(text_surface, (input_box.x+10, input_box.y+10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                    print("name entered")
                else:
                    active = False
                    color = color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(f"Player Name: {player_name}")
                        waiting = False

                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode

    WIN.blit(BG, (0, 0))
    pygame.display.update()
    pygame.time.delay(0)

    return player_name

player_name = intro_screen()


user_name = class_file.Player(player_name)


velocity_of_car = .7 # This is the amount of space the car covers per click

cps = 0 # Clicks per second
num = 0 # Number of clicks

game_started = False  # Used to keep track of whether the game has started or not
last_time = pygame.time.get_ticks()  # Stores the time in ms

# Updates the score based on the amount of clicks per second
def cps2(score, time_left):
    global  cps, num, last_time
    if time_left > 0:  # Makes sure there is still time left on the timer
        # Calculates the time difference between calls of pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        time_diff = (current_time - last_time) // 1000.0

        # If the time difference is 1 second (1 second has passed), then calculate the CPS, set last_time to current_time,
        # and update current score/high score accordingly
        if time_diff >= 1:
            cps = num / time_diff
            cps = int(cps)
            last_time = current_time
            score.update_current_score(cps)
            score.update_high_score(score.current_score)
            num = 0
    else:
        pass

# Increases the number of clicks by 1
def addcps():
    global num
    num += 1

#sizes down the image used as the button because it was too big
start_img = pygame.image.load("New Start Button.png").convert_alpha() # the start button image
restart_image = pygame.image.load("Restart.png").convert_alpha() # the restart button image

#calls the button class in order to give its position/ its instance for both the start and restart image
start_button = class_file.Button(370, 200, start_img, 0.2)
restart_button = class_file.Button(350, 288, restart_image, 0.3)

def draw(car, score, game_time):
    global game_started
    WIN.blit(BG, (0, 0))  # Draws the background image at coordinates (0, 0) (top left) on the game window
    user_name.draw(WIN)
    car.draw(WIN)  # Displays the car object on the game window
    score.draw(WIN)  # Displays the high score and current score on the game window
    game_time.draw(WIN) # Displays the time in the window

    # Checks if button has been pressed. If it has been pressed it removes it from the window and resets the
    # score, timer, and car position.
    if not game_started:
        if start_button.draw(WIN):
            print("START")
            score.reset_current_score()
            game_started = True
            game_time.reset_timer()
            car.reset_position()

    if game_started and game_time.time == 0:
        if restart_button.draw(WIN):
            print("RESTART")
            game_started = False
            car.reset_position()
            score.reset_current_score()
            game_time.reset_timer()


    pygame.display.update() # Shows any changes made to the window display


def main():
    global game_started

    car = class_file.Car() # Creates Car object
    score = class_file.Score()  # Creates a Score object
    game_time = class_file.Time()  # Creates a time object

    run = True

    # Making a while loop to make sure that our window stays open and the game runs unless the x-button is pressed
    while run:
        # Looking at when user presses x-button to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        # If the game has started and there is still time remaining, a press of the space bar will increase the CPS
            if game_started and game_time.time > 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        addcps()

        # Call to draw() function, which contains all draw() methods from each the Car, Score, and Time classes. It also
        # handles the game_started state.
        draw(car, score, game_time)

        # Handles the movement of the car based on the number of presses on the space bar
        keys = pygame.key.get_pressed()
        if game_started and game_time.time > 0:
            if keys [pygame.K_SPACE] and car.position.x + velocity_of_car + car.width <= WIDTH:
                car.position.x += velocity_of_car

        # If the game has started, the score will be updated based on CPS and the timer will start counting down.
        if game_started:
            cps2(score, game_time.time)
            game_time.update_time()

    pygame.quit() # Shuts down all Pygame modules and closes window

if __name__ == "__main__": # makes sure we are running file and not importing it from a different file
    main()