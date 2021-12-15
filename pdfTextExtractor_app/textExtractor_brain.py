
# Importing the Bindings
import fitz

def handle_uploaded_file(f):
    with open('pdf_uploads/temp_file', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def getPDFText(pdf, first_page, last_page, chapter_name):

# get_page_text(pno, output="text", flags=3, textpage=None, sort=False)
  text = ''
  doc = fitz.open(pdf)
  print()
  print(chapter_name)
  for i in range(first_page, last_page):
      text = text + doc[i].get_text('text', flags=2)  # .replace("\n", " ") <--- removed this to focus on pure raw
 
  # use the below two lines to save as text file. Otherwise function only prints out text
  # with open("ai_text.txt", "w") as output:  
  #     output.write('\n'+ chapter_name + '\n'+'\n' + text)
  return text