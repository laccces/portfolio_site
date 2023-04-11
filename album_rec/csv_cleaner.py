import csv

input_file = 'input.csv'
output_file = 'output.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)

        for row in reader:
            for cell in row:
                # Split at the first hyphen
                part1, part2 = cell.split(' – ', 1)

                # Split at the first pair of brackets and remove them
                part2, part3 = part2.split(' (', 1)
                part3 = part3.rstrip(')')

                # Write the split data to the output CSV file
                writer.writerow([part1, part2, part3])
