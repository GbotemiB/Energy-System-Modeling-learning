import pandas as pd
import matplotlib.pyplot as plt
import pypsa


def add_sensitvity_to_network(n, co2):
    """
    Add sensitivity analysis results to the network.
    """
    n.global_constraints.loc["CO2Limit", "constant"] = co2 * 1e6
    return n

if __name__ == "__main__":

    n = pypsa.Network(snakemake.input[0])
    n = add_sensitvity_to_network(n, float(snakemake.wildcards["CO2"]))
    n.export_to_netcdf(snakemake.output[0])


