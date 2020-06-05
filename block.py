## MIT License
##
## Copyright 2020 4yub1k salahuddin@protonmail.com
##
## Permission is hereby granted, free of charge, to any person obtaining a copy of this
## software and associated documentation files (the "Software"), to deal in the Software
## without restriction, including without limitation the rights to use, copy, modify, merge,
## publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
## to whom the Software is furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all copies
## or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
## INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
## PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
## FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
## OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.



from datetime import datetime as d
from time import sleep

url_filter=[] #url=list()
redirect='127.0.0.1'
file_host=r"C:\Windows\System32\drivers\etc\hosts"
while True:
    url=str(input('please enter the site @example.com End=stop : '))
    #url='end'
    if url =='end':
        break
    url.lower() #lower case
    url_filter.append(url)
    url="www.{}".format(url) #format add www.
    url_filter.append(url)
#url_filter=['f.com','test.com','tester.com','d.com']
hour_start=int(input('Enter Start Time : '))
hour_stop=int(input('Enter stop time : '))
def check(i,url_filter): #check for url_filter items  in line
    for x in range(0,len(url_filter)):
        if url_filter[x] in i:
            return 'yes'

while True:
    if d(d.now().year,d.now().month,d.now().day,d.now().hour,hour_start) < d.now() < d(d.now().year,d.now().month,d.now().day,d.now().hour,hour_stop):
        #d.now().min > hour_start or d.now().min < hour_stop:
        with open(file_host,'r+') as host:
            r=host.read()
            for web in url_filter:
                if web in r:
                    print("Already Added")
                else:
                    host.write(redirect+" "+web+"\n")
                    #print("Done", web)
                    print("Added")
    else:
        with open(file_host,'r+') as host:
            r=host.readlines() #read lines can use rstrip()
            host.seek(0) #from start index in file as after writng it will start from end
            for i in r:
                x=check(i,url_filter)
                if x=='yes': #skipping that line
                    pass
                    # print(i,type(i),len(i))
                    #host.write(i)
                    #print(i)
                else:
                    host.write(i)
                    print("Removed")
            host.truncate() # remove remaining file content
    sleep(20) #time.sleep(seconds) Delay in while loop
    
