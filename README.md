# Hurricane Tracker

## Project Description
This project visualizes the path of hurricanes on a map using Python and the Turtle graphics module. The program reads hurricane data from user-selected files and animates the hurricane’s movement with color-coded paths based on the storm's category.

## Features
- Reads hurricane data from a user-specified text file.
- Animates the hurricane's movement on a map.
- Uses different colors to indicate storm strength:
  - **Red**: Category 5 (157+ mph)
  - **Orange**: Category 4 (130-156 mph)
  - **Yellow**: Category 3 (111-129 mph)
  - **Green**: Category 2 (96-110 mph)
  - **Blue**: Category 1 (74-95 mph)
  - **White**: Below hurricane strength
- Adjusts line thickness based on hurricane category.
- Interactive user input to select hurricane data files.

## Installation & Setup
1. Ensure Python is installed on your system.
2. Install dependencies if necessary (e.g., `tkinter` is built into Python but may require installation on some systems).
3. Place your hurricane data files (e.g., `Ian2022.txt`) in the project directory.
4. Run the script:
   ```bash
   python hurricane.py
   ```
5. Enter the filename when prompted to visualize the hurricane path.

## File Structure
```
project-folder/
│── images/
│   ├── atlantic-basin.gif   # Background map
│   ├── hurricane.gif        # Hurricane icon
│── hurricane.py             # Main program
│── Ian2022.txt              # Sample hurricane data
│── README.md                # Project documentation
```

## Data Format
Hurricane data files should follow this format:
```
Date       Time        Lat    Lon    Wind(mph)    Pressure(mb)    Storm Type
9/23/2022  5:00 AM    13.90  -68.60 35           1006            Tropical Depression
```
- Latitude and Longitude must be in decimal format.
- Wind speed determines the hurricane category.
