import numpy as np
import pandas as pd


def readxyz(filename):
    coords=[]
    elements=[]
    for lineidx,line in enumerate(open(filename,"r")):
        if lineidx >= 2:
            elements.append(line.split()[0].capitalize())
            coords.append([float(line.split()[1]),float(line.split()[2]),float(line.split()[3])])
    coords=np.array(coords)
    return(coords, elements)


def load_data():
    data = pd.read_csv("data/vaskas_features_properties_smiles_filenames.csv")

    molecules_complex=[]
    for filename in data["filename"]:
        coords, elements = readxyz("data/coordinates_complex/{}_min.xyz".format(filename))
        molecules_complex.append([coords, elements])

    molecules_TS=[]
    for filename in data["filename"]:
        coords, elements = readxyz("data/coordinates_TS/{}_ts.xyz".format(filename))
        molecules_TS.append([coords, elements])

    return(data, molecules_complex, molecules_TS)


def quick_data_analysis(molecules):
    elements_unique = []
    mol_sizes = []
    for mol in molecules:
        coords = mol[0]
        elements = mol[1]
        mol_size = len(coords)
        for el in set(elements):
            if el not in elements_unique:
                elements_unique.append(el)
        mol_sizes.append(mol_size)
    print("found the following elements:")
    print(elements_unique)
    size_min = min(mol_sizes)
    size_max = max(mol_sizes)
    print("the size of the complexes ranges from {} to {} atoms".format(size_min, size_max))
    return()


if __name__ == "__main__":
    data, molecules_complex, molecules_TS = load_data()
    num_molecules_complex = len(molecules_complex)
    num_molecules_TS = len(molecules_TS)
    quick_data_analysis(molecules_complex)
    print("Found {} molecules in optimized complex geometry".format(num_molecules_complex))
    print("Found {} molecules in optimized transition state geometry".format(num_molecules_TS))
    print(data.head())




