from os.path import exists
from model import creating
from model import writing_scv
from model import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt() 