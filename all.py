import requests
import zipfile
import io
import csv
import pandas as pd
import qrcode
import pdfkit

# Load the submissions from the CSV file
submissions_csv = "assets/submissions/Creative Abstract Competition - ISIE 2023 - Submission form.csv"
submissions = pd.read_csv(submissions_csv)
rows = submissions.to_dict('records')

# Define the HTML template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>{title}</title>
  <style>
    body {{
      font-family: serif;
      font-size: 22px;
      line-height: 1.2;
      text-align: center;
      margin: 1.0em;
    }}
    h1 {{
      font-size: 46px;
      margin-top: 2em;
      margin-bottom: 0.2em;
    }}
    h2 {{
      font-size: 34px;
      margin-top: 0.5em;
      margin-bottom: 0.2em;
    }}
    h3 {{
      font-size: 30px;
      margin-top: 1em;
      margin-bottom: 0.2em;
    }}
    p {{
      font-size: 25px;
      margin-top: 0.5em;
      margin-bottom: 0.5em;
    }}
    iframe {{
      margin-top: 1em;
      margin-bottom: 1em;
    }}
    img {{
      margin-top: 1em;
      margin-bottom: 1em;
    }}
    .page-break {{
      page-break-after: always;
    }}
  </style>
</head>
<body>
  <h1>{name}</h1>
  <h2>{institution}</h2>
  <h3>ISIE abstract number: {isie}</h3>
  <h3>Category: {category}</h3>
  <h3>Creative abstract description:</h3>
  <p>{description}</p>
  <h3>Official ISIE abstract:</h3>
  <p>{abstract}</p>
  <div class="page-break"></div>
</body>
</html>
"""

# Create a list to hold the HTML for each entry
html_list = []

# Loop over the rows and generate the HTML for each entry
for row in rows:

    # Fill in the template with the values from the row
    html = template.format(
        name=row['Full name'],
        title=row['Submission Title'],
        category=row['Submission Category'],
        institution=row['Institution'],
        isie=row['ISIE abstract number'],
        description=row['Short description of creative abstract'],
        abstract=row['Official ISIE abstract'],
    )

    # Add the HTML to the list
    html_list.append(html)
    html_list.append('<div class="page-break"></div>')

# Join all the HTML strings into one string
all_html = '\n'.join(html_list)

# Write the HTML to a file
with open('all.html', 'w') as htmlfile:
    htmlfile.write(all_html)

# Convert the HTML to PDF
options = {
    'page-size': 'A3',
    # 'orientation': 'Landscape',
}
pdfkit.from_file('all.html', 'all.pdf', options=options)