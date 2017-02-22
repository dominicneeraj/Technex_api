import string

import re
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer
from decimal import Decimal

from numpy.core.defchararray import isdigit
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer

def isto(item,text):
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    # print newtext
    tagged_sent = pos_tag(text.split())
    #print tagged_sent
    bi_grams = list(ngrams(newtext, 2))
    propernouns = [word for word, po in tagged_sent if po in ['TO']]
    #print propernouns
    if item in propernouns:
        return True
    else:
        return False
def isnoun(item,text):
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    # print newtext
    tagged_sent = pos_tag(text.split())
    #print tagged_sent
    bi_grams = list(ngrams(newtext, 2))
    propernouns = [word for word, po in tagged_sent if po in ['NNP', 'NN', 'VB', 'PRP', 'JJ']]
    #print propernouns
    if item in propernouns:
        return True
    else:
        return False
def istonoun(item,text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokenizer = RegexpTokenizer(r'\w+')
    formated_text = tokenizer.tokenize(text)
    newtext = [w.replace("CC'd", "CC") for w in formated_text]
    if 'd' in newtext: newtext.remove('d')
    if 'CC' in newtext: newtext.remove('CC')
    #print newtext


    textnew="".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in newtext]).strip()
    #print textnew
    tagged_sent = pos_tag(textnew.split())
    #print tagged_sent
    bi_grams = list(ngrams(newtext, 2))
    propernouns = [word for word, po in tagged_sent if po in ['NNP', 'NN', 'VB', 'PRP', 'JJ']]
    #print propernouns
    if item in propernouns:
        return True
    else:
        return False


def isconj(item,text):
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    # print newtext
    tagged_sent = pos_tag(text.split())
    #print tagged_sent
    bi_grams = list(ngrams(newtext, 2))
    conjunctions = [word for word, po in tagged_sent if po in ['CC']]
    #print propernouns
    if item in conjunctions:
        return True
    else:
        return False

def getFeature(text,feature):
    val = ''
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    # print newtext
    tagged_sent = pos_tag(text.split())
    # print tagged_sent
    bi_grams = list(ngrams(newtext, 2))
    # print bi_grams
    tri_grams = list(ngrams(newtext, 3))
    # print tri_grams
    uni_grams = list(ngrams(newtext, 1))
    # print uni_grams
    next_to = [w for word, w in bi_grams if word in feature]
    # print next_to
    if not next_to:
        val = 'Any'
        return val
    else:
        val = next_to[0]
        va = next_to[0]

    for item in newtext:
        # print item
        # print text
        if isnoun(item, text) == True and newtext.index(item) > newtext.index(va):
            val = val + ' ' + item
        elif isconj(item, text) == True and newtext.index(item) > newtext.index(va):
            continue
        elif isconj(item, text) == False and newtext.index(item) > newtext.index(va):
            break
        elif isnoun(item, text) == False and newtext.index(item) > newtext.index(va):
            break
        else:
            continue

    return val






def getFrom(text):
    val = ''
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    #print newtext
    tagged_sent = pos_tag(text.split())
    # print tagged_sent
    bi_grams = list(ngrams(newtext, 2))
    # print bi_grams
    tri_grams = list(ngrams(newtext, 3))
    # print tri_grams
    uni_grams = list(ngrams(newtext, 1))
    # print uni_grams
    next_to = [w for word, w in bi_grams if word in ['From','from','by']]
    #print next_to
    if not next_to:
        for i in newtext:
            if nextstring(i, text) == 's':
             print 'done'
             #print i
             return i
            else:
                val='Any'

    else:
      val = next_to[0]
      va = next_to[0]

      for item in newtext:
        #print item
        # print text
        if isnoun(item, text) == True and newtext.index(item) > newtext.index(va):
            val = val + ' ' + item
        elif isconj(item, text) == True and newtext.index(item) > newtext.index(va):
            continue
        elif isconj(item, text) == False and newtext.index(item) > newtext.index(va):
            break
        elif isnoun(item, text) == False and newtext.index(item) > newtext.index(va):
            break
        else:
            continue

    return val


