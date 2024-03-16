import xml.etree.ElementTree as ET

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

# Create the root element
root = ET.Element("data")

# Add data to the XML tree
for item in data:
    province = ET.SubElement(root, "province")
    province_name = ET.SubElement(province, "name")
    province_name.text = item[0]
    population = ET.SubElement(province, "population")
    population.text = item[1]
    percentage = ET.SubElement(province, "percentage")
    percentage.text = item[2]

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write the XML tree to a file
xml_file_path = 'voting_stats.xml'
tree.write(xml_file_path)

print("XML file has been created successfully.")
