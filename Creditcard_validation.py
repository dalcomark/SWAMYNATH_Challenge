import re
import itertools
#text="5133-3367-8912-3456"
text = input()
#print(len(text))

l=[(k, sum(1 for i in g)) for k,g in itertools.groupby(text)]  #To calculate frequency of characters and later we can filter it with the condition v<=3 for checking the concurrency condition

if re.search(r'^[456]+',text) and len(text)==16  and re.search(r'[\d]',text) and all(v<=3 for k,v in l) and bool(re.search(r'\s',text)) is False and bool(re.search(r'[a-z]',text)) is False or( bool(re.search(r'-',text))is True and len(text)==19) :
    print("Valid")

else :
    print("Invalid")
