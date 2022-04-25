'''
Full Name: Francesco Lezano
Teacher: Bro. Codling
Title: L04 Assignment(Drawing 2d graphics)


During the previous lesson's milestone, you wrote code to draw at 
least the sky, clouds, and ground of an outdoor scene. During this lesson, 
you will write code that draws the remaining objects in your scene. 
Your program can draw any outdoor scene that you like as long as it 
meets these requirements:

1. The scene must be outdoor and include part of the sky.
2. The sky must have clouds.
3. The scene must include repetitive objects, such as blades of grass, trees, 
leaves on a tree, birds, flowers, insects, fish, pickets in a fence, 
dashed lines on a road, buildings, bales of hay, snowmen, snowflakes, or icicles.
'''

# Import the functions from the Draw 2-D library 
# so I can use it in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_house(canvas,300, 165)
    draw_house(canvas,150, 150)
    draw_house(canvas,450, 150)
    # Draw the pool. (exceed requirements)
    draw_rectangle(canvas, 220,0,580,120, fill="steelBlue1")

    draw_pine_tree(canvas, 140, 100, 180)
    draw_pine_tree(canvas, 80, 100, 180)
    draw_pine_tree(canvas, 100, 70, 180)
    draw_pine_tree(canvas, 50, 50, 180)
    draw_pine_tree(canvas, 0, 0, 180)
    # copy and past trees. (exceed requirements)
    draw_pine_tree(canvas, 650, 100, 180)
    draw_pine_tree(canvas, 720, 100, 180)
    draw_pine_tree(canvas, 700, 70, 180)
    draw_pine_tree(canvas, 750, 50, 180)
    draw_pine_tree(canvas, 800, 0, 180)

    # Draw the sun. (exceed requirements)
    draw_oval(canvas, 400, 380, 500, 480, width=0,fill="yellow1")

    # Draw the clouds. (exceed requirements)
    draw_oval(canvas, 300, 415, 50, 470, width=0,fill="ivory1")
    draw_oval(canvas, 590, 415, 790, 470, width=0,fill="ivory1")
   
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    # Draw the sky and all the objects in the sky.
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="skyBlue1")


def draw_ground(canvas, scene_width, scene_height):
    # Draw the ground.
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="navajoWhite3")


def draw_pine_tree(canvas, center_x, bottom, height):

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="saddleBrown")

    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="forest green")

def draw_house(canvas, house_left=0, house_bottom=0):
    
    # Making wall.
    draw_rectangle(canvas,
            house_left, house_bottom, house_left+200, house_bottom+135,
            outline="gray20", width=1, fill="aliceBlue")

    # Making door.
    draw_rectangle(canvas,
            house_left + 80, house_bottom, house_left + 130, house_bottom+55,
            outline="gray20", width=1, fill="red2")
    # Making Ceeling.
    draw_polygon(canvas, 
            house_left + 100, house_bottom + 235,
            house_left + 200, house_bottom + 135,
            house_left, house_bottom + 135,
            outline="gray20", width=1, fill="orange")

# Call the main function so that
# this program will start executing.
main()