def getTo(text):
    v=''
    val = ''
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    formated_text = [w.replace("CC'd", "CC") for w in newtext]
    if 'd' in formated_text: formated_text.remove('d')
    #print formated_text
    tagged_sent = pos_tag(text.split())
    #print tagged_sent
    bi_grams = list(ngrams(formated_text, 2))
    #print bi_grams
    tri_grams = list(ngrams(formated_text, 3))
    # print tri_grams
    uni_grams = list(ngrams(formated_text, 1))
    # print uni_grams
    next_to = []
    for a,b in bi_grams:
        if b in['to','To'] and a not in['cc','CC','CC`d']:
            next_to.append(b)

    #print next_to
    if next_to:
       #print True
       va = next_to[0]

       for item in newtext:
         val=''
        # print item
        # print text
         if istonoun(item, text) == True and newtext.index(item) > newtext.index(va)and (newtext.index(item)-newtext.index(va))in[1,2,3]:
            val = val + ' ' + item
            v=v+val
         elif isconj(item, text) == True and newtext.index(item) > newtext.index(va):
            continue
         elif isconj(item, text) == False and newtext.index(item) > newtext.index(va):
             break
         elif istonoun(item, text) == False and newtext.index(item) > newtext.index(va):
             break
         else:
            continue

    else:
        v = 'Any'

    return v


def getCC(text):
    val = ''
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    formated_text = [w.replace("CC'd", "CC") for w in newtext]
    if 'd' in formated_text: formated_text.remove('d')
    #print formated_text
    tagged_sent = pos_tag(text.split())
    #print tagged_sent
    bi_grams = list(ngrams(formated_text, 2))
    # print bi_grams
    tri_grams = list(ngrams(formated_text, 3))
    # print tri_grams
    uni_grams = list(ngrams(formated_text, 1))

    # print uni_grams
    next_to = []
    next_cc = []
    for a, b in bi_grams:
        if a in ['cc', 'CC'] and b in ['to','To']:
            next_to.append(b)
            next_cc.append(a)
            break
        elif a in ['cc', 'CC'] and b not in ['to','To']:
            next_cc.append(a)
            break
        else:
            continue


    #print next_to
    #print next_cc
    if not next_to and not next_cc:
        val = 'Any'
        return val
    elif not next_to and next_cc:
      #print "hii"
      ca=next_cc[0]
      val=''
      for item in formated_text:
        # print item
        # print text
        if isnoun(item, text) == True and formated_text.index(item) > formated_text.index(ca):
            val  = val+' '+ item


        elif isnoun(item, text) == False and formated_text.index(item) > formated_text.index(ca):

            break
        else:
            continue

    elif next_to and next_cc:
        #print True
        ca = next_cc[0]
        va=next_to[0]
        val = ''
        for item in formated_text:
            # print item
            # print text
            if isnoun(item, text) == True and formated_text.index(item) > formated_text.index(va) and formated_text.index(
                    item) > formated_text.index(ca):
                val = val + ' ' + item
                print val

            elif isnoun(item, text) == False and formated_text.index(item) > formated_text.index(va) and formated_text.index(
                    item) > newtext.index(ca):

                break
            else:
                continue
    else:
        return 'Any'

    return val


file_data=['pdfs','videos','audio','video','attachment','attachments','Attachment','alx', 'asp', 'au','bas', 'bat', 'bin', 'bmp', 'c', 'cab', 'cda', 'cdr', 'chf', 'cmd', 'com', 'cpl', 'cur', 'dic', 'dll', 'doc', 'dot', 'drw', 'dwg', 'dxf', 'eml', 'eps', 'exe', 'fav', 'gif', 'grp', 'gtar', 'gwf', 'gz', 'hlp', 'ht', 'htm', 'html', 'ico', 'img', 'image', 'inf', 'ini', 'iso', 'java', 'jpeg', 'jpg', 'js', 'jse', 'ldb', 'lnk', 'log', 'mdb', 'mde', 'mdw', 'mid', 'midi', 'mov', 'movie', 'mp1', 'mp2', 'mp3', 'mpeg', 'mpg', 'msg', 'msi', 'msp', 'nws', 'obd', 'oft', 'pbk', 'pcl', 'pcx', 'pdd', 'pdf', 'pic', 'pif', 'pl', 'pot', 'pps', 'ppt','ppts', 'presentation','presentations','pub', 'qbb', 'qbw', 'qdb', 'ra', 'reg', 'scr', 'sct', 'shtml', 'snd', 'sys', 'tar', 'text', 'tga', 'tgz', 'tif', 'tsv', 'ttf', 'txt', 'url', 'uu', 'vbe', 'vbs', 'vir', 'wav', 'wb2', 'wbk', 'wiz', 'wk4', 'wks', 'wma', 'wmf', 'wpd', 'wri', 'wsc', 'wsf', 'wsh', 'xlk', 'xls', 'xlt', 'xml', 'z', 'zip']



