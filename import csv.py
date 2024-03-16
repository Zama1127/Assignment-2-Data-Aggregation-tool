import csv

# Data to be written to the CSV file
data = [
    ['Eastern Cape  3,439,325  12.41%'],
    ['0  Free State  1,456,935   5.26%'],
    ['1  Gauteng  6,542,033   23.6%'],
    ['2  KwaZulu Natal  5,738,272  20.7%']
    ['3  Mpumalanga  2,025,074    7.3%']
    ['4  Northern Cape    656,831   2.37%']
    ['5  Limpopo  2,779,668  10.03%']
    ['6  North West  1,768,580   6.38%']
    ['7  Western Cape  3,317,102  11.96%']
]

# File path to the CSV file
csv_file_path = 'voting.stats.csv'

# Writing data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

    data = ['2  Kwazulu-natal  5,738,272  20.7%']
components = data[0].split()  # Splitting the string by whitespace
print(components)


print(data[0])  # Accessing the first element of the list

print(f'Data has been successfully written to {csv_file_path}')


