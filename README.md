# ColorPuzzle

Inspired by Colorfle, a Wordle offshoot. This puzzle allows users to change the puzzle's palette and other parameters.

## Custom Colorfle

Open `src/custom_colorfle.html` in a browser to play a customizable color-mixing puzzle.

- Edit the 12-color base palette in the right panel.
- Choose a 3, 4, 5, or 6-color recipe, then click **New puzzle**.
- Click palette tiles to fill the weighted slots on the lower half of the wheel.
- Click a previous guess number to recall that mix and compare its resulting color.
- Feedback matches Colorfle-style clues: green is the right color in the right slot, yellow is a recipe color in the wrong slot, and gray is not in the recipe.

Palette changes are saved in the browser with `localStorage`.
