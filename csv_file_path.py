import csv

def extract_data_from_csv(csv_file_path):
    """
    Extract data from a CSV file and return it as a list of dictionaries.
    
    :param csv_file_path: Path to the CSV file.
    :return: List of dictionaries containing the data from the CSV file.
    """
    data = []
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File '{csv_file_path}' does not exist.")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

# Example usage:
csv_file_path = 'voting_stats.csv'
extracted_data = extract_data_from_csv(csv_file_path)
print(extracted_data)
