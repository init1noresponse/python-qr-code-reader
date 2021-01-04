import pyqrcode

otp_url = input("Enter OTP url:\n")
url = pyqrcode.create(otp_url)

# displays tempfile that is deleted afterwards
url.show()