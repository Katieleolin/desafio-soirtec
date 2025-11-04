from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Enquete, Choice

def index(request):
    enquetes = Enquete.objects.all()
    return render(request, "enquetes/index.html", {"enquetes": enquetes})

def detail(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render(request, "enquetes/detail.html", {"enquete": enquete})

def vote(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    try:
        selected_choice = enquete.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "enquetes/detail.html", {
            "enquete": enquete,
            "error_message": "Você não selecionou uma opção.",
        })
    else:
        selected_choice.votos += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("enquetes:results", args=(enquete.id,)))

def results(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render(request, "enquetes/results.html", {"enquete": enquete})
