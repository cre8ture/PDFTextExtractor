
# Importing the Bindings
import fitz

def handle_uploaded_file(f):
    filename = 'pdf_uploads/temp_file.pdf'
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            print(chunk)
            destination.write(chunk)
    return getPDFText(filename, 1,3, 'sample')

# breaks user inputted pages into readable format for extractor
def parsePages(pages):
    print("the pages to be processed are", pages)

    pageList = pages.split(',')
    # double check if this is actually changing list or just making new vars
    for i in range(0, len(pageList)):
        pageList[i] = pageList[i].strip() # remove empty space
        pageList[i] = pageList[i].split('-') # remove '-' to turn that into a list itself aka '1-4' is now [1,4]
        for j in range(0,len(pageList[i])):
            pageList[i][j] = pageList[i][j].strip()
            pageList[i][j] = int(pageList[i][j])
        if len(pageList[i]) == 1:
            pageList[i] = [pageList[i][0], pageList[i][0]+1] # if just 1 page aka '5' then make it [5,6]

    return pageList



# translates page into readable text
def getPDFText(pdf_filename, pages):
        print("extracting text from", pdf_filename)

        text = ''
    # extract pages by comma, then create forloop to iterate through the fitz correct amount of times
    # try:

        pageList = parsePages(pages)
        doc = fitz.open("pdf_uploads/" + pdf_filename)
        
        for x in pageList:
            first_page = x[0]
            last_page = x[1]
            print('PAGES', first_page,last_page)
            text = text + "\n\n(" + str(first_page) + "-" + str(last_page) + ")\n"
            for i in range(first_page, last_page):
                text = text + doc[i].get_text('text', flags=2)  # .replace("\n", " ") <--- removed this to focus on pure raw
            
            # print(text) 
    # except:
        # text = "Error in processing pdf. Make sure file and page numbers are valid. \n - File should be \'.pdf\' file. \n - Page numbers should be in the form of \'page_start-page_end\' seperated by commas. You can also input single pagse."
    
        return text

# TEST
# getPDFText('(PEARSON SERIES IN ARTIFICIAL INTELLIGENCE) Stuart Russell and Peter Norvig - Artificial Intelligence_ A Modern Approach-Pearson (2020)_OT586Ar.pdf', '100-200')
