import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)

lt = LanguageTranslatorV3(version='{version}', authenticator = auth)

lt.set_service_url(url)

def englishToFrench(englishText):
    
    return frenchText