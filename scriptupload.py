# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:25:40 2020

@author: user
"""



from google.cloud import storage
from firebase import firebase
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/user/Desktop/recordfirebase-97cba9d6313b.json"
firebase=firebase.FirebaseApplication("https://recordfirebase.firebaseio.com/")
client=storage.Client();
bucket=client.get_bucket("recordfirebase.appspot.com")
imageBlob = bucket.blob("/")
#imagePath = [os.path.join(self.path,f) for f in os.listdir(self.path)]
imagePath = "./"

imageBlob = bucket.blob("DSC07832.jpg")
imageBlob.upload_from_filename(imagePath)