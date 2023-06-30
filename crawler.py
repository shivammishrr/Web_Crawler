from googleapiclient.discovery import build
import json
import csv

def scrape_youtube_channels(api_key, cse_id):
    query = 'site:youtube.com openinapp.co'
    num_results = 100

    # A Customsearch API service object
    service = build('customsearch', 'v1', developerKey=api_key)

    youtube_links = []
    start_index = 1
    while start_index <= num_results:
        # Perform Google search and get the JSON response
        response = service.cse().list(
            q=query,
            cx=cse_id,
            start=start_index
        ).execute()
        print(json.dumps(response, indent=4))

        # Find all the search results
        search_results = response.get('items', [])

        for result in search_results:
            url = result['link']
            if 'youtube.com/' in url:
                youtube_links.append(url)

        start_index += 10

    return youtube_links

def save_links_to_json(links):
    with open('youtube_links.json', 'w') as file:
        json.dump(links, file, indent=4)

def save_links_to_csv(links):
    with open('youtube_links.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['YouTube Channel Links'])
        for link in links:
            writer.writerow([link])

# Set up your API key and Custom Search Engine ID
api_key = 'AIzaSyCepbPxdj9muR0UYLb1uFE88vXqC13y75Q'
cse_id = 'b6b7afac2664c444e'

# Scrape YouTube channel links
youtube_links = scrape_youtube_channels(api_key, cse_id)

# Print the extracted links
for link in youtube_links:
    print(link)

# Save the links to JSON file
save_links_to_json(youtube_links)

# Save the links to CSV file
save_links_to_csv(youtube_links)

