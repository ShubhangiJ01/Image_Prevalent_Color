"""
Functionality: Resizing the image to reduce the time

"""

import requests
import numpy
from PIL import Image

from clustering import KmeansPlus

logf = open("error.log", "w") 

def preprocessing(url,q):
    
    image = Image.open(requests.get(url, stream=True).raw)   
    try:
        
        image = image.resize((150, 150))      #to reduce time
        ar = numpy.asarray(image)
        shape = ar.shape
        ar = ar.reshape(numpy.product(shape[:2]), shape[2]).astype(float)
        KmeansPlus(ar,url,q) #calling clustering algorithm
    
    except Exception as e:     
        logf.write("Failed to preprocess image {0}: {1}\n".format(str(url), str(e)))
        