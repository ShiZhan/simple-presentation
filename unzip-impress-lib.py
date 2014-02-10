import zipfile

with zipfile.ZipFile('impress.js.zip', "r") as z:
    z.extractall("release\\static\\")