from base64 import b64encode
from base64 import b64decode
import os
from sklearn.datasets import fetch_20newsgroups

dirname="DATA/newsgroup"

os.makedirs( dirname , exist_ok=True  )

#categories to consider:
categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]

remove=()


data_train = fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42,
                                remove=remove)

data_test = fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42,
                               remove=remove)

target_names = data_train.target_names


with open( os.path.join(  dirname, "train_data.tsv"  ) , 'w'  ) as f:
    for doc, label in zip(data_train.data, data_train.target):
        encoded_doc = b64encode( doc.encode() )
        f.write( f"{encoded_doc.decode()  }\t{target_names[label]}\t{label}\n" )
        
with open( os.path.join(  dirname, "test_data.tsv"  ) , 'w'  ) as f:
    for doc, label in zip(data_test.data, data_test.target):
        encoded_doc = b64encode( doc.encode() )
        f.write( f"{encoded_doc.decode()  }\t{target_names[label]}\t{label}\n" )