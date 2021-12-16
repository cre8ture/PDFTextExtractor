from django import forms

# from pdfTextExtractor_app.views import upload_file

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
    # file = forms.ImageField(upload_to = 'pictures')
    # file = forms.FieldFile()

class UploadFileForm(forms.Form):
    file = forms.FileField()
    pages = forms.CharField(max_length=50)