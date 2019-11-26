from aip import AipFace
import json
import base64
from PIL import Image
from io import BytesIO
from urllib.parse import urlencode
def image_to_base64(image_path):
    with open(image_path, 'rb') as fp:
        return base64.b64encode(fp.read())

""" 你的 APPID AK SK """
APP_ID = '17855607'
API_KEY = 'zOLUvfGrQZp2ZNyoc7RTmcIL'
SECRET_KEY = 'tgO9fMLMLwLclUbq67ybGlDCRfBD3iqm'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

encoded_string  = image_to_base64("small.jpeg")
    
imageType = "BASE64"
options = {}
options["face_field"] = "age"
options["max_face_num"] = 2
options["face_type"] = "LIVE"
options["liveness_control"] = "LOW"

""" 调用人脸检测 """
result = client.detect(str(encoded_string,'utf-8') , imageType)
print(result)



