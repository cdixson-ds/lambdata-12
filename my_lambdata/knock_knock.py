#my_lambdata/my_script.py

import pandas

#print("Hello World")

#df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
#print(df.head())

print('Hello! I have a joke for you:')
a= input('Knock, knock!\n')
if (a=="Who's there" or a=="who's there" or a=="Who's there?" or a=="who's there?"):
   b=input('Scold\n')
else:
    a=input("Please print 'Who's there?'\n")
    if (a=="Who's there" or a=="who's there" or a=="Who's there?" or a=="who's there?"):
        b=input('Scold\n')
if (b=="Scold who?" or b=="scold who?" or b=="Scold who" or b=="scold who"):
    c='Scold outside let me in!'
    print(c)
else:
    b=input("Please print 'Scold who?'\n")
    if (b=="Scold who?" or b=="scold who?" or b=="Scold who" or b=="scold who"):
       c='Scold outside let me in!'
       print(c)
