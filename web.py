fileData="""<!DOCTYPE html>
<head>
<meta charset="utf-8" />
<title>Exam</title>
</head>
<body>
<table
border="1"
bgcolor="#7FFFD4"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку таблицы-->
<tr>
<!--Создаём столбец таблицы-->
<th>
<!--Содержание ячейки столбца-->
<h1>Exam</h1>
<!--Закрываем таблицу-->
</th>
</tr>
</table>
<table
border="1"
bgcolor="#e6e6fa"
cellpadding="10"
style="width:100%; border-radius:5px;">
<!--Создаём строку-->
<tr>
<td
<p style="text-indent:20px">
time is </p>
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

from datetime import datetime
current_time = datetime.now().time()
with open("index.html",'r+') as f:
    # Read the file 
    lines=f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('time is'):
            lines[i] = lines[i].strip() + str(current_time)
    f.seek(0)
    for line in lines:
        f.write(line)
