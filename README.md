# Snake-Water-Gun Game

## Overview

Welcome to the Snake-Water-Gun game, a Python-based implementation of the classic game where you compete against the computer. The game is based on three choices: Snake (S), Water (W), and Gun (G), each of which interacts with the others according to simple rules:

- Snake drinks Water and wins.
- Water drowns the Gun and wins.
- Gun shoots the Snake and wins.

In this game, you can play for a specific number of rounds, and at the end, your results will display the total number of Wins, Losses, and Draws.

## Features

- Play the game against the computer.
- Choose from three options: Snake (S), Water (W), and Gun (G).
- Track results (Wins, Losses, Draws) for the total number of rounds.
- Handle invalid inputs gracefully with user-friendly prompts.
- Interactive and engaging game logic.

## How to Run

To run the game, simply execute the Python script. Make sure you have Python 3.x installed on your system.

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Snake-Water-Gun.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Snake-Water-Gun
   ```

3. Run the Python script:

   ```bash
   python snake_water_gun.py
   ```

4. Follow the on-screen instructions to enter your choices for each round.

## Game Flow

- Upon starting, the game will prompt you to enter the total number of rounds you want to play.
- For each round, you'll choose from:
  - **S** for Snake
  - **W** for Water
  - **G** for Gun
- The computer will randomly choose one of the three options.
- After each round, you'll see whether you won, lost, or tied, and the results will be updated accordingly.
- At the end of the game, the program will display your total Wins, Losses, and Draws.

## Example

```
..:: The Total Point: 3

1. Enter your choice (S for Snake, W for Water, G for Gun): S
---> You Chose: Snake AND The Computer Chose: Gun
..:: You Win!

2. Enter your choice (S for Snake, W for Water, G for Gun): G
---> You Chose: Gun AND The Computer Chose: Snake
..:: You Lose!

3. Enter your choice (S for Snake, W for Water, G for Gun): W
---> You Chose: Water AND The Computer Chose: Gun
..:: You Win!

==> Total Win(s): 2, Lose(s): 1 and Draw(s): 0 in 3 Points...
```

## Contributions

Feel free to fork the repository and contribute to improving the game! You can:

- Fix bugs.
- Add new features or game modes.
- Improve the user interface or experience.
- Optimize the code.

To contribute, please fork the repo, make changes, and create a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy playing the game, and feel free to reach out with any suggestions or feedback!
```

This `README.md` file gives a complete guide to understanding, running, and contributing to your project while maintaining a human-written, clear, and concise style.
