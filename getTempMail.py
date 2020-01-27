#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "@subtosilencio on GitHub"

'''
MIT License

A short and simple permissive license with conditions only requiring preservation of
copyright and license notices. Licensed works, modifications, and larger works may
be distributed under different terms and without source code.

Get domains used for disposable emails.

'''

###############################################################################
from tempmail import TempMailScrap


###############################################################################
def main():
    '''
    Get domains used for disposable emails.
    '''
    
    fileName = 'tempMailList.cvs'
    domainsFile = []

    api = TempMailScrap()
    api.load("./geckodriver") # loads the selenium's webdriver module of firefox
    domains = api.get_mail_list() # get the list of domains
    api.close() # close webdriver

    if len(domains) == 0:
        print('Total of Zero domains were colected!')
    else:

        with open(fileName, 'r') as f:
            for line in f:
                domainsFile.append(line.rstrip())
            f.close()

        l = len(domainsFile)

        for domain in domains:
            domain = domain.replace('@','')
            if domain not in domainsFile:
                domainsFile.append(domain)
        
       
        with open(fileName, 'w') as f:
            for domain in sorted(domainsFile):
                f.write(domain+'\n')
            f.close()
        if len(domainsFile) == l:
            print('There was no new domains')
        else:
            print('New emails saved in', fileName)
    
    
###############################################################################
if __name__ == '__main__':
    main()
