from sys import argv

file = open(argv[1], "r")
sp_name = "VALF"
archive_name = sp_name+".fasta"
proteome_fasta = open(archive_name, "a")

for line in file:
    data = line.split('\t')
    if data[1] != "Entry name":
        proteome_fasta.write(">"+data[1]+"\n"+data[7])
 
        

