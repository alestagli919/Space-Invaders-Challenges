# Space Invaders Challenges

A simple two-player game made with Python and Pygame.

## How to run

Install Pygame:

```bash
py -m pip install pygame
```

Run the game:

```bash
py main.py
```

## Controls

- Player 1 (green): W, A, S, D
- Player 2 (blue): Arrow keys
- Increase Player 1 speed: + (or numpad +)
- Decrease Player 1 speed: - (or numpad -)
- Pause / resume: ESC
- Restart after Game Over: R

## Challenges completed

1. Keep both players inside the window.
2. Spawn random obstacles between 20 and 70 pixels, fully within the window width.
3. Detect collisions with both players.
4. Pause and resume the game using ESC.
5. Restart after Game Over using R.
6. Show survival time, excluding pause and Game Over.
7. Increase obstacle spawn frequency every 10 points, down to a minimum interval of 150 ms.
8. Change Player 1 speed between 2 and 12 with key presses.
9. Keep the high score during the current session.
10. Optional: Each player has three lives and two seconds of invulnerability after a hit; the game ends when both have zero lives.

## Scoring

Earn one point for each obstacle that passes the bottom of the screen.

## Remaining optional challenges

- 11. Power-ups.
- 12. Save named scores to `scores.txt` and display a top-five leaderboard.

## Gameplay video

[Watch the gameplay video](gameplay.mp4)

The gameplay recording is included in this repository as `gameplay.mp4`.
