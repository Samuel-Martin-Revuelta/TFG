from sys import argv

file = open(argv[1], "r")
IPR012951_ipr = open("IPR012951.csv", "a")
IPR016169_ipr = open("IPR016169.csv", "a")
IPR012951_IPR016169_ipr = open("IPR012951_IPR016169.csv", "a")

for line in file:
    data = line.split('\t')
    species_name = "C_tofieldiae"
    if "IPR012951" in data[6]:
        if "IPR016169" in data[6]:
            IPR012951_IPR016169_ipr.write(species_name+"_"+data[1]+";"+data[6]+"\n")
        else: 
            IPR012951_ipr.write(species_name+"_"+data[1]+";"+data[6]+"\n")
    elif "IPR016169" in data[6]:
        IPR016169_ipr.write(species_name+"_"+data[1]+";"+data[6]+"\n")
