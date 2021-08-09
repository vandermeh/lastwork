#!/usr/bin/env python3
fileData="""<!DOCTYPE html>
<head>
<meta charset="utf-8" />
<title>Exam</title>
</head>
<body>
<table
border="1"
bgcolor="#A0BEC4"
cellpadding="10"
style="width:100%; border-radius:5px;">
<h1>Exam</h1>
</table>
<table
border="1"
bgcolor="#e6e6fa"
cellpadding="10"
style="width:100%; border-radius:5px;">
<tr>
<td
<p style="text-indent:30px">
this is 
</p>
<!--Закрываем ячейку-->
</td>
</td>
</tr>
</table>
</td>
</tr>
</table>
</body>
</html>"""


f = open('index.html', 'w')
f.write (fileData)
f.close()

import os
info_os = 'lsb_release -d'
with open("index.html",'r+') as f:
    # Read the file 
    lines=f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('this is '):
            lines[i] = lines[i].strip() + str(info_os)
    f.seek(0)
    for line in lines:
        f.write(line)
