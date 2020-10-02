import os
os.getcwd()
os.chdir("C:\\Manuel\\SPLsTulip")

""""
With this script we´re going to read a .txt file containing gene IDs and Arabidopsis thaliana cDNA SPL
sequences. In the file, several sequences are chopped by line skips (\n), we´re going to write a new
.txt file with the IDs and the sequences in a single line without the line skips. Each ID + sequence
set will be separated by an empty line, after which the next ID + sequence set will be printed.
To confirm that the code works a function is used at the end of the script to print the newly created
.txt file.
"""

# Read file with \n and open the file where we´ll store the \n-less sequences
with open("C:\\Manuel\\SPLsTulip\\data\\raw\\cDNA.txt", "r") as source,\
     open("C:\\Manuel\\SPLsTulip\\data\\processed\\cDNAs_wo_spaces.txt", "w") as new_file:

# Loop over the lines
    for line in source.readlines():
        seq = ""
        if line.startswith(">"):    # Identifies when a line stars with a ">" symbol
            ID = line.rstrip()      # Line starting with ">", are assigned as an ID
            new_file.write(ID + "\n")
        elif line == "\n":
            new_file.write(line + "\n")
        else:
            seq += line.rstrip()
            new_file.write(seq.upper())


with open("C:\\Manuel\\SPLsTulip\\data\\processed\\cDNAs_wo_spaces.txt", "r") as proof:
    text = proof.read()

print(text)