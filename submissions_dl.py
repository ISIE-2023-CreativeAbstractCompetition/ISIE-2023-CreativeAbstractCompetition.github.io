#%%

import requests
import zipfile
import io
import csv
import pandas as pd
import qrcode

# url = 'https://docs.google.com/forms/u/0/d/1GBjuJ3TiFvKU0wa4_NWwCE2Hvo3h9x1X3A_-6bCiRw0/downloadresponses?tz_offset=7200000&sort_by_timestamp=true'
# response = requests.get(url)

# ZIP = "Creative Abstract Competition - ISIE 2023 - Submission form.csv"

# with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
    # with zip_file.open(ZIP) as csv_file:
    #     reader = csv.DictReader(io.TextIOWrapper(csv_file))
    #     rows = [row for row in reader]

submissions_csv = "assets/submissions/Creative Abstract Competition - ISIE 2023 - Submission form.csv"
# with submissions as csv_file:
submissions = pd.read_csv(submissions_csv)
rows = submissions.to_dict('records')

#%%
# Define the HTML template
template = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>{name} - Creative Abstract Competition @ ISIE 2023</title>
  <meta content="This is the official website for the Creative Abstract Competition at ISIE 2023. Submit your abstracts and view entries here!" name="description" />
  <meta content="Creative Abstract Competition, ISIE 2023, Industrial Ecology, Leiden University, abstracts, entries" name="keywords" />
      <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: rgba(0, 0, 0, 0.87);
        }}
        .container {{
            max-width: 75%;
            margin: 0 auto;
            padding: 20px;
            box-sizing: border-box;
            background-color: #fff;
            box-shadow: 0px 0px 10px 0px rgba(255, 255, 255, 0.5);
        }}
        h1, h2, h3, h4 {{
            color: rgb(0, 0, 0);
        }}
        iframe {{
            max-width: 100%;
            height: 500px;
            margin: 20px 0;
        }}

    </style>
  <!-- Favicons -->
  <link href="assets/img/logo_tiny.png" rel="icon" />
  <link href="assets/img/logo_tiny.png" rel="apple-touch-icon" />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet" />
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet" />
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet" />
  <link href="assets/vendor/aos/aos.css" rel="stylesheet" />

  <!-- Template Main CSS File -->
  <link href="../assets/css/main.css" rel="stylesheet" />
  <!-- Custom CSS -->
  <link href="../assets/css/style.css" rel="stylesheet" />

</head>
  <header id="header" class="header d-flex align-items-center fixed-top">
    <div class="container-fluid d-flex align-items-center justify-content-between">
      <a href="../index.html" class="logo d-flex align-items-center me-auto me-lg-0">
        <h1 class="title">Creative Abstract Competition @ ISIE 2023</h1>
      </a>
      <nav id="navbar" class="navbar">
        <ul>
          <li><a href="../index.html" >Home</a></li>
          <li><a href="../about.html">About</a></li>
          <li><a href="../gallery.html"class="active">View entries</a></li>
          <li><a href="../submit.html">Submit</a></li>
          <li><a href="../prizes.html">Prizes</a></li>
          <li><a href="../people.html">People</a></li>
        </ul>
      </nav>

      <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
      <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>
    </div>
  </header>
<body>
  <!-- End Header -->

  <main id="main" data-aos="fade" data-aos-delay="200">
    <div class="page-header d-flex align-items-center">
        <div class="container">
                    <div style="color: black;">
                        <h1 style="color: black; font-size: xlarge;">{title}</h1>
                        <h3>{name}</h3>
                        <h3><strong></strong> {institution}</h3>
                        <h4><strong>ISIE abstract number:</strong> {isie}<br>
                        <strong>Category:</strong> {category}<br>
                        

                        <h4><strong>Creative abstract:</strong></h4>
                        <p style="color: black">{description}</p>

                    </div>
                    <iframe src="https://drive.google.com/file/d/{id}/preview" width="640" height="480" allow="autoplay"></iframe>
                        <h4><strong>Scientific abstract:</strong></h4>
                        <p style="color: black">{abstract}</p>
                    </div>

    </div>
    </div>
    </main>

    
</body>
</html>
"""
#%%
for row in rows:
    path_submissions = "assets/submissions"
    path_html = 'submissions_html'
    entry = f"{path_submissions}/{row['Full name']}_{row['Submission Title']}"
    url = row['Upload your file']
        # Generate the QR code
    img = qrcode.make(url)
    # Save the QR code image to a file
    img.save(row['Full name']+"qrcode.png")

    ID = url.split('&id=')[1].split('&')[0]
    url = f"https://drive.google.com/uc?export=download&id={ID}"



    # Fill in the template with the values from the row
    html = template.format(
        name=row['Full name'],
        title=row['Submission Title'],
        category=row['Submission Category'],
        institution=row['Institution'],
        isie = row['ISIE abstract number'],
        description=row['Short description of creative abstract'],
        abstract=row['Official ISIE abstract'],
        email=row['Email'],
        time=row['Timestamp'],
        iframe_src="../"+entry,
        id = ID
    )



    ID = url.split('&id=')[1].split('&')[0]
    url = f"https://drive.google.com/uc?export=download&id={ID}"


    # response = requests.get(url)
    # with open(entry, 'wb') as f:
    #     f.write(response.content)

        # Write the HTML to a file
    with open(f"{path_html}/{row['Full name']}.html", 'w') as htmlfile:
        htmlfile.write(html)
    
#%%
# # Add all changes to the staging area
# os.system('git add .')

# # Commit the changes with a commit message
# os.system('git commit -m "new submissions"')

# # Push the changes to the remote repository
# os.system('git push')

