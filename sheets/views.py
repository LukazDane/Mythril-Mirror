from django.shortcuts import render
from django.http import HttpResponse
from .models import Character
from django.template import loader


def index(request):
    recent_char_list = Character.objects.order_by('-created')
    # template = loader.get_template('sheets/index.html')
    context = {'recent_char_list': recent_char_list, }
    # return HttpResponse(template.render(context, request))
    return render(request, 'sheets/index.html', context)


def detail(request, character_id):
    return HttpResponse("You're looking at character: %s." % character_id)
