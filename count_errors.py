import os

# Function to extract IDs from lines starting with 'Event:'
def extract_ids(line):
    if line.startswith('Event: '):
        event_text = line[len('Event: '):].strip()
        comma_index = event_text.find(',')
        if comma_index != -1:
            return event_text[:comma_index]
    return None

# Iterate through files starting with 'error_logs'
def process_files():
    unique_ids = set()

    for filename in os.listdir('.'):
        if filename.startswith('error_logs'):
            with open(filename, 'r') as file:
                for line in file:
                    extracted_id = extract_ids(line)
                    if extracted_id:
                        unique_ids.add(extracted_id)

    with open('id_aggregates.txt', 'w') as output_file:
        for unique_id in unique_ids:
            output_file.write(unique_id + '\n')

    return len(unique_ids)

if __name__ == '__main__':
    total_unique_ids = process_files()
    print(f"Total unique IDs aggregated: {total_unique_ids}")
