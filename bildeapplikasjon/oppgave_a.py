from PIL import Image
import pilgram

im = Image.open('bilde.jpg')
pilgram.toaster(im).save('bilde-instagram-filter.jpg')