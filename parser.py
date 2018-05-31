import glob

# import nltk

import StringExtractor as se

list_of_files = glob.glob('./dataset/*')
i=0
print(list_of_files)
#define output file
outputfile = open('outputfile.xml','w')
# statistic = open('Statistics.txt','w')
# brand = open('Brands.txt','w')
# carsPerY = open('carsPerY','w')

data = []
#getting files' names in the directory and write results in the output
for file_name in list_of_files:
    (file_name.__len__())
    if(file_name.__contains__('200')):
        data.append({'title':str(se.Str_extr.get_docID(file_name))})
        data.append({'description': str(se.Str_extr.get_string(file_name))})
        # outputfile.write('{')
        # outputfile.write(str(i))
        # outputfile.write('}')
        # outputfile.write('{')
        # outputfile.write(str(se.Str_extr.get_docID(file_name)))
        # outputfile.write('}')
        # outputfile.write(str(se.Str_extr.get_string(file_name)))
        # outputfile.write("\n")
        # statistic.write(str(i))
        # statistic.write(' - ')
        # statistic.write(str(file_name[2:]))
        # statistic.write(': ')
        # statistic.write(se.Str_extr.numberOfCommentsPerDoc(file_name))
        # statistic.write("\n")


    i = i + 1
outputfile.close()
print(data)
# carsPerY.write(str(numberOfCarsPerYear(list_of_files)))

def numberOfBrands(s):
    j=0
    pattern = r'^((200([7-9])(_)))'
    brands=[]
    for file_name in list_of_files:
        if not brands.__contains__(file_name[5:8]):
            j = j+1
    return j
def numberOfCarsPerYear(s):
    i2007 =0
    i2008=0
    i2009=0
    stat=''
    j = 0
    for file_name in list_of_files:
        if file_name.__contains__('2007'):
            i2007 = i2007+1
        elif file_name.__contains__('2008'):
            i2008 = i2008 + 1
        elif file_name.__contains__('2009'):
            i2009 = i2009 + 1
    stat = 'number of cars in 2007: '+str(i2007)+"\nnumber of cars in 2008: "+str(i2008)+"\nnumber of cars in 2009: "+str(i2009)
    return stat

