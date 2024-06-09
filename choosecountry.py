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
selected_option = data.getvalue("selected_option", "")
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Selected Option</title>")
print("</head>")
print("<body>")
print("<h2>Selected Option:</h2>")
print("<p>{}</p>".format(selected_option))
print("</body>")
print("</html>")

# if __name__ == "__main__":
#     main()
# 
# data = cgi.FieldStorage()
# name = 'batman'
# if ('name' in data):
#     name = data['name'].value
# bgcolor = 'DarkSeaGreen'
# if ('bgcolor' in data):
#     bgcolor = data['bgcolor'].value
# 
# html= HTML_HEADER
# html+= '<body style="background-color: '
# html+= bgcolor + ';">'
# html+= '<h1>Hello ' + name + '</h1>'
# html+= '<br><a href="hello.html">Try Again</a>'
# html+= HTML_FOOTER
# print(html)