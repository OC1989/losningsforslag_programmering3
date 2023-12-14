from PIL import Image
import pilgram

im = Image.open('bilde.jpg')
pilgram._1977(im).save('bilde-instagram-filter.jpg')