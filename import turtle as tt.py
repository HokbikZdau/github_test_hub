import turtle as tt

# turtle is great to draw!!!
# Set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

# Iterate six times in total
for i in range(40):
    # Choose your color combination
    for color in ('red', 'white'):
        tt.color(color)
        # Draw a circle of chosen size, 100 here
        tt.circle(100)
        # Move 10 pixels left to draw another circle
        tt.left(10)

# Hide the cursor(or turtle) which drew the circle
tt.hideturtle()
