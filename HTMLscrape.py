import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://www.elections.org.za/pw/StatsData/Voter-Registration-Statistics'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the specific data you want to extract using BeautifulSoup methods like find() or find_all()
    # For example, if you want to extract all the <div> elements with a class of 'container', you can use:
    containers = soup.find_all('div', class_='container')

    # Process the extracted data as needed
    for container in containers:
        # Extract specific information from each container
        # For example, you might extract text or attributes using container.text or container['attribute_name']
        print(container.text)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
