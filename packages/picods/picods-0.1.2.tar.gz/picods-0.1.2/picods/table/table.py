from numbers import Number

import matplotlib.pyplot as plt
import pandas as pd


def picotable(
    title: str,
    rows: list[list[Number | str]],
    columns_labels: list[str],
    row_labels: list[str],
    round_digits: int = 4,
    color: str = "white",
) -> None:

    fig, ax = plt.subplots()

    # hide axes
    fig.patch.set_visible(False)
    ax.axis("off")
    ax.axis("tight")

    df = pd.DataFrame(
        rows,
        columns=columns_labels,
    ).round(round_digits)

    ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc="center",
        colColours=[color] * len(df.columns),
        rowLabels=row_labels,
        rowColours=[color] * len(df),
    )

    ax.set_title(title)
    fig.tight_layout()

    plt.show()
