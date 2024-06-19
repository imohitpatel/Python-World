import json
import string
import random
import os

# Define the filename for storing URL mappings
FILE_NAME = "url_mappings.json"

# Function to generate a random string of fixed length
def generate_short_id(num_of_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

# Load URL mappings from file
def load_mappings():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return {}

# Save URL mappings to file
def save_mappings(mappings):
    with open(FILE_NAME, 'w') as file:
        json.dump(mappings, file)

# Shorten a URL
def shorten_url(original_url):
    mappings = load_mappings()
    if original_url in mappings:
        return mappings[original_url]
    else:
        short_id = generate_short_id()
        while short_id in mappings.values():
            short_id = generate_short_id()
        mappings[original_url] = short_id
        save_mappings(mappings)
        return short_id

# Resolve a short URL to the original URL
def resolve_url(short_id):
    mappings = load_mappings()
    for original_url, sid in mappings.items():
        if sid == short_id:
            return original_url
    return None

# Command-line interface
def main():
    while True:
        print("\n1. Shorten URL")
        print("2. Resolve URL")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            original_url = input("Enter the URL to shorten: ")
            short_id = shorten_url(original_url)
            print(f"Short URL is: {short_id}")

        elif choice == '2':
            short_id = input("Enter the short URL ID: ")
            original_url = resolve_url(short_id)
            if original_url:
                print(f"Original URL is: {original_url}")
            else:
                print("Short URL not found.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
