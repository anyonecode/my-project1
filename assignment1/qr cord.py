import pyqrcode
s = "i love you"
url = pyqrcode.create(s)
url.svg("myqr.svg",scale=10)
url.png("myqr.png",scale=10)