from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .textExtractor_brain import getPDFText

# Create your views here.
def index(request):

    print("hello", request.POST)
    return render(request, 'pdfExtractor_app/index.html')
    # return render(request, 'pdfExtractor_app/upload.html')

def extract(request):
    pass
    return 

def upload_pdf(request):
    print("upload_file")
    print(request.POST)
    print("request.method", request.method)
    if request.method == 'POST':
        

        form = UploadFileForm(request.POST, request.FILES)
        # form = UploadFileForm({'title', 'tiempo2D1':Data2})  #<<< how to extra queryDict
        print("it's a post:)", form.is_valid(), form.errors)

        if form.is_valid():
            

            # save the file directly
            file = request.FILES['file']
            print("fileNAMMME", file.name, request.POST['title'])
            file_name = default_storage.save(file.name, file)

            text = getPDFText(file_name, request.POST['title'])

            print("TEXT IS", text)
            
            return render(request, 'pdfExtractor_app/index.html') # HttpResponseRedirect('pdfExtractor_app/result.html')
    else:
        print("form not valid")
        form = UploadFileForm()
    return render(request, 'pdfExtractor_app/upload.html', {'form': form})


    
def upload_pdf2(request):
    print("upload_file")
    print(request.POST,  "WEEEEEEE", request.POST['file'])
    print("request.method", request.method)
    

# https://stackoverflow.com/questions/49016255/django-display-contents-of-txt-file-on-the-website
def read_file(request):
    f = open('pdf_uploads/text.txt', 'r')
    file_content = f.read()
    f.close()
    context = {'file_content': file_content}
    # return render(request, "pdfExtractor_app/upload.html", context)
    return render(request, "pdfExtractor_app/index.html", context)