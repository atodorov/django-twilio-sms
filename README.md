This is a simple Django application which can send SMS messages using
Twilio's API. 

How to install
--------------

    $ cd my_django_project
    $ git clone https://github.com/atodorov/django-twilio-sms.git twilio_sms
    $ pip install twilio

Then edit `settings.py` to look like this

```
INSTALLED_APPS = (
    # ... skip ...
    'twilio_sms',
)


TWILIO_NUMBER = "+1-my-number"
TWILIO_ACCOUNT_SID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
```

Update DB tables:

    ./manage.py syncdb

How to use
-----------

Fill your DB with some info about users (if need be)

    $ ./manage.py sms_import --help
    Usage: ./manage.py sms_import [options] <filename.csv filename2.csv ...>
    
    Import name/email/number (s) from CSV


Send messages to everyone or just a single number:

    $ ./manage.py send_sms --help
    Usage: ./manage.py send_sms [options] <text> --everyone | <number number ...>
    
    Sends SMS text to the specified number(s) (or everyone)


More info
---------

Pricing info is available at http://www.twilio.com/sms/pricing
