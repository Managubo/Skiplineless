import os
os.getcwd()
os.chdir("C:\\Manuel\\SPLsTulip")
    #("C:\\Users\\usuario\\Desktop\\SPLs 7-2020")
"""
With this script we´re going to read a .txt file with the fasta sequences containing line skips (\n) of our genes
and then we´re going to write a new .txt file with the IDs and the sequences without the line skips.
"""
#Read file with \n and open the file where we´ll store the \n-less sequences
with open("C:\\Manuel\\SPLsTulip\\data\\raw\\cDNA.txt", "r") as source, open("C:\\Manuel\\SPLsTulip\\data\\processed\\SPLs cDNA sequences wo-spaces.txt", "w") as new_file:


    #Loop over the lines
    for line in source.readlines():
        seq = ""
        if line.startswith(">"):    #Identifies when a line stars with a ">" symbol
            ID = line.rstrip()      #If the line starts with ">", then such line is assigned as an ID
            new_file.write(ID + "\n")
#        elif line.endswith("\n"):  #In this case it does the same as just using "else:"
        elif line == "\n":
            new_file.write(line + "\n")
        else:
            seq += line.rstrip()
            new_file.write(seq.upper())


with open("C:\\Manuel\\SPLsTulip\\data\\processed\\SPLs cDNA sequences wo-spaces.txt", "r") as proof:
    text = proof.read()

print(text)