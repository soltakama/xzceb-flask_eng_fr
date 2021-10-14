
import os

import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)

lt = LanguageTranslatorV3(version='2018-05-01', authenticator = auth)

lt.set_service_url(url)

def englishToFrench(englishText):
    if englishText == None:
        
        frenchText = "N/A"
    
    else:
        
        frenchText = lt.translate(text=englishText, model_id='en-fr').get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    if frenchText == None:
        englishText = "N/A"
    else:
        englishText = lt.translate(text=frenchText, model_id='fr-en').get_result()['translations'][0]['translation']
    return englishText

