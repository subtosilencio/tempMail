# tempMail

[![Build Status](https://travis-ci.org/subtosilencio/tempMail.svg?branch=master)](https://travis-ci.org/subtosilencio/tempMail)
![Python application](https://github.com/subtosilencio/tempMail/workflows/Python%20application/badge.svg)

Get domains used in disposable emails.

```
from tempmail import TempMailScrap

api = TempMailScrap()
api.load("./geckodriver") # loads the selenium's webdriver module of firefox
print(api.get_mail_list()) # get the list of domains
api.close() # close webdriver
```

geckodriver available at:
https://github.com/mozilla/geckodriver/releases/
