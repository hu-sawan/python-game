# Python Game using Pygame

This repository contains a simple game written in Python using the Pygame library. The game was created as a practice project to master Python syntax and explore game development concepts. The game is a simple 2D platformer where the player has to avoid flying balls and collect coins to score points. As score increases, the speed of the player also increases. The collision implementation needes some modification since it only checks if corners collide and this is causing a bug when speed is high, I will fix it later.

## Table of Contents

-   [Installation](#installation)
-   [Usage](#usage)
-   [Controls](#controls)

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install the Pygame library using pip:

```bash
pip install pygame
```

3. Clone this repository to your local machine:

```bash
git clone https://github.com/hu-sawan/simple-python-game.git
```

## Usage

To run the game, navigate to the project directory and execute the following command:

```bash
py main.py
```

## Controls

-   Use the arrow keys to move the player box
-   also use `w` for up direction, `a` for left direction, `s` for down direction and `d` for right direction.
-   Press `Esc` to exit the game
