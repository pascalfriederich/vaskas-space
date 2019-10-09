# Welcome to Vaska's space
This repository contains a list of 1947 Iridium complexes, including their geometry (xyz files) and energy barriers for the hydrogen splitting reaction.

For more information, please read our paper on [ChemRxiv](https://chemrxiv.org/).

The data loader (vaskas_data_loader.py) provides some basic functionality to load the complexes.

## Data
* Coordinates in xyz files
    * data/coordinates_complex: the .xyz files of all complexes without additional hydrogen
    * data/coordinates_TS: the .xyz files of all complexes with an additional hydrogen molecule in transition state
* csv (data/vaskas_features_properties_smiles_filenames.csv) file with
    * "smiles": [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) strings of all molecules
    * "filename": corresponding xyz filename
    * "barrier": DFT computed energy barrier [kcal/mol] for the transition state of the hydrogen splitting reaction
    * "distance": DFT computed H-H distance in the transition state geometry
    * "chi-X", "Z-X", "T-X", "I-X" and "S-X": (auto)correlation features described in [out paper](https://chemrxiv.org/)


## Chemical space

We constructed 2574 unique iridium complexes in a combinatorial way using the following scheme. In an automated DFT based workflow, we computed the energy barriers of the hydrogen splitting reaction for 1947 of these complexes.

![Image of the chemical space of the Vaska's complexes](images/chemical_space.png)


## Links

More information can be found here:

[ChemRxiv](https://chemrxiv.org/)



