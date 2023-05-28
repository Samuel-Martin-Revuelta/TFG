from sys import argv

file = open(argv[1], "r")
IPR012951_p = open("IPR012951.fasta", "a")
IPR016169_p = open("IPR016169.fasta", "a")
IPR012951_IPR016169_p = open("IPR012951_IPR016169.fasta", "a")

IPR012951_n = open("IPR012951_n.txt", "a")
IPR016169_n = open("IPR016169_n.txt", "a")
IPR012951_IPR016169_n = open("IPR012951_IPR016169_n.txt", "a")


for line in file:
    data = line.split('\t')
    species_name = "C_gloeosporioides"
    if "IPR012951" in data[6]:
        if "IPR016169" in data[6]:
            IPR012951_IPR016169_n.write(">"+species_name+"_"+data[1]+"\n"+"")
            IPR012951_IPR016169_p.write(">"+species_name+"_"+data[1]+"\n"+data[7].replace(" ", "_"))
        else: 
            IPR012951_n.write(">"+species_name+"_"+data[1]+"\n"+"")
            IPR012951_p.write(">"+species_name+"_"+data[1]+"\n"+data[7].replace(" ", "_"))
    elif "IPR016169" in data[6]:
        IPR016169_n.write(">"+species_name+"_"+data[1]+"\n"+"")
        IPR016169_p.write(">"+species_name+"_"+data[1]+"\n"+data[7].replace(" ", "_"))
        
        
