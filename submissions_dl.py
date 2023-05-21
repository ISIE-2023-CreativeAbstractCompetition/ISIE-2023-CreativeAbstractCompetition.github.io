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
    <link href="assets/css/main.css" rel="stylesheet">
    <title>{title}</title>

</head>
<body class="col-lg-10 text-center" style="background-color:rgba(0, 0, 0, 0.87)">
    <h1 style="color:white">{title}</h1>
    <h2 style="color:white">{name}</h2>
    <h4 style="color:white"><strong>Institution:</strong> {institution}</h4>
    <h4 style="color:white"><strong>Description:</strong> {description}</h4>
    <img src="{image}" alt="{title}" style="box-shadow: 0px 0px 10px 0px rgba(255, 255, 255, 0.5); padding: 10px;">
    <h4 style="color:white"><strong>Abstract:</strong><h4>
    <p style="color:white">{abstract}</p>
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
    

# Add all changes to the staging area
os.system('git add .')

# Commit the changes with a commit message
os.system('git commit -m "new submissions"')

# Push the changes to the remote repository
os.system('git push')

