import os
import argparse
import pickle
from base64 import b64encode, b64decode
import pandas as pd
import numpy as np

def size_mb(docs):
    return sum(len(s.encode('utf-8')) for s in docs) / 1e6

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #Input-output:
    parser.add_argument("--filename", dest="filename",
                        help="path to the test data (file with at each line a base64 encoded document", required=True)
    parser.add_argument("--model_path", dest="model_path",
                        help="path to the classfier (python pickle format)", required=True)
    parser.add_argument("--output_file", dest="output_file",
                        help="output file with predicted labels", required=True)
    args = parser.parse_args()
    
    test_data=open( args.filename , 'r'  ).read().rstrip("\n").split("\n")
    
    test_data=[ b64decode( doc ).decode()  for doc in test_data  ]

    data_test_size_mb = size_mb(test_data)

    print("%d documents - %0.3fMB (test set)" % (
        len(test_data), data_test_size_mb))
    print()
    
    #load the classifier 

    clf = pickle.load( open(  args.model_path  , "rb" ) )

    #classify with the classifier
    
    pred=clf.predict( test_data  )
    
    os.makedirs(  os.path.dirname( args.output_file ) , exist_ok=True  )
    
    with open(  args.output_file ,  "w"  ) as fp:
        for pred_label in pred:
            fp.write( f"{pred_label}\n"     )