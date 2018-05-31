import re
class Str_extr:
    """
    Str_extr have been written in order to parse data among Tags.
    contained functions are:
                            f_tag(String)
                            text_tag(String)
    implemented by Soran Ghadri
    Email: kpg.kurd@gmail.com"""

    #define constructor and its variables
    tex=''
    fav=''
    def __init__(self):
        self.tex=""
        self.fav=""

    #getting docID
    def get_docID(s):

        with open(s, "r",encoding = "ISO-8859-1") as ins:

            for line in ins:
                if line.__contains__('DOCNO'):
                    # print (line[7:-9])
                    return line[7:-9]

    #getting context of the tags
    def get_string(s):
        str = ''
        with open(s, 'r',encoding = "ISO-8859-1") as ins:
            for line in ins:
                if not line.__contains__('TEXT') and not line.__contains__('FAVORITE') and not line.__contains__('DOC') and not line.__contains__('DATE') and not line.__contains__('AUTHOR'):
                    str += (line)
                elif line.__contains__('TEXT'):
                    # re.search('<TEXT>(.*)</TEXT>', line).group(1)
                    # print (line[6:-8])
                    str += (line[6:-8])
                elif line.__contains__('FAVORITE'):
                    # print (line[10:-12])
                    str += (line[10:-12])
        return str
    def numberOfCommentsPerDoc(s):
        i =0
        with open(s, "r") as ins:
            for line in ins:
                if line.__contains__('DOC'):
                    i = i+1
        # 'doc'+s+': '+(i/2)-1+'comments'
        return str(int(i/2)-1)



