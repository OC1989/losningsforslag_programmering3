from PIL import Image

input_path = "bilde.jpg"

print("Velg rotasjonsretning:")
print("1. 90 grader med klokka")
print("2. 90 grader mot klokka")
print("3. 180 grader")

rotation_choice = int(input("Valg: "))

im = Image.open(input_path)

if rotation_choice == 1:
    rotated_im = im.rotate(-90, expand=True)
    output_path = input("Skriv inn sti til det roterte bildet: ")
    rotated_im.save(output_path)

elif rotation_choice == 2:
    rotated_im = im.rotate(90, expand=True)
    output_path = input("Skriv inn sti til det roterte bildet: ")
    rotated_im.save(output_path)

elif rotation_choice == 3:
    rotated_im = im.rotate(180, expand=True)
    output_path = input("Skriv inn sti til det roterte bildet: ")
    rotated_im.save(output_path)

else:
    print("Ugyldig valg. Avslutter programmet.")