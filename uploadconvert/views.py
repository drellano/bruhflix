from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.core.urlresolvers import reverse
from .models import MovieForm


def handle_uploaded_file(f):
    with open('/home/david/abc.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        form = MovieForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return render(request, 'success.html')
