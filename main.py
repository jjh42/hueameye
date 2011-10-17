from google.appengine.ext import deferred
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import hueameye

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)
        deferred.defer(hueameye.send_reply, mail_message.sender)

def main():
    run_wsgi_app(webapp.WSGIApplication([LogSenderHandler.mapping()]))

if __name__ == "__main__":
    main()
