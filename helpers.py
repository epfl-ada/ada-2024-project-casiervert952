"""Some helper functions for project"""

import csv
import os
import numpy as np

def txt_to_csv(file_txt, file_csv):

    data = []
    data_line = []
    iteration = 0

    # If the file already exist, just delete it
    if os.path.exists(file_csv):
        os.remove(file_csv)

    # Let start by oppening the input and output files
    with open(file_txt, 'r', encoding='utf-8') as file:
        with open(file_csv, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Take line by line
            for line in file:
                line = line.strip()

                # If the line is empty, change the rating element
                if line == "":

                        # Write the rating elements each 10'000
                        if iteration % 10000 == 0:
                            writer.writerows(data)
                            data = []
                        else:
                            data.append(data_line)
                        
                        iteration += 1
                        print(f"Itération : {iteration}")
                        data_line = []
                # Else add the feature to the in growing line, and supress the feature prefix
                else:
                    parts = line.split(": ")
                    if parts[0] == "text:":
                        data_line.append("")
                    else:
                        data_line.append(parts[1])
        # Add the remaining data to the csv file
        if data:
                writer.writerows(data)

        print("Data have been placed in + " + file_csv)


file_txt = 'data/RateBeer/ratings.txt'
file_csv = 'data/RateBeer/ratings2.csv'

txt_to_csv(file_txt, file_csv)
