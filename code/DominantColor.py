"""
Functionality: Count pixels associated with each cluster centroid. 
Converting top 3 count occurence color into hexa value and adding
value to queue manager to be used to write in output file.

"""

import numpy
import scipy.cluster
import binascii
import logging

LOG = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)
logf = open("error.log", "w") 

def most_frequent(ar,codes,url,q):
    
    try:
        logging.info('Identifying 3 most prevalent color in an image')
        
        vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign cluster centroid
        counts, bins = numpy.histogram(vecs, len(codes))    # count occurrences
        ind = counts.argsort()[-3:][::-1] # identifying top 3 count occurrences
        
        res = url
        for index_max in ind:
            peak = codes[index_max]
            colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii') # converting to hexadecimal 
            res += ',' + colour
        
        q.put(res) #adding in the queue
        
        return res
    except Exception as e:
        logf.write("Error in counting dominant color {0}:{1}\n".format(str(url) , str(e)))
        

    
