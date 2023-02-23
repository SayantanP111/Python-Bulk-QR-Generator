import csv
import requests

with open('csv_qr.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("QR Code Generating - - - - - - - Please Wait - - - - - -")
 for row in data:
 	image_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="+row['qr_text']
 	r = requests.get(image_url)
 	with open(row['file_name']+".png", 'wb') as f:
 		f.write(r.content)
