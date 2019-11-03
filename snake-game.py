"""
    A simple snake game. Using arrow keys to navigate the snake, ESC key to exit the game
"""
import curses
from curses import KEY_RIGHT, KEY_DOWN, KEY_UP, KEY_LEFT
from random import randint

curses.initscr()  # initialising the terminal screen
curses.noecho()  # to not echo keys pressed while playing the game
curses.curs_set(0)  # setting the cursor's visibility/blinking state to 0

win = curses.newwin(20, 60, 0, 0)  # creating a new window of dimensions 20 * 60 (y * x)
win.keypad(1)  # treat special keyboard characters as is
win.border(0)  # draw a border on the terminal screen

key = KEY_RIGHT  # setting the default key pressed to RIGHT ARROW
snake = [[5, 10], [5, 9], [5, 8]]  # initial snake co-ordinates
food = [10, 10]  # initial food co-ordinates
win.addch(food[0], food[1], '#')  # placing the food on the screen
score = 0

while key != 27:  # 27 is the value for ESC key. Play the game until ESC key is pressed
    win.addstr(0, 2, f"Score : {score}")
    win.timeout(150)  # wait for 150 milliseconds before capturing the input from the screen
    event = win.getch()  # read inputs from the screen
    key = key if event == -1 else event

    # moving the snake in the direction of the key pressed
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1),
                     snake[0][1] + (key == KEY_RIGHT and 1) + (key == KEY_LEFT and -1)])

    # end the game if snake runs over itself
    if snake[0] in snake[1:]: break

    # making the snake enter from the other side if the head hits the other side of the boundary
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # if the snake's head co-ordinates and the food co-ordinates match, it means that the snake has eaten the food
    if snake[0] == food:
        food = [randint(1, 18), randint(1, 58)]  # place the food at another co-ordinate randomly
        win.addch(food[0], food[1], '#')
        score += 1  # increment the score
    else:
        # if the snake doesn't eat the food, pop the last element of the snake's co-ordinates (tail) and replace it with an empty space
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')
    win.addch(snake[0][0], snake[0][1], '*')

# cleaning up the terminal to its previous state
curses.echo()
curses.curs_set(1)
curses.endwin()

print(f"Your Score: {score}")
