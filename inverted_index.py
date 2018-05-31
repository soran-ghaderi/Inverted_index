import re
import glob
import StringExtractor as se
from collections import defaultdict, Counter
import nltk
import stemmedCount as stc
import tabulate

from nltk import word_tokenize
sw = open('./files/stopwords.txt','r')
inverted_index_file = open('./files/inverted index.csv','w')
inverted_index_doc_freq = open('./files/inverted index doc freq.csv','w')
stopwords = str(sw.read())
inp = open('PorterStemmed.txt','r', encoding='ISO-8859-1')
inpstr = str(inp.read())

list_of_files = glob.glob('./dataset/*')
data = []
numberOfBrands =[]
stri=''
stri_stw=''
tokensList = []
for file_name in list_of_files:
    (file_name.__len__())
    if(file_name.__contains__('200')):
        data.append({'title':str(se.Str_extr.get_docID(file_name)),'description': str(se.Str_extr.get_string(file_name))})
        numberOfBrands.append(str(se.Str_extr.get_docID(file_name)))
        stri= stri+' '+ (str(se.Str_extr.get_string(file_name)))



def bold(txt):
    return '\x1b[1m%s\x1b[0m' % txt



pattern = re.compile(r'[^a-zA-Z]')
pattern2 = r'^((200([7-9])(_)([^a-zA-Z0-9]+)(_)))'
c2007 = 0
c2008 = 0
c2009 = 0
for x in numberOfBrands:
    if (str(x).__contains__('2007')):
        c2007 = c2007+1
    elif (str(x).__contains__('2008')):
        c2008 = c2008+1
    elif (str(x).__contains__('2009')):
        c2009 = c2009+1
xx = []
xx.append(c2007)
xx.append(c2008)
xx.append(c2009)

print(c2007,c2008,c2009)

def tokenize(text):
    yield from pattern.split(text)




def text_only(tokens):
    for t in tokens:
        if t.isalnum():
            yield t

def lowercase(tokens):
    for t in tokens:
        yield t.lower()

def uppercase(tokens):
    for t in tokens:
        yield t.uppper()

def stem(tokens):

    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()
    for t in tokens:
        if t not in stopwords:
            return (porter.stem(t))
    # return [porter.stem(t) for t in tokens]
    # elif stemmer is 'lancaster':
    #     return [lancaster.stem(t) for t in tokens]
    # for t in tokens:
    #     if t.endswith('ly'):
    #         t = t[:-2]
    #     yield t

SYNONYMS = {
    'rapid': 'quick',
}
def synonyms(tokens):
    for t in tokens:
        yield SYNONYMS.get(t, t)

def analyze(text):
    tokens = tokenize(text)
    for token_filter in (text_only, lowercase, stem):
        tokens = token_filter(tokens)

    yield from tokens

uu=[]
def index_docs(docs, *fields):
    index = defaultdict(lambda: defaultdict(Counter))
    for id, doc in enumerate(docs):
        # print(id,doc)
        for field in fields:
            for token in analyze(doc[field]):
                index[field][token][id] += 1
    return index



def combine_or(*args):
    if not args:
        return Counter()
    out = args[0].copy()
    for c in args[1:]:
        out.update(c)
    return out

COMBINE = {
    'OR': combine_or,
    # 'AND': cand,
}

def search_in_fields(index, query, fields):
    for t in analyze(query):
        yield COMBINE['OR'](*(index[f][t] for f in fields))

def search(index, query, operator='OR', fields=None):
    combine = COMBINE[operator]
    return combine_or(*(search_in_fields(index, query, fields or index.keys())))

def query(index, query,i=0, fields=None):
    # print('Search for',(bold(query)))
    # print('-'*100)
    j=0
    if query not in stopwords:
        ids = search(index, query, 'OR', fields)
        for doc_id, score in ids.most_common():
            # print('ID %s: %s - frequency: %s' % (doc_id, bold(data[doc_id]['title']), bold(score)))
            inverted_index_file.write(str(i))
            inverted_index_file.write(',')
            inverted_index_file.write(str(doc_id))
            inverted_index_file.write(',')
            inverted_index_file.write(str(score))
            inverted_index_file.write("\n")
        # print('\n')
        for doc_id in ids:
            j = j+1
        # print(i,query,j)
        inverted_index_doc_freq.write(str(i))
        inverted_index_doc_freq.write(',')
        inverted_index_doc_freq.write(str(query))
        inverted_index_doc_freq.write(',')
        inverted_index_doc_freq.write(str(j))
        inverted_index_doc_freq.write("\n")

    else:
        pass

index = index_docs(data, 'title', 'description')



# //////////////////////////////////////////////////////////////////////////////////////
number_with_stopword = set(nltk.re.split(r'[^a-zA-Z]', stri))
# number of tokens without stopwords:

number_without_stopword = set(nltk.re.split(r'[^a-zA-Z]', stri_stw))

# number of tokens after stemming:
numberOfstemmed_words = set(nltk.re.split(r'[^a-zA-Z]', stem(stri)))
print('number of all words: ',number_with_stopword.__len__())
print('number of stemmed words: ',set(stc.num(inpstr)).__len__())


# /////////////////////////////////////////////////////////////////////////////////////


i=0
for q in number_with_stopword:
    # inverted_index_file.write(str(i))
    # inverted_index_file.write(',')

    try:
        query(index, str(q),i)
        i= i+1
    except:
        pass
    # query(index, 'rapid')
        # query(index, 'of')
