import pandas as pd
import logging
import traceback
import sys

LOG = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.INFO)

def data_load(filepath):
    
    try:
        data = pd.read_csv(filepath,header=None)
        return data
    
    except Exception:
        LOG.error(traceback.format_exc())
        sys.exit(1)
    
    
