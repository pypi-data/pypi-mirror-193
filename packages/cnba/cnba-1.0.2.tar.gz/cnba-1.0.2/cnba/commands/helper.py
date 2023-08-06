import pickle
from console_logging.console import Console
console = Console()
import pandas as pd

def save_pickle(path, data):
    with open(path, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def dict2disk(data, output, columns):
    d1=[]
    for s, t in data.items():
        temp = " ".join(t)
        d1.append([s, len(t), temp])
    d1 = pd.DataFrame(d1)
    d1.columns = columns
    d1.to_csv(output, index=False)


def xintersection(a, b):
    return set.intersection(set(a), set(b))


def xintersection_length(a, b):
    return len(set.intersection(set(a), set(b)))


def split(x, n):
    
    chunks=[]
    # If we cannot split the
    # number into exactly 'N' parts
    if(x < n):
        return [x]
 
    # If x % n == 0 then the minimum
    # difference is 0 and all
    # numbers are x / n
    elif (x % n == 0):
        # console.error([x//n for _ in range(n)])
        return [x//n for _ in range(n)]
    else:
        # upto n-(x % n) the values
        # will be x / n
        # after that the values
        # will be x / n + 1
        zp = n - (x % n)
        pp = x//n
        for i in range(n):
            if(i>= zp):
                chunks.append(pp+1)
            else:
                chunks.append(pp)
        return chunks