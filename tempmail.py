from selenium import webdriver


__author__ = "@subtosilencio on GitHub"


"""
MIT License

A short and simple permissive license with conditions only requiring preservation of
copyright and license notices. Licensed works, modifications, and larger works may
be distributed under different terms and without source code.

"""


class TempMailScrap:
    def __init__(self):
        self.driver = None

    def load(self, firefox_binary_location, geckodriver_location = "./geckodriver"):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=geckodriver_location)

    def get_mail_list(self):
        self.driver.get('https://temp-mail.org/en/change')   
        return self.driver.execute_script("return Mails.domains;")
    
    def close(self):
        try:
            self.driver.close()
            self.driver.quit()
        except:
            pass
