
N_COLS = 1024
N_ROWS = 1024

LONG_SLIT_EDGE_MARGIN = 6

starting_order = {'NIRSPEC-1': 80, 'NIRSPEC-2': 70, 'NIRSPEC-3': 67, 'NIRSPEC-4': 61, 
                  'NIRSPEC-5': 53, 'NIRSPEC-6': 49, 'NIRSPEC-7': 41 }

def get_starting_order(filtername):
    return starting_order[filtername.upper()]

order_edge_peak_thresh = {'NIRSPEC-1': 300, 'NIRSPEC-2': 300, 'NIRSPEC-3': 300, 
                'NIRSPEC-4': 600, 'NIRSPEC-5': 600, 'NIRSPEC-6': 500, 'NIRSPEC-7': 100 }

def get_order_edge_peak_thresh(filtername):
    return order_edge_peak_thresh[filtername.upper()]






    