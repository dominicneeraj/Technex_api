import datetime
from nltk import pos_tag, ngrams
from nltk.tokenize import RegexpTokenizer
import vaderSentiment as sentiment
from dateparser import parse
from datetime import datetime

import datetime

data = [(1, 'today'), (2, 'yesterday'), (1, 'last'), (1, 'days'), (1, 'day'), (30, 'months'), (30, 'month'),
        (365, 'years'), (365, 'years'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
        (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13')]
datedata = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','january','jan',
            'february','feb','march','mar','april','apr','may','june','july','jul','august','aug','september','sept','october','oct','november','nov','december', 'dec','day', 'days',
            'today', 'yesterday','Yesterday','Yesterdays', 'last','past', 'this', 'next', 'months', 'years',
            'weeks', 'week', 'month','year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22','23', '24', '25', '26', '27', '28', '29', '30', '31','1st', '2nd',
            '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
actualdate = ['today', 'yesterday','Yesterday','Yesterdays', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
              'january','jan',
            'february','feb','march','mar','april','apr','may','june','july','jul','august','aug','september','sept','october','oct','november','nov','december', 'dec', 'day', 'days',
              'months', 'years',
              'weeks', 'week', 'month','year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22','23', '24', '25', '26', '27', '28', '29', '30', '31', '1st',
              '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th']
text = "Mails sent by bnrao@gmail.com last 30 days"
#tagged_sent = pos_tag(text.split())


def dateparser(text):
    tokenizer = RegexpTokenizer(r'\w+')
    wordtoken = tokenizer.tokenize(text)
    bi_grams = list(ngrams(wordtoken, 2))
    tri_grams = list(ngrams(wordtoken, 3))
    tagged_sent = pos_tag(text.split())

    out = []
    w = []
    for word in wordtoken:
        for d in datedata:
            if word.lower() == d:
                w.append(word)
    if w:
     st = ' '.join(w)
     print st
    else:
        st='Any'
    # r=reduce(lambda x, y: x * y, out)
    # print st
    # print r
    return st


def date(text):
    w = []
    k='Any'
    date = dateparser(text)
    if date=='Any':
        return 'Any'
    elif date in ['last week','Last week']:
        return 'Today-'+'' +str(7) + ' '+ 'days'
    elif date in ['last night','Last night']:
        return 'Today-' + '' + str(1) + ' ' + 'days'
    elif date in ['before yesterday', 'Before yesterday']:
        return 'Today-' + '' + str(2) + ' ' + 'days'
    elif date in['last month','Last month']:
        return 'Today-' + '' + str(30) + ' ' + 'days'
    elif date in ['last year', 'Last year']:
        return 'Today-' + '' + str(365) + ' ' + 'days'
    else:
     tokenizer = RegexpTokenizer(r'\w+')
     wordtoken = tokenizer.tokenize(date)
     for word in wordtoken:
        if word.lower() in actualdate:
            w.append(word)


     st = ' '.join(w)
     dat = (parse(st))

     string = dat.strftime('%m/%d/%Y')

     date_format = "%m/%d/%Y"
     end_date = datetime.datetime.strptime(string, date_format)
     today = datetime.datetime.today()
     k=abs((end_date - today).days)
     if k>1:
        return 'Today-'+'' +str(k-1) + ' '+ 'days'
     else:
         return 'Today'
