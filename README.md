# Python-Bulk-QR-Generator
This code generates QR codes in bulk using the text and file name stored in a .CSV file using the link of api.qrserver.com
In the file 'csv_qr.csv' contains two columns.
-> first column 'qr_text' contains the qr code text which you want to make encoded in qr code. Please use HTML URL encoding references for some special characters.
--> second column 'file_name' contains the file name that the image will save. Don't use .png extention over there because it will automatically done.
--> make sure python 3 is installed in your system.
--> For linux user: ==> Download two files ==> place in a directory ==> fill up the csv_qr.csv file == save the csv file ==> right click ==> Open in terminal ==>type ==>$ python3 bulk_qr.py ==> hit enter key. ----> Wait a few second and enjoy........
#Note:
Default size of the qr code will be 200 X 200 pixels.
If you want to customize it as 450 X 450 pixel then please change code in the bulk_qr.py file as "https://api.qrserver.com/v1/create-qr-code/?size=450x450&data"
