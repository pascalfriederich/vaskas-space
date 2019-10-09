# Welcome to Vaska's space
This repository contains a list of 1947 Iridium complexes, including their geometry (xyz files) and energy barriers for the hydrogen splitting reaction.

The data loader (vaskas_data_loader.py) provides some basic functionality to load the complexes.

# Data
* Coordinates in xyz files
* csv file with
    * "smiles": [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system) strings of all molecules
    * "filename": corresponding xyz filename
    * "barrier": DFT computed energy barrier [kcal/mol] for the transition state of the hydrogen splitting reaction
    * "distance": DFT computed H-H distance in the transition state geometry
    * "chi-X", "Z-X", "T-X", "I-X" and "S-X": (auto)correlation features described in [out paper](https://chemrxiv.org/)

![Image of the chemical space of the Vaska's complexes](images/chemical_space.png)

More information can be found here:

[ChemRxiv](https://chemrxiv.org/)



