import pgzrun
import random


TITLE = 'CLICKER'
WIDTH = 500
HEIGHT = 500

score = 0
time = 0

mini_button1_pressed = False
mini_button2_pressed = False
button_pressed = False

fontsz = 50
mouse_pos = (0, 0)

score_per_click = 1
score_per_second = 0

score_per_click_price = 10
score_per_second_price = 10

# Load images
pix = Actor('pixel', mouse_pos)
bg = Rect((0, 0), (WIDTH, HEIGHT))
button1 = Actor('button', (WIDTH//2, -50+HEIGHT//2))
mini_button1 = Actor('minibutton', (button1.x - 103, button1.y + 150))
mini_button2 = Actor('minibutton', (button1.x + 103, button1.y + 150))


def draw():
    pix.draw()
    screen.draw.filled_rect(bg, "#ADADAD")
    button1.draw()
    mini_button1.draw()
    mini_button2.draw()

    screen.draw.text(f'{score}',
                     center=button1.pos,
                     color='white',
                     fontsize=fontsz)
    screen.draw.text(f'{score_per_click}',
                     midleft=(mini_button1.x - 75, mini_button1.y + 55),
                     color='black',
                     fontsize=50)
    screen.draw.text(f'{score_per_second}',
                     midright=(mini_button2.x + 75, mini_button2.y + 55),
                     color='black',
                     fontsize=50)
    screen.draw.text('Double clicks',
                     center=(mini_button1.x, mini_button1.y - 42),
                     color='black',
                     fontsize=30)
    screen.draw.text('+2 to points per s.',
                     center=(mini_button2.x, mini_button2.y - 42),
                     color='black',
                     fontsize=30)
    screen.draw.text(f'{score_per_click_price}',
                     center=(mini_button1.pos),
                     color='white',
                     fontsize=25)
    screen.draw.text(f'{score_per_second_price}',
                     center=(mini_button2.pos),
                     color='white',
                     fontsize=25)


def update(dt):
    global fontsz, score, time

    pix.pos = mouse_pos

    time += dt
    if time >= 1:
        score += score_per_second
        time = 0

    if score >= 10000000000000:
        fontsz -= 2
        if fontsz < 30:
            fontsz = 30

    if pix.colliderect(button1) and not (button_pressed):
        button1.image = 'button_select'
    elif button_pressed:
        button1.image = 'button_pressed'
    else:
        button1.image = 'button'

    if pix.colliderect(mini_button1) and not (mini_button1_pressed):
        mini_button1.image = 'minibutton_select'
    elif mini_button1_pressed:
        mini_button1.image = 'minibutton_pressed'
    else:
        mini_button1.image = 'minibutton'

    if pix.colliderect(mini_button2) and not (mini_button2_pressed):
        mini_button2.image = 'minibutton_select'
    elif mini_button2_pressed:
        mini_button2.image = 'minibutton_pressed'
    else:
        mini_button2.image = 'minibutton'


def on_mouse_down(button, pos):
    global button_pressed, score, mini_button1_pressed, mini_button2_pressed, score_per_click, score_per_click_price, score_per_second_price, score_per_second

    if button == mouse.LEFT and pix.colliderect(button1):
        button_pressed = True
        score += score_per_click

    if button == mouse.LEFT and pix.colliderect(mini_button1):
        mini_button1_pressed = True
        if score >= score_per_click_price:
            score -= score_per_click_price
            score_per_click *= 2
            score_per_click_price *= 4

    if button == mouse.LEFT and pix.colliderect(mini_button2):
        mini_button2_pressed = True
        if score >= score_per_second_price:
            score -= score_per_second_price
            score_per_second += 2
            score_per_second_price *= 2


def on_mouse_up(button, pos):
    global button_pressed, mini_button1_pressed, mini_button2_pressed

    if button == mouse.LEFT or not (pix.colliderect(button1)):
        button_pressed = False

    if button == mouse.LEFT or not (pix.colliderect(mini_button1)):
        mini_button1_pressed = False

    if button == mouse.LEFT or not (pix.colliderect(mini_button2)):
        mini_button2_pressed = False


def on_mouse_move(pos):
    global mouse_pos

    mouse_pos = pos


def on_key_down(key):
    pass


def on_key_up(key):
    pass


pgzrun.go()
