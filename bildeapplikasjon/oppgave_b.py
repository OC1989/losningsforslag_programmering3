from PIL import Image
import pilgram

im = Image.open('bilde.jpg')
pilgram.willow(im).save('bilde-med-sort-hvitt-filter.jpg')