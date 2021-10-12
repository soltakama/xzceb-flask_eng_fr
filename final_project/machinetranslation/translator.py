#import sys
#print(sys.path)

import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)

lt = LanguageTranslatorV3(version='{version}', authenticator = auth)

lt.set_service_url(url)

def englishToFrench(englishText):
    frenchText = lt.translate(text=englishText, model='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    englishText = lt.translate(text=frenchText, model='fr-en').get_result()
    return englishText

