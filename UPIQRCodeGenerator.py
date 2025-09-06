import qrcode

#taking UPI ID as a input
upi_id = input("Enter your UPI ID : ")

#upi://pay?pa=upi_id&pn=Name&am=Amount&cu=Currency&tn=Message
#Defining the payment URL based  on the UPI ID and the payment app
# You can modify these URLs based on the payment app you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=123456789'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=123456789'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=123456789'

#Create QR codes for each payment APP
phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

#save
phonepe_qr.save = ('phonepe_qr.png')
google_pay_qr.save = ('google_pay_qr.png')
paytm_qr.save = ('paytm_qr.png')

#Show
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()
