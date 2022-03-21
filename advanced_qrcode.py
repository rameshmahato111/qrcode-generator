import qrcode
from PIL import Image

# create a variable

qc = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
qc.add_data('https://www.linkedin.com')
qc.make(fit=True)
# again create a variable
img = qc.make_image(fill_color="pink", back_color='gray')
img.save("linkedin.png")