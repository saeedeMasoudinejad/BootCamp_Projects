import http.client
import urllib.request
import re
# import pillow
REMOTTE_HOST = "www.isna.ir"
REMOTTE_PATH = '/'


# METHOD #1: OpenCV, NumPy, and urllib
# def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    # resp = urllib.urlopen(url)
    # image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return image
    # return img


class httpClient:
    def __init__(self, host):
        self.host = host
        self.http = http.client.HTTPSConnection(host)

    def fetch(self, address):
        self.http.putrequest("GET", address)
        self.http.putheader("Host", REMOTTE_HOST)
        self.http.putheader("Connection", "Keep-Alive")
        self.http.putheader("Accept", "*/*")
        self.http.endheaders()
        try:
            self.resp = self.http.getresponse()
        except Exception as e:
            raise e

    def detect_img(self):
        folder = "C:\\Users\saide\PycharmProjects\MD_s1\downlodimg\\"
        html_strs = self.resp.read().decode()
        urls = re.findall(r"<img .*?src\s*=\s*\"(.+?)\"", html_strs)
        i = 0
        for url in urls:
            try:
                i += 1
                a = str(i)+".png"
                filename = folder + a
                urllib.request.urlretrieve(url, filename)
            except Exception:
                continue

conn = httpClient(REMOTTE_HOST)
conn.fetch(REMOTTE_PATH)
print('status', conn.resp.status, 'reason', conn.resp.reason)
# print(conn.resp.read())
conn.detect_img()


