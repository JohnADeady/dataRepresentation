# Import libraries
import requests
import json

# read into html
#html = '<h1>hello world</h1>This is html'
f = open("../Week 4/carviewer2.html", "r")
html = f.read()

#print (html)
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

# rename ad post to json
data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)
#print (resp

# Print status code
newFile = open("Lab6.2.htmlaspdf.pdf", "wb")
newFile.write(response.content)
print(response.status_code)