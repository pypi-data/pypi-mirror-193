import wikipedia
import csv

# Set the Wikipedia language to English
wikipedia.set_lang("en")

# Get a list of all Wikipedia page titles
all_titles = wikipedia.page("Special:AllPages").links

# Create a list to store the input and label values
data = []

# Loop through all Wikipedia page titles and get the first 4 lines of each page's content
for title in all_titles:
    try:
        page = wikipedia.page(title)
        content_lines = page.content.split('\n')[:4]
        content = ' '.join(content_lines)
        data.append((title, content))
        print(f"Retrieved article: {title}")
    except wikipedia.exceptions.DisambiguationError:
        pass
    except wikipedia.exceptions.PageError:
        pass

# Write the data to a CSV file
with open('wikipedia_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    writer.writerow(['input', 'label'])
    writer.writerows(data)
    print("Wrote To CSV")
