import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)

lt = LanguageTranslatorV3(version='2018-05-01', authenticator = auth)

lt.set_service_url(url)

def english_to_french(english_text):
    if english_text is None:
        french_text = "N/A"
    else:
        french_text = lt.translate(text=english_text, model_id='en-fr').get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    if french_text is None:
        english_text = "N/A"
    else:
        english_text = lt.translate(text=french_text, model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text