def get_sub_strings(s):
    words = s.split()
    for i in xrange(len(words)+1, 0, -1):
        for n in xrange(0, len(words)+1-i):
            yield ' '.join(words[n:n+i])

def attachment(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    v = Decimal(vs['neg']) == 0.0
    tokenizer = RegexpTokenizer(r'\w+')
    wordtoken = tokenizer.tokenize(text)
    out = []
    for word in file_data:
        for sub in wordtoken:
            if sub.lower()==word:
                out.append(sub)

                break
    print out
    if not out:
        return 'Any'
    elif not v==True:
        return 'Any'
    else:
     return max(out, key=len)

file_data2=['.alx', '.asp', '.au', '.avi', '.bas', '.bat', '.bin', '.bmp', '.c', '.cab', '.cda', '.cdr', '.chf', '.cmd', '.com', '.cpl', '.cur', '.dic', '.dll', '.doc', '.dot', '.drw', '.dwg', '.dxf', '.eml', '.eps', '.exe', '.fav', '.gif', '.grp', '.gtar', '.gwf', '.gz', '.hlp', '.ht', '.htm', '.html', '.ico', '.img', '.inf', '.ini', '.iso', '.java', '.jpeg', '.jpg', '.js', '.jse', '.ldb', '.lnk', '.log', '.mdb', '.mde', '.mdw', '.mid', '.midi', '.mov', '.movie', '.mp1', '.mp2', '.mp3', '.mpeg', '.mpg', '.msg', '.msi', '.msp', '.nws', '.obd', '.oft', '.pbk', '.pcl', '.pcx', '.pdd', '.pdf', '.pic', '.pif', '.pl', '.pot', '.pps', '.ppt', '.pub', '.qbb', '.qbw', '.qdb', '.ra', '.reg', '.scr', '.sct', '.shtml', '.snd', '.sys', '.tar', '.text', '.tga', '.tgz', '.tif', '.tsv', '.ttf', '.txt', '.url', '.uu', '.vbe', '.vbs', '.vir', '.wav', '.wb2', '.wbk', '.wiz', '.wk4', '.wks', '.wma', '.wmf', '.wpd', '.wri', '.wsc', '.wsf', '.wsh', '.xlk', '.xls', '.xlt', '.xml', '.z', '.zip']


def attachmentname(text):
    name=''
    wordtoken = text.split()
    print wordtoken
    out = []
    for word in wordtoken:
        for w in file_data2:
            if not (word.find(w)==-1):
                out.append(word)
            else:

                continue
    for items in out:
        name=name+' '+items
    if name:
     return name
    else:
        return 'Any'


def attachmentsize(text):
    v=''
    out=[]
    wordtoken = text.split()
    for word in wordtoken:
     if re.findall(r'\d+', word):
         out.append(word)

    for items in out:
        if not isdigit(items):

            return items
        else:
           return 'Any'

def hasNumbers(inputString):
 return bool(re.search(r'\d', inputString))


def nextstring(st,text):
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    bi_grams = list(ngrams(newtext, 2))
    print bi_grams
    for a, b in bi_grams:
        if a ==st:
            return b
        else:
           continue
def pre_string(st,text):
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    bi_grams = list(ngrams(newtext, 2))
    #print bi_grams
    for a, b in bi_grams:
        if b ==st:
            return a
        else:
           continue
#print pre_string('than',text)
def nexttri_gram(st,text):
    out=''
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    tri_grams = list(ngrams(newtext, 3))
    #print tri_grams
    for a,b,c in tri_grams:
        if pre_string(a,text)==st:
            print True
            out=a + ' ' +b +' ' +c
            #print out
    #print out
    return out

#print nexttri_gram('size',text)


def size(text):
    tokenizer = RegexpTokenizer(r'\w+')
    newtext = tokenizer.tokenize(text)
    if 'size' in newtext:
        if hasNumbers(nextstring('size', text)):
            s=nextstring('size', text)

        else:
            s=nexttri_gram('size',text)
    else:
        s=attachmentsize(text)
    return s
