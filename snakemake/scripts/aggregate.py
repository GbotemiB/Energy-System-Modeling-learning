import pandas as pd
import matplotlib.pyplot as plt
import pypsa
from typing import TYPE_CHECKING


def aggregate_results(n):
    """
    Aggregate the results of the optimization.
    """
    return (
        pd.concat([n.statistics.capex(), n.statistics.opex()])
        .groupby("carrier")
        .sum()
        .div(1e9)
    )  # bn€/a



def plot_sensitivity(df, colors=None):
    df.plot.area(
        stacked=True,
        linewidth=0,
        color=df.columns.map(colors),
        figsize=(4, 4),
        xlim=(0, 150),
        xlabel=r"CO$_2$ emissions [Mt/a]",
        ylabel="System cost [bn€/a]",
        ylim=(0, 80),
        backend="matplotlib",
    )
    plt.legend(frameon=False, loc=(1.05, 0))


if __name__ == "__main__":
    if TYPE_CHECKING:
            from snakemake.script import snakemake
            
    sensitivity_results = {}

    for path, co2 in zip(snakemake.input, snakemake.params["co2"]):
        n = pypsa.Network(path)
        sensitivity_results[co2] = aggregate_results(n)

        df = pd.DataFrame(sensitivity_results).T
        df.to_csv(snakemake.output["stats"])
        plot_sensitivity(df, n.carriers["color"])
        plt.savefig(snakemake.output["plot"], bbox_inches="tight", dpi=300)