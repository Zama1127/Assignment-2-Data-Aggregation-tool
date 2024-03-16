from openpyxl import Workbook

# Provided data
data = [
    ["Eastern Cape", "3,439,325", "12.41%"],
    ["Free State", "1,456,935", "5.26%"],
    ["Gauteng", "6,542,033", "23.6%"],
    ["Kwazulu-natal", "5,738,272", "20.7%"],
    ["Mpumalanga", "2,025,074", "7.3%"],
    ["Northern Cape", "656,831", "2.37%"],
    ["Limpopo", "2,779,668", "10.03%"],
    ["North West", "1,768,580", "6.38%"],
    ["Western Cape", "3,317,102", "11.96%"]
]

# Create a new workbook
wb = Workbook()
ws = wb.active

# Add data to the worksheet
ws.append(["Province", "Population", "Percentage"])
for row in data:
    ws.append(row)

# Save the workbook
xlsx_file_path = 'voting_stats.xlsx'
wb.save(xlsx_file_path)

print("XLSX file has been created successfully.")
