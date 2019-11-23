from django.shortcuts import render
import utils
from index.models import Document
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import pdfkit
import urllib


# Create your views here.


def search(request):
    if request.GET.get('term'):
        term = request.GET['term'].lower()
        inverseIndex=utils.getDict()
        retrievedDocs = utils.getSearchList(term)

        if len(retrievedDocs)>10:
            retrievedDocs=retrievedDocs[10:]
        docs=[]

        for doc in retrievedDocs:
            try:
                retrieved= Document.objects.get(name=doc)
                docs.append(retrieved)
            except Exception:
                pass

        if len(docs)>0:
            context = {'docs': docs}
        else:
            context = {'noneFound': "No Documents Found"}
        return render(request, 'search.html',context)

    return render(request, 'search.html')

