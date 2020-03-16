
from  google.cloud import storage

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/user/Desktop/recordfirebase-97cba9d6313b.json"

client = storage.Client(project='https://recordfirebase.firebaseio.com/')

bucket = client.get_bucket('recordfirebase.appspot.com')

blob = storage.Blob('/', bucket)

blob.download_to_filename('C:/Users/user/Desktop/images')