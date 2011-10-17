"""Simple app to let people query what Rapleaf knows about them directly using email."""
from google.appengine.api import mail
import sys
import logging
from email.utils import parseaddr
from rapleafApi import RapleafApi
import secrets

def get_info(sender):
    """Query the Rapleaf service for info on sender (email address).
    Returns a dictionary of fields (may be empty).

    Email address is parsed first, so it can be in "name <email>" format or just email."""
    email = parseaddr(sender)[1] # Cleanup email address
    api =  RapleafApi(secrets.RAPLEAF_API_KEY)
    try:
        response = api.query_by_email(email)
    except:
        logging.info('Error querying rapleaf %s' % sys.exc_info()[0])
        response = {}
    return response

def build_msg(to, info):
    """Construct and the message about sender with x info (returns the message object)."""
    message = mail.EmailMessage(sender="admin@hueameye.appspotmail.com", subject="Rapleaf info")
    message.to = to
    message.body = """
                   You requested that information rapleaf holds about you.

                   """
    if len(info) == 0:
        message.body += """We got nothing.\n"""
    else:
        for key in info:
            message.body += '%s: %s\n' % (key,info[key])
    return message

def send_reply(sender):
    """Send a reply email with everything that RapLeaf knows about the sender."""
    logging.info('Sending information for %s' % sender)
    info = get_info(sender)
    build_msg(sender, info).send()

