import os
from pdf2image import convert_from_path

# Set temporary directory for ImageMagick pixel cache
os.environ['MAGICK_TMPDIR'] = '~/scratch'

# Convert PDF to SVG
dir = 
os.system('pdf2svg netmi.pdf WasteFootprintPoster_ISIE.svg')


# Convert PDF to high-resolution PNG image
images = convert_from_path('WasteFootprintPoster_ISIE.pdf', dpi=200)
image = images[0]

# Save PNG image
image.save('WasteFootprintPoster_ISIE.png', 'PNG')