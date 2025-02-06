"""
Filename: hurricane.py
Description: Animates the path of a hurricane using turtle graphics, marking the storm category at each point.
Author: [Your Name]
Date: [Current Date]
Input: Text file containing hurricane data (date, time, lat, lon, wind speed, pressure, storm type)
Output: Turtle animation showing hurricane path with color-coded strength
"""

import turtle
import matplotlib.pyplot as plt
import numpy as np

def read_hurricane_data(filename):
    """Reads hurricane data from the given file."""
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            try:
                parts = line.strip().split('\t')
                date, time, lat, lon, wind, pressure, storm_type = parts
                category = get_category(int(wind))
                data.append((float(lat), float(lon), category))
            except ValueError:
                continue  # Skip invalid lines
    return data

def get_category(wind_speed):
    """Returns the hurricane category based on wind speed."""
    if wind_speed >= 157:
        return 5
    elif wind_speed >= 130:
        return 4
    elif wind_speed >= 111:
        return 3
    elif wind_speed >= 96:
        return 2
    elif wind_speed >= 74:
        return 1
    else:
        return 0

def get_color_and_thickness(category):
    """Returns the color and thickness based on hurricane category."""
    colors = {5: 'red', 4: 'orange', 3: 'yellow', 2: 'green', 1: 'blue', 0: 'white'}
    return colors.get(category, 'white'), max(1, category)  # Thickness is at least 1

def hurricane_setup():
    """Sets up the turtle screen with a map background."""
    import tkinter
    turtle.setup(965, 600)
    wn = turtle.Screen()
    wn.title("Hurricane Tracker")
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)
    map_bg_img = tkinter.PhotoImage(file="images/atlanticbasin_1738788248847.gif")
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)
    t = turtle.Turtle()
    wn.register_shape("images/hurricane_1738788248848.gif")
    t.shape("images/hurricane_1738788248848.gif")
    return t, wn

def animate_hurricane(data):
    """Animates the hurricane path using turtle graphics."""
    t, wn = hurricane_setup()
    t.speed(1)
    t.penup()
    
    for lat, lon, category in data:
        color, thickness = get_color_and_thickness(category)
        t.goto(lon, lat)
        t.pendown()
        t.pensize(thickness)
        t.pencolor(color)
        t.forward(5)
    
    wn.exitonclick()

def main():
    """Main function to execute the hurricane animation."""
    while True:
        filename = input("Enter hurricane data file (or 'exit' to quit): ")
        if filename.lower() == 'exit':
            break
        try:
            data = read_hurricane_data(filename)
            animate_hurricane(data)
        except FileNotFoundError:
            print("File not found. Please try again.")

if __name__ == "__main__":
    main()
