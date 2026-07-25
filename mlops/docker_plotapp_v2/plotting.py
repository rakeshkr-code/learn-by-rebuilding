from datetime import datetime

import matplotlib.pyplot as plt

from config import UPLOAD_DIR
from logger import logger


def create_plot(numbers: list[int]) -> str:
    """
    Generate a line plot from the given numbers.

    Parameters
    ----------
    numbers : list[int]
        List of integers to plot.

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

    logger.info("Created plot %s", filename)

    return filename

