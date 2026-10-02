import pypsa
import os


def main(network: pypsa.Network) -> pypsa.Network:
    """Solve the network"""

    network.optimize(solver_name="highs")
    return network


if __name__ == "__main__":


    network_path = str(snakemake.input)
    solved_network_path = str(snakemake.output)


    network = pypsa.Network(network_path)
    solved_network = main(network)
    solved_network.export_to_netcdf(solved_network_path)
