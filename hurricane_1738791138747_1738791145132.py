# INCLUDE A TOP BLOCK COMMENT name of file, description, name, date, input, output

import turtle

# Creates the Turtle and Screen with a background map
# Original code by Phil Ventura
# http://nifty.stanford.edu/2018/ventura-hurricane-tracker/nifty-hurricanes.html
#
# Creates turtle and screen with map and proper coordinates
# output: returns a tuple with turtle and screen and turtle icon
# 
# Modified by DRF

def hurricane_setup():
    """       DO NOT CHANGE THE CODE IN THIS FUNCTION! """
    # DRF - changed "tkinter" to "Tkinter as tkinter" to run on Windows 10
    # DRF - when using Windows 11 use import tkinter
    import tkinter
    
    # set size of window to size of map
    turtle.setup(965, 600)

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    # set the coordinate system to match lat/long
    # DRF - parameters are llx lly urx ury (lower left and upper right)
    turtle.setworldcoordinates(-90, 0, -17.66, 45)
    
    # DRF - Windows only supports gif, pgm, ppm unless you use the PIL library
    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

# Remember to comment your functions
def hurricane():
    # this can go here or in main depending on how you plan to set up your code
    (t, wn, map_bg_img) = hurricane_setup()

    # YOUR CODE TO ANIMATE HURRICANE DATA GOES HERE
    
    # DRF - Added so window does not become unreponsive when moved
    # this can go here or in main depending on how you plan to set up your code
    wn.exitonclick()

def main():
    hurricane()

main()
