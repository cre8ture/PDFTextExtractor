

def handle_uploaded_file(f):
    with open('pdf_uploads/temp_file', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)