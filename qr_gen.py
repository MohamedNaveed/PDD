import pyqrcode
qr = pyqrcode.create('Name: PDD \n Weight: 100kg \n From: TRY Destination: MAS \n Content composition: \n Passport number: ')
qr.png('QR_tag.png', scale=5)
