from django.shortcuts import render
import utils 
from .models import Document
from django.core.files.storage import default_storage

# Create your views here.
def index(request):
    if request.method == 'POST':
        pdfText=""
        if request.FILES.get('pdf',False):
            file = request.FILES['pdf']
            file_name = default_storage.save(file.name, file)
            pdfText= "\r\n\r\n" + utils.parsePDF(file_name)

        data = request.POST.copy()
        doc = data.get('document')
        doc += pdfText

        count= Document.objects.count()
        seperatedDocs= utils.seperateDoc(doc)
        invindex = utils.createInvertedIndex(seperatedDocs,count)

        for d in seperatedDocs:
            name="Doc"+str(count)
            count+=1
            doc_instance = Document.objects.create(name=name,doc=d)

        utils.updateDict(invindex)

    return render(request, 'index.html')