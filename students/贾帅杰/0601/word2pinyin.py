from xpinyin import Pinyin

p=Pinyin()

with open('lovecn.txt','r',encoding='utf-8') as fp :
    text = p.get_pinyin(fp.read())
    print(text)
print(fp.closed)
