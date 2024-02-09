# Elevator Simulation

This project is a simulation of an elevator system implemented using Python and Pygame library. It simulates the operation of an elevator, allowing users to interact with it by selecting floors and observing its movement.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Virtual Environment (venv)](#virtual-environment-venv)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Elevator Simulation project is designed to provide a visual representation of an elevator system. It allows users to interact with the elevator by selecting floors using keyboard input. The simulation displays the movement of the elevator as it travels between floors, opens and closes its doors, and tracks the number of passengers.

The Elevator's max capacity is 9 people, if it reaches max capacity, it automatically goes to first floor, simulation a drop off.

This simulation is used to develop ML operations that minimizes the waiting time for passengers.

For a view of the project:
https://talentospropygame.itch.io/elevator-game
Only playable in Desktop, runs on mobile but no user input allowed

## Features

- Simulation of elevator movement and operation.
- User interaction through keyboard input to select floors.
- Visual representation of elevator movement and status.
- Display of the number of passengers inside the elevator.
- Real-time clock display.

## Installation

To run the Elevator Simulation project, follow these steps:

1. Clone the repository to your local machine:
    git clone <repository_url>

2. Navigate to the project directory:
    cd elevator_game

3. Create a virtual environment using Python's `venv` module:
    python3 -m venv venv

4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
    pip install -r requirements.txt

## Usage
To run the Elevator Simulation project, execute the following command:

    python3 main.py

Once the simulation is running, use the keyboard to interact with the elevator:
- Press keys 0-9 to select floors.
- Observe the elevator's movement and status on the screen.
- View the number of passengers inside the elevator and the current time.

## Screenshots

![Evotar as Avatar](/Evotar_Image.png)
*Image of the Evotar.*

![Image of the Game](/ReadMe_Image.png)
*The elevator moving to picking up the Evotar.*

![Resting Elevator](/Elevator_Image.png)
*Elevator in resting position.*

![Moving Elevator](/opened_door_elevator.png)
*Elevator mooving.*