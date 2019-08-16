#! python3
#CreateNewChapterPage.py - creates new HTML formated chapter page for jpeterson1823.github.io.
import os, shutil

def getFormatedString(num):
    if len(str(num)) > 1:
        return '''<img src="../src/Ch'''+str(chapterNum)+'''/Chapter'''+str(chapterNum)+'''BIO-'''+str(num)+'''.png" width="850" height="1000"/>'''
    else:
        return '''<img src="../src/Ch'''+str(chapterNum)+'''/Chapter'''+str(chapterNum)+'''BIO-0'''+str(num)+'''.png" width="850" height="1000"/>'''

os.chdir('/Users/john/Documents/GitHub/jpeterson1823.github.io/Chapters')
os.system('clear')
print('Please enter the chapter of this HTML page:')
chapterNum = input()
pageName = 'Chapter'+chapterNum+'.txt'

print('Please enter the directory for the folder containing the png files:')
locationOfFolder = input()

if not os.path.isdir(locationOfFolder):
    print('Invalid DIR at: '+locationOfFolder)
    exit()

numberOfPages = len(os.listdir(locationOfFolder))
for filename in os.listdir(os.getcwd()):
    if pageName == filename:
        print(pageName+' already exist in provided path: '+locationOfFolder)
        exit(1)

print('Number of Pages: '+str(numberOfPages))

chapterFile = open(os.getcwd()+os.sep+pageName,'w+')
chapterFile.write('''
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="../style.css">
        <script src="../loginCheck.js"></script>
        <script>
            function start(){
                if(getCookie("pass") == "") document.location="login.html";
            }
        </script>

        <title>Wrobel Biololgy II Class Book</title>
    </head>

    <body onload="start();">
        <div class="navbar">
            <a class="home" href="../index.html">Home</a>
            <div class="ch5">
                <button class="ch5btn">Sections<i class="fa fa-caret-down"></i></button>
                <div class="ch5-content">

                    Chapters Link Goes Here

                </div>
            </div>
        </div>

        <div id="title"><h1>Byrd Wrobel Biology II Book<br>
            <div id="email">Email: petersonjohn418@gmail.com<br>Phone: (318)553-3792<br></div>
        </h1></div>

        <div class="ch15" oncontextmenu="return false;">
            <img id="sec'''+str(chapterNum)+'''.1" src="../src/Ch'''+str(chapterNum)+'''/Chapter'''+str(chapterNum)+'''BIO-01.png" width="850" height="1000"/>
''')

chapterFile = open(os.getcwd()+os.sep+pageName,'a')
for num in range(2,numberOfPages):
    chapterFile.write('''            '''+getFormatedString(num)+'\n')

chapterFile.write('''        </div>
    </body>
</html>
''')

chapterFile.close()
shutil.move(os.getcwd()+os.sep+pageName, os.getcwd()+os.sep+pageName.split('.')[0]+'.html')

print("Created HTML file at:"+os.getcwd())