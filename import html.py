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

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Voting Statistics</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>Province</th>
            <th>Population</th>
            <th>Percentage</th>
        </tr>
"""

# Add data to the HTML table
for row in data:
    html_content += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
        </tr>
"""

# Close the HTML content
html_content += """
    </table>
</body>
</html>
"""

# Write the HTML content to a file
html_file_path = 'voting_stats.html'
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

print("HTML file has been created successfully.")
