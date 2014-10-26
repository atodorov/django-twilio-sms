from twilio_sms.models import *
from django.conf import settings
from optparse import make_option
from twilio.rest import TwilioRestClient
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<text> --everyone | <number number ...>'
    help = 'Sends SMS text to the specified number(s) (or everyone)'

    can_import_settings = True

    option_list = BaseCommand.option_list + (
        make_option('--everyone',
                    action='store_true',
                    dest='everyone',
                    default=False,
                    help='Send SMS to everyone'),
                )

    def handle(self, *args, **options):
        i = 0
        text = args[0][:140]

        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


        if options['everyone']:
            send_to = SmsUser.objects.all()
        else:
            send_to = args[1:]

        for number in send_to:
            i += 1

            try:
                _send_sms(client, text, number)
                self.stdout.write('%d SENT TO %s' % (i, number))
            except Exception as e:
                print e.code, e
                raise CommandError("SMS sent failed")



def _send_sms(client, text, number):
    """
        See https://github.com/twilio/twilio-python/pull/189
    """

    # quick hack to make it work with 
    # both QuerySet objects and lists
    if type(number) == SmsUser:
        number = number.number

    message = client.messages.create(body=text, to=number, from_=settings.TWILIO_NUMBER)
