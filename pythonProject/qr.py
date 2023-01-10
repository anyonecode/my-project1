import pyqrcode
import png

s = "i love you achuuuu"
url = pyqrcode.create(s)
url.svg("myqr.svg",scale=10)
url.png("myqr.png",scale=10)