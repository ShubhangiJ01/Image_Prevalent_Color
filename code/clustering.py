"""
Functionality: Applying KMeans++ on an image

"""

import sklearn.cluster
import logging

from DominantColor import most_frequent

LOG = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)
logf = open("error.log", "w") 

def KmeansPlus(ar,url,q):
    
    try:
        logging.info('KMeans++ initialization')    
        num_clusters = 10
        kmeans = sklearn.cluster.KMeans(n_clusters=num_clusters,
                                        init="k-means++",max_iter=20,
                                        random_state=1000).fit(ar)
        codes = kmeans.cluster_centers_ 
        most_frequent(ar,codes,url,q) #calling function to identify most dominant color
    
    except Exception as e:
        logf.write("Failed to segmenting image through clustering {0}: {1}\n".format(str(url), str(e)))     
        
    
