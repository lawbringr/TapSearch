from django.shortcuts import render
import utils
from index.models import Document
# Create your views here.
def clear(request):
    if request.method == 'POST':
        utils.clearPickle()
        Document.objects.all().delete()
    return render(request, 'clear.html')