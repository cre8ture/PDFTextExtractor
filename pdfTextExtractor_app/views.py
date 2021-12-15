from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .textExtractor_brain import handle_uploaded_file

# Create your views here.
def index(request):
    return render(request, 'pdfExtractor_app/index.html')

def extract(request):
    pass
    return 

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # text extractor 
            text = handle_uploaded_file(request.FILES['file'])
            print(text)
            return HttpResponseRedirect('/pdfExtractor/index.html')
    else:
        print("form not valid")
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# https://stackoverflow.com/questions/49016255/django-display-contents-of-txt-file-on-the-website
def read_file(request):
    f = open('pdf_uploads/text.txt', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    return render(request, "pdfExtractor_app/upload.html", context)