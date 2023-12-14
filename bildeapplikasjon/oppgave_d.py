from PIL import Image

input_bilde = "bilde.jpg"
ny_bredde = 1080
output_bilde = input("Skriv inn et navn på den nye filen: ")

# Åpne bildet
bilde = Image.open(input_bilde)

# Endre størrelsen på bildet ved å bruke Thumbnail-funksonen i Pillow. Thumbnual gjør at bredde- og høydeforhold holder seg inntakt.
bilde.thumbnail((ny_bredde, ny_bredde))

# Lagre det endrede bildet
bilde.save(output_bilde)

print(f"Bilde endret og lagret som {output_bilde}")