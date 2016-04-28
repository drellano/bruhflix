from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def browse(request):
    return render(request, template_name='browse.html')
