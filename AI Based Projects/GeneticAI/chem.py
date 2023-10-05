import numpy as np
from fractions import Fraction

reactants = ["k4Fe(CN)6", "KMnO4", "H2SO4"]
products = ["KHSO4", "Fe2(SO4)3", "MnSO4", "HNO3", "CO2", "H20"]

element_counts = {
    "k4Fe(CN)6": {"K": 4, "Fe": 1, "C": 6, "N": 6},
    "KMnO4": {"K": 1, "Mn": 1, "O": 4},
    "H2SO4": {"H": 2, "S": 1, "O": 4},
    "KHSO4": {"K": 1, "H": 1, "S": 1, "O": 4},
    "Fe2(SO4)3": {"Fe": 2, "S": 3, "O": 12},
    "MnSO4": {"Mn": 1, "S": 1, "O": 4},
    "HNO3": {"H": 1, "N": 1, "O": 3},
    "CO2": {"C": 1, "O": 2},
    "H20": {"H": 2, "O": 1}
}

all_elements = set([item for sublist in [list(element_counts[key].keys()) for key in element_counts] for item in sublist])

A = []

for element in all_elements:
    row = []
    for compound in reactants[1:]:
        row.append(-element_counts.get(compound, {}).get(element, 0))
    for compound in products:
        row.append(element_counts.get(compound, {}).get(element, 0))
    A.append(row)

b = []
for element in all_elements:
    b.append(element_counts.get(reactants[0], {}).get(element, 0))

A = np.array(A, dtype=float)
b = np.array(b, dtype=float)

x = np.linalg.lstsq(A, b, rcond=None)[0]

fractions = [Fraction(item).limit_denominator() for item in x]

lcm = np.lcm.reduce([fraction.denominator for fraction in fractions])

scaled_x = [int(item * lcm) for item in x]
scaled_x = [lcm] + scaled_x 

print("ansssssss:", scaled_x)
