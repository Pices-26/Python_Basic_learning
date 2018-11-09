import string
from collections import Counter
fo = open("output.html", "w")
fo.write('<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')


# your code goes here!
c = Counter()


html_page = """ 
<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">
"""




count = {}
wrdtxt = open('lab8txt.txt', 'r')
for line in wrdtxt:
    line = line.strip().split()
    for word in line:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # c.update(line.split())
print(count)
for key, wrd in count.items():
    fo.write('<span style="font-size: {}px"> {} </span>'.format(wrd *10, key))


fo.write('</div>\
    </body>\
    </html>')
