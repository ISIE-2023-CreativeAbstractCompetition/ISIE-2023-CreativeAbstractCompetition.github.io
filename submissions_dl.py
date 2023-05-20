#%%

import requests
import zipfile
import io
import csv

url = 'https://docs.google.com/forms/u/0/d/1GBjuJ3TiFvKU0wa4_NWwCE2Hvo3h9x1X3A_-6bCiRw0/downloadresponses?tz_offset=7200000&sort_by_timestamp=true'
response = requests.get(url)


ZIP = "Creative Abstract Competition - ISIE 2023 - Submission form.csv"

with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
    with zip_file.open(ZIP) as csv_file:
        reader = csv.DictReader(io.TextIOWrapper(csv_file))
        rows = [row for row in reader]

#%%
# Define the HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <h2>{name}</h2>
    <img src="{image}" alt="{title}">
    <ul>
        <li><strong>Category:</strong> {category}</li>
        <li><strong>Institution:</strong> {institution}</li>
        <li><strong>Description:</strong> {description}</li>
        <li><strong>Abstract:</strong> {abstract}</li>
        <li><strong>Email:</strong> {email}</li>
        <li><strong>Time:</strong> {time}</li>
    </ul>
</body>
</html>
"""
#%%
for row in rows:
    path_submissions = "assets/submissions"
    path_html = 'submissions_html'
    jpg = f"{path_submissions}/{row['Full name']}_{row['Submission Title']}.jpg"
    url = row['Upload your file']

    # Fill in the template with the values from the row
    html = template.format(
        name=row['Full name'],
        title=row['Submission Title'],
        category=row['Submission Category'],
        institution=row['Institution'],
        description=row['Short description of creative abstract'],
        abstract=row['Official ISIE abstract'],
        email=row['Email'],
        time=row['Tijdstempel'],
        image="../"+jpg
    )



    ID = url.split('&id=')[1].split('&')[0]
    url = f"https://drive.google.com/uc?export=download&id={ID}"
    response = requests.get(url)
    
    with open(jpg, 'wb') as f:
        f.write(response.content)

        # Write the HTML to a file
    with open(f"{path_html}/{row['Full name']}.html", 'w') as htmlfile:
        htmlfile.write(html)
    



            # name = row['Name']
            # link = row['Link']
            # print(f"Name: {name}, Link: {link}")



#%%