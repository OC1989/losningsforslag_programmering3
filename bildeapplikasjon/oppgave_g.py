from PIL import Image, ImageOps

input_path = "bilde.jpg"
polaroid_frame_path = "polaroid-frame-PNG-6.png"
output_path = "bilde-polaroid.jpg"

# Åpne bildet
original_image = Image.open(input_path)

# Beskjær til 1:1 høyde-breddeforhold
cropped_image = ImageOps.fit(original_image, (min(original_image.size), min(original_image.size)))

# Skaler bildet til passende størrelse for den polaroide fotorammen (760x760)
scaled_image = cropped_image.resize((760, 760))

# Åpne polaroid-ramme PNG-filen
polaroid_frame = Image.open(polaroid_frame_path)

# Opprett en ny bildebeholder med hvit bakgrunn. Et canvas.
frame_image = Image.new("RGB", (880, 1048), "white")

# Legg til polaroid-rammen på toppen
frame_image.paste(polaroid_frame)

# Legg til den skalerte bildet i bildebeholderen med en offset på 64 piksler i x- og y-retning
frame_image.paste(scaled_image, (64, 64))

# Lagre det endelige bildet
frame_image.save(output_path)