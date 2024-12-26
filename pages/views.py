from django.shortcuts import render
from django.http import HttpResponse
from .models import Msglist

# Create your views here.


def index(request):

    msglist = Msglist.objects.all()
    msglist = msglist[0]

    context = {
        'msglist' : msglist,
    }

    return render(request, 'pages/index.html', context)
