"""Worst Pizza Topping entry (make.fun bounty u-motasimfuad-the-worst-pizza-topping-062c6893).

Writes one funny line pitching a terrible pizza topping to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
"""

import os

ENTRY = "Try the Biohazard Special \u2014 a pizza topped with glow-in-the-dark mushrooms the box warns of 'mild levitation.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
