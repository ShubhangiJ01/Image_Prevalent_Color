"""
Functionality: Read data from queue and write data in output file.

"""

import csv
import logging
import traceback
import sys

LOG = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)

def listener(output_file,q):
    
    logging.info('writing 3 most prevalent color for an image in output file')
    try:
        with open(output_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['url', 'prevalent_color1', 'prevalent_color2','prevalent_color3'])
            
            while 1:
                m = q.get() #reading from queue
                if m == 'kill': 
                    break
                f.write(m + '\n')
                f.flush()
    except Exception:
        LOG.error(traceback.format_exc())
        sys.exit(1)