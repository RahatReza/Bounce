import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Catch the Ball")
window.geometry("400x400")

# Create the canvas
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create the player paddle
paddle = canvas.create_rectangle(175, 380, 225, 390, fill="blue")

# Create the ball
ball = canvas.create_oval(190, 190, 210, 210, fill="red")

# Set the initial ball direction and speed
ball_dx = random.choice([-2, -1, 1, 2])
ball_dy = -2

# Function to handle key events
def move_paddle(event):
    key = event.keysym
    x1, _, x2, _ = canvas.coords(paddle)

    if key == "Left" and x1 > 0:
        canvas.move(paddle, -10, 0)
    elif key == "Right" and x2 < 400:
        canvas.move(paddle, 10, 0)

# Bind the key event to the move_paddle function
canvas.bind_all("<KeyPress>", move_paddle)

# Function to update the game state
def update():
    global ball_dx, ball_dy  # Declare the global variables

    canvas.move(ball, ball_dx, ball_dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    # Check if the ball hits the paddle
    if y2 >= 380 and x2 >= canvas.coords(paddle)[0] and x1 <= canvas.coords(paddle)[2]:
        ball_dy *= -1

    # Check if the ball hits the walls
    if x1 <= 0 or x2 >= 400:
        ball_dx *= -1
    if y1 <= 0:
        ball_dy *= -1

    # Check if the ball goes out of bounds
    if y2 >= 400:
        canvas.delete(ball)
        canvas.create_text(200, 200, text="Game Over", font=("Helvetica", 24))
    else:
        window.after(10, update)  # Call the update function again

# Start the game loop
update()

# Start the main event loop
window.mainloop()
