def handle_upload_file(f):
    destination = open('images/3.jpg', 'wb+')
    for chunk in f.chunk():
        destination.write(chunk)
    destination.close()
