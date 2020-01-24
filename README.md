# tempMail

[![Build Status](https://travis-ci.org/subtosilencio/git-lint-validators.svg?branch=master)](https://travis-ci.org/subtosilencio/git-lint-validators)

Get domains used for disposable emails.

```
from tempmail import TempMailScrap

api = TempMailScrap()
api.load("./geckodriver") # loads the selenium's webdriver module of firefox
print(domains = api.get_mail_list()) # get the list of domains
api.close() # close webdriver
```

geckodriver available at:
https://github.com/mozilla/geckodriver/releases/
