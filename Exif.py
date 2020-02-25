print('test feature')


import Pillow_master
#from PIL.ExifTags import TAGS

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

exif = get_exif('image.jpg')
labeled = get_labeled_exif(exif)
print(labeled)


#https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3
