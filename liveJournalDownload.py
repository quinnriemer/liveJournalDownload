import requests

# Ask the user for a URL
url = input("Enter a URL: ")

# Strip anything after 'skip=' in the URL
url = url.split("skip=")[0] + "skip="

# Ask the user for a maximum value to iterate up to
max_value = int(input("Enter the maximum value to iterate up to: "))

# Iterate over the skip values
for i in range(0, max_value + 1, 20):
    # Construct the full URL
    full_url = url + str(i)
    
    # Send a GET request
    response = requests.get(full_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Define the filename
        filename = f"page_{i//20}.html"
        
        # Write the content to a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
            
        print(f"Saved {full_url} to {filename}")
    else:
        print(f"Failed to fetch {full_url}")

# Now you will have html files named page_0.html, page_1.html, ..., up to page_{max_value//20}.html

