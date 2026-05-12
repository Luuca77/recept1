from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recept, Kategorie
from .forms import ReceptForm


def seznam_receptu(request):
    recepty = Recept.objects.all()
    kategorie = Kategorie.objects.all()
    aktivni_kategorie = None

    kategorie_id = request.GET.get('kategorie')
    if kategorie_id:
        recepty = recepty.filter(kategorie__id=kategorie_id)
        aktivni_kategorie = Kategorie.objects.get(id=kategorie_id)

    return render(request, 'recepty/seznam.html', {
        'recepty': recepty,
        'kategorie': kategorie,
        'aktivni_kategorie': aktivni_kategorie,
    })

def detail_receptu(request, pk):
    recept = get_object_or_404(Recept, pk=pk)
    return render(request, 'recepty/detail.html', {'recept': recept})

@login_required
def pridat_recept(request):
    if request.method == 'POST':
        form = ReceptForm(request.POST, request.FILES)
        if form.is_valid():
            recept = form.save(commit=False)
            recept.autor = request.user
            recept.save()
            return redirect('seznam')
    else:
        form = ReceptForm()
    return render(request, 'recepty/pridat.html', {'form': form})

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def registrace(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('seznam')
    else:
        form = UserCreationForm()
    return render(request, 'recepty/registrace.html', {'form': form})

def prihlaseni(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('seznam')
    else:
        form = AuthenticationForm()
    return render(request, 'recepty/prihlaseni.html', {'form': form})

def odhlaseni(request):
    logout(request)
    return redirect('seznam')

@login_required
def upravit_recept(request, pk):
    recept = get_object_or_404(Recept, pk=pk)
    if recept.autor != request.user:
        return redirect('seznam')
    if request.method == 'POST':
        form = ReceptForm(request.POST, request.FILES, instance=recept)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = ReceptForm(instance=recept)
    return render(request, 'recepty/upravit.html', {'form': form, 'recept': recept})

@login_required
def smazat_recept(request, pk):
    recept = get_object_or_404(Recept, pk=pk)
    if recept.autor != request.user:
        return redirect('seznam')
    if request.method == 'POST':
        recept.delete()
        return redirect('seznam')
    return render(request, 'recepty/smazat.html', {'recept': recept})