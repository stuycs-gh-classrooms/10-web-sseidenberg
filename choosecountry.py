print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""

data = cgi.FieldStorage()
name = 'Alabama'
if ('name' in data):
    name = data['name'].value
 
# html= HTML_HEADER
# html+= '<body style="background-color: '
# html+= bgcolor + ';">'
# html+= '<h1>Hello ' + name + '</h1>'
# html+= '<br><a href="hello.html">Try Again</a>'
# html+= HTML_FOOTER
# print(html)
