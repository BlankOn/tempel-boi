import uuid, string
from datetime import datetime

from django.conf import settings

languages = dict([(item['name'], item) for item in settings.TEMPEL_LANGUAGES])

def get_languages():
    return sorted([(item['name'], item['label'])
                    for item in languages.values()])

def get_language(name):
    return languages[name]['label']

def get_mimetype(name):
    return languages[name]['mime']

def get_extension(name):
    return languages[name]['ext']

def create_token():
    return str(uuid.uuid4()).split('-')[0]

def check_badword(text):
    # Badword filter
    badwords = sorted(set(
        word.strip(string.punctuation)
        for line in open('badwords.txt','r')
        for word in line.split()))

    if any(word in text for word in badwords):
        return True
    else:
        return False
