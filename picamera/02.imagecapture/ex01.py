# 스트림으로 캡처하기

from io import BytesIO
from time import sleep
from picamera import PiCamera

# Create an in-memory stream
my_stream = BytesIO()

camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(2)

camera.capture(my_stream, 'jpeg')  # 포맷 지정 필요
