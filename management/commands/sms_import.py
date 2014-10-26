from twilio_sms.models import *
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<filename.csv filename2.csv ...>'
    help = 'Import name/email/number (s) from CSV'

    def handle(self, *args, **options):
        i = 0

        for filename in args:
            f = open(filename, 'r')
            for line in f.xreadlines():
                try:
                    i += 1
                    data = line.strip().split(',')
                    name = data[0].strip('"').strip("'").strip()
                    email= data[1].strip('"').strip("'").strip()
                    number=data[2].strip('"').strip("'").strip()

                    # save to database stripping quotes
                    SmsUser.objects.create(
                                        name = name,
                                        email= email,
                                        number = number,
                                    )
                    self.stdout.write('%d IMPORTED %s %s %s' % (i, name, email, number))
                except Exception as e:
                    print e
                    self.stderr.write('%d ERROR IMPORTING %s' % (i, line))
                    continue


            f.close()



