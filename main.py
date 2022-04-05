import math
elements = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067,
                'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815386,
                'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
                'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64,
                'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585,
                'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42,
                'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.760, 'Te': 127.6,
                'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116,
                'Pr': 140.90465, 'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
                'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
                'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217,
                'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
                'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176, 'Fr': 223.0197, 'Ra': 226.0254, 'Ac': 227.0278,
                'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237.0482, 'Pu': 244.0642, 'Am': 243.0614,
                'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796, 'Es': 252.0829, 'Fm': 257.0951, 'Md': 258.0951,
                'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268, 'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278,
                'Ds': 281, 'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289, 'Lv': 292, 'Ts': 294, 'Og': 294}

blank_elements={'H': 0, 'He': 0, 'Li': 0, 'Be': 0, 'B': 0, 'C': 0, 'N': 0,
                'O': 0, 'F': 0, 'Ne': 0, 'Na': 0, 'Mg': 0, 'Al': 0,
                'Si': 0, 'P': 0, 'S': 0, 'Cl': 0, 'Ar': 0, 'K': 0, 
                'Ca': 0, 'Sc': 0, 'Ti': 0, 'V': 0, 'Cr': 0, 'Mn': 0,
                'Fe': 0, 'Co': 0, 'Ni': 0, 'Cu': 0, 'Zn': 0, 'Ga': 0, 'Ge': 0,
                'As': 0, 'Se': 0, 'Br': 0, 'Kr': 0, 'Rb': 0, 'Sr': 0, 'Y': 0,
                'Zr': 0, 'Nb': 0, 'Mo': 0, 'Tc': 0, 'Ru': 0, 'Rh': 0, 'Pd': 0,
                'Ag': 0, 'Cd': 0, 'In': 0, 'Sn': 0, 'Sb': 0, 'Te': 0,
                'I': 0, 'Xe': 0, 'Cs': 0, 'Ba': 0, 'La': 0, 'Ce': 0,
                'Pr': 0, 'Nd': 0, 'Pm': 0, 'Sm': 0, 'Eu': 0, 'Gd': 0,
                'Tb': 0, 'Dy': 0, 'Ho': 0, 'Er': 0, 'Tm': 0, 'Yb': 0,
                'Lu': 0, 'Hf': 0, 'Ta': 0, 'W': 0, 'Re': 0, 'Os': 0, 'Ir': 0,
                'Pt': 0, 'Au': 0, 'Hg': 0, 'Tl': 0, 'Pb': 0, 'Bi': 0,
                'Po': 0, 'At': 0, 'Rn': 0, 'Fr': 0, 'Ra': 0, 'Ac': 0,
                'Th': 0, 'Pa': 0, 'U': 0, 'Np': 0, 'Pu': 0, 'Am': 0,
                'Cm': 0, 'Bk': 0, 'Cf': 0, 'Es': 0, 'Fm': 0, 'Md': 0,
                'No': 0, 'Lr': 0, 'Rf': 0, 'Db': 0, 'Sg': 0, 'Bh': 0, 'Hs': 0, 'Mt': 0,
                'Ds': 0, 'Rg': 0, 'Cn': 0, 'Nh': 0, 'Fl': 0, 'Mc': 0, 'Lv': 0, 'Ts': 0, 'Og': 0}
 

def getWeight(input, sig = "x"):
    #splits array at spaces
    arr = input.split(" ")
    #convert all strings to ints when possible
    for x in range (0, len(arr)):
        try:
            arr[x] = int(arr[x])
        except ValueError:
            pass
    x = 0
    #add implicit 1's
    while x < len(arr)-1:
        if (type(arr[x]) == str and not type(arr[x+1]) == int):
            arr.insert(x+1, 1)
        x = x + 1
    if (type(arr[len(arr)-1]) == str):
        arr.append(1)
    #add corsponding quantites to blank blank_elements
    #throws error if key does not exist
    for i in range (0, len(arr), 2):
        try:
            temp = blank_elements.get(arr[i]) + arr[i+1]
            blank_elements.update({arr[i]: temp})
        except:
            return "Invalid entry"
    #goes through every element in the quantity dictionay and adds the molar weight
    total = 0
    for i in blank_elements:
        total = total + (elements.get(i) * blank_elements.get(i))
    #if a number of sig figs is entered, returns proper sig figs
    #if not, passes and returns with no rounding
    try:
        total = round(total, sig-int(math.floor(math.log10(abs(x))))-2)
        return total
    except:
        pass
    return total

def main():
    print(getWeight("Na Cl", 4))
if __name__ == "__main__":
    main()