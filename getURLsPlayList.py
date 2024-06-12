from bs4 import BeautifulSoup
import csv

file_name = 'playlist.html'

# Read HTML
with open(file_name, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create Object BeautifulSoup to Check HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find links with class "video-link"
video_links = soup.find_all('a', class_='video-link')

# Extract href from each link and save it to a list
hrefs = [link.get('href') for link in video_links if link.get('href')]

# Save YT links in a CSV file
with open('playlistLinks.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Links'])  # Write CSV column name
    for href in hrefs:
        csvwriter.writerow([href])

print(f'{len(hrefs)} links have been saved in the file playlistLinks.csv')