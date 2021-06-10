import os
import argparse

parser = argparse.ArgumentParser("This script parses amber mdout files to extrace the total energy")
parser.add_argument("filepath", help= "The filepath to the file to be analyzed.")

args = parser.parse_args()

filename = args.filepath
f = open(filename, 'r')
data = f.readlines()
f.close()

print(f'Analyzing {filename}')

# data/03_Prod.mdout
# 03_Prod_Etot.txt

# data/mdout/polyAT_vac.mdout
# polyAT_cav_Etot.txt

output_filename = os.path.basename(filename)
output_filename = output_filename.split('.')[0]
output_filename = F"{output_filename}_Etot.txt"

print(F"Writing output to {output_filename}")

f_write = open(output_filename, 'w+')
energies = []

for line in data: 
    if 'Etot' in line:
        split_line = line.split()
        energies.append(float(split_line[2]))
        f_write.write(F'{split_line[2]} \n')
        
f_write.close()

print(f"Done analyzing {filename}")
