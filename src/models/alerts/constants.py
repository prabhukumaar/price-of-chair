__author__ = 'jslvtr'
import os

URL = os.environ.get('MAILGUN_URL')             #"https://api.mailgun.net/v3/<>.mailgun.org/messages"
API_KEY = os.environ.get('MAILGUN_API_KEY')     #"key-<>"
FROM = os.environ.get('MAILGUN_FROM')           #"Mailgun Sandbox <postmaster@<>.mailgun.org>"
ALERT_TIMEOUT = 10
COLLECTION = "alerts"