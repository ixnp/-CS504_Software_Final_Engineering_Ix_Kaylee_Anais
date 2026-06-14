# -Krishna, A. (2023, November 27). How to Implement Two-Factor Authentication with PyOTP and Google Authenticator in Your Flask App. freeCodeCamp.org. https://www.freecodecamp.org/news/how-to-implement-two-factor-authentication-in-your-flask-app/
# This utils file creates the QR code that will be rendered in setup-2fa.html
from io import BytesIO
import qrcode
from base64 import b64encode


def get_b64encoded_qr_image(data):
    """
    Generates the QR code in memory needed for the Authentication App.
    Arg: authentication uri
    Returns: QR Code 
    """
    print(data)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    buffered = BytesIO()
    img.save(buffered)
    return b64encode(buffered.getvalue()).decode("utf-8")