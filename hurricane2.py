# hurricane.py
# Description: Animates hurricane paths on a map
# Author: [Your Name]
# Date: [Today's Date]
# Input: Hurricane data file selected by the user
# Output: Animated hurricane path with categorized markers

import turtle
import tkinter as tk


# Define category-based colors and thickness
CATEGORY_COLORS = {
    5: "red",
    4: "orange",
    3: "yellow",
    2: "green",
    1: "blue",
    0: "white"
}
# CATEGORY_THICKNESS = {
#     5: 5,
#     4: 4,
#     3: 3,
#     2: 2,
#     1: 1,
#     0: 1
# }

CATEGORY_THICKNESS = {
    5: 10,  # Increased thickness for category 5
    4: 8,   # Increased thickness for category 4
    3: 6,   # Increased thickness for category 3
    2: 4,   # Increased thickness for category 2
    1: 2,   # Increased thickness for category 1
    0: 2    # Increased thickness for category 0
}


def hurricane_setup():
    """Sets up the map and turtle."""
    turtle.setup(965, 600)
    wn = turtle.Screen()
    wn.title("Hurricane Tracker")
    wn.bgpic("images/atlanticbasin_1738788248848.png")
    t = turtle.Turtle()
    t.speed(1)
    return t, wn

def determine_category(wind_speed):
    """Determines hurricane category based on wind speed."""
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

def read_hurricane_file(filename):
    """Reads hurricane data from a file."""
    data = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        next(file)  # Skip subheader
        for line in file:
            parts = line.strip().split('\t')  # Split by tab
            if len(parts) == 7:  # Ensure the line has exactly 7 values
                date, time, lat, lon, wind_speed, pressure, storm_type = parts
                try:
                    lat, lon, wind_speed = float(lat), float(lon), int(wind_speed)
                    category = determine_category(wind_speed)
                    data.append((lat, lon, category))
                except ValueError:
                    # Skip the line if there's an issue with converting to float or int
                    print(f"Skipping invalid line: {line}")
            else:
                print(f"Skipping line with unexpected format: {line}")
    return data


def animate_hurricane(t, data):
    """Animates the hurricane path."""
    t.penup()
    for i, (lat, lon, category) in enumerate(data):
        t.goto(lon, lat)
        t.pendown()
        t.pensize(CATEGORY_THICKNESS[category])
        t.pencolor(CATEGORY_COLORS[category])
    t.penup()

def main():
    t, wn = hurricane_setup()
    filename = input("Enter the hurricane data file: ")
    data = read_hurricane_file(filename)
    animate_hurricane(t, data)
    wn.exitonclick()


if __name__ == "__main__":
    main()

























# import turtle
# import tkinter as tk

# # Define category-based colors and thickness
# CATEGORY_COLORS = {
#     5: "red",
#     4: "orange",
#     3: "yellow",
#     2: "green",
#     1: "blue",
#     0: "white"
# }

# CATEGORY_THICKNESS = {
#     5: 5,
#     4: 4,
#     3: 3,
#     2: 2,
#     1: 1,
#     0: 1
# }

# CATEGORY_IMAGES = {
#     4: "images/hurricane_1738788248848.gif",  # Custom image for category 4
#     5: "images/hurricane_1738788248848.gif",  # Custom image for category 5
#     3: "images/hurricane_1738788248848.gif",  # Custom image for category 3
#     2: "images/hurricane_1738788248848.gif",  # Custom image for category 2
#     1: "images/hurricane_1738788248848.gif",  # Custom image for category 1
#     0: "images/hurricane_1738788248848.gif"   # Custom image for category 0
# }


# def hurricane_setup():
#     """Sets up the map and turtle."""
#     turtle.setup(965, 600)
#     wn = turtle.Screen()
#     wn.title("Hurricane Tracker")
#     wn.bgpic("images/atlanticbasin_1738788248848.png")
    
#     # Register custom category images for stamps
#     for category, image in CATEGORY_IMAGES.items():
#         turtle.register_shape(image)
    
#     t = turtle.Turtle()
#     t.speed(0.5)
#     t.penup()  # Start with the pen lifted, as we're stamping
#     return t, wn


# def determine_category(wind_speed):
#     """Determines hurricane category based on wind speed."""
#     if wind_speed >= 157:
#         return 5
#     elif wind_speed >= 130:
#         return 4
#     elif wind_speed >= 111:
#         return 3
#     elif wind_speed >= 96:
#         return 2
#     elif wind_speed >= 74:
#         return 1
#     else:
#         return 0


# def read_hurricane_file(filename):
#     """Reads hurricane data from a file."""
#     data = []
#     with open(filename, 'r') as file:
#         next(file)  # Skip header
#         next(file)  # Skip subheader
#         for line in file:
#             parts = line.strip().split('\t')  # Split by tab
#             if len(parts) == 7:  # Ensure the line has exactly 7 values
#                 date, time, lat, lon, wind_speed, pressure, storm_type = parts
#                 try:
#                     lat, lon, wind_speed = float(lat), float(lon), int(wind_speed)
#                     category = determine_category(wind_speed)
#                     data.append((lat, lon, category))
#                 except ValueError:
#                     # Skip the line if there's an issue with converting to float or int
#                     print(f"Skipping invalid line: {line}")
#             else:
#                 print(f"Skipping line with unexpected format: {line}")
#     return data


# def animate_hurricane(t, data):
#     """Animates the hurricane path using custom stamps."""
#     for i, (lat, lon, category) in enumerate(data):
#         t.goto(lon, lat)
#         # Set the shape based on the hurricane category
#         t.shape(CATEGORY_IMAGES[category])
#         t.stamp()  # Place the stamp at the current position


# def main():
#     t, wn = hurricane_setup()
#     filename = input("Enter the hurricane data file: ")
#     data = read_hurricane_file(filename)
#     animate_hurricane(t, data)
#     wn.exitonclick()


# if __name__ == "__main__":
#     main()
