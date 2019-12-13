from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Character
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'sheets/index.html'
    context_object_name = 'recent_char_list'

    def get_queryset(self):
        return Character.objects.filter(created__lte=timezone.now()).order_by('-created')


def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'sheets/detail.html', {'character': character})


class DetailView(generic.DetailView):
    model = Character
    template_name = 'sheets/detail.html'
