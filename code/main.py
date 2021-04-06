"""
Functionality: Identify 3 most prevalent color in an image.

Change 1:
Images are loaded from corresponding URL. Multiprocessing pool 
is created based on number of cores of CPU. Queue is created to
provide write access to single processor for generating output file.

"""

import sys
import multiprocessing
import traceback
import logging

from DataLoader import data_load
from SamplePreprocessing import preprocessing
from output import listener

LOG = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)

OUTPUT_FILE = sys.argv[2]

def main(filepath):
    
    manager = multiprocessing.Manager()
    pool = multiprocessing.Pool(multiprocessing.cpu_count()+2)
    
    ##To give write access to only one process for output file
    q = manager.Queue() 
    watcher = pool.apply_async(listener, args=(OUTPUT_FILE,q,))
    jobs = []
    
    try:
        logging.info('Calling data loader')
        data = data_load(filepath)
    except Exception:
        LOG.error(traceback.format_exc())
        sys.exit(1)
    
    try:
        ## loop to process each image url using multiprocessing
        for row in range(len(data)):
            job = pool.apply_async(preprocessing, args=(data[0][row],q,))
            jobs.append(job) #appending result to be used by queue manager
                                
        for job in jobs: 
            job.get()

        #now we are done, kill the listener
        q.put('kill')
        pool.close()
        pool.join()    
    
    except Exception:
        LOG.error(traceback.format_exc())
        sys.exit(1)
    
if __name__ == '__main__':
    main(sys.argv[1])
    