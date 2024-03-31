import pandas as pd 
import numpy as np 
import seaborn as sns 
import torch 
from docarray import DocList, BaseDoc
from docarray.index import HnswDocumentIndex

from docarray.typing import ImageUrl, ImageTensor, NdArray

class ImageDoc(BaseDoc):
    url: ImageUrl
    tensor: ImageTensor
    embedding: NdArray[128]


# create some data
dl = DocList[ImageDoc](
    [
        ImageDoc(
            url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Alpamayo.jpg",
            tensor=np.zeros((3, 224, 224)),
            embedding=np.random.random((128,)),
        )
        for _ in range(100)
    ]
)

# create a Document Index
index = HnswDocumentIndex[ImageDoc](work_dir='/tmp/test_index2')


# index your data
index.index(dl)

# find similar Documents
query = dl[0]
results, scores = index.find(query, limit=10, search_field='embedding')


print(results, scores)