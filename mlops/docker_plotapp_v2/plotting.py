from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def create_plot(numbers: list[int]) -> str:
    """
    Create a line plot from the given numbers.

    Returns
    -------
    str
        Generated image filename.
    """

    filename = f"plot_{datetime.now():%Y%m%d_%H%M%S}.png"

    filepath = UPLOAD_DIR / filename

    plt.figure(figsize=(6, 4))

    plt.plot(numbers, marker="o")

    plt.title("Number Plot")

    plt.xlabel("Index")

    plt.ylabel("Value")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(filepath)

    plt.close()

    return filename
