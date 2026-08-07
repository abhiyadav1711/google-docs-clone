from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages



@login_required
def document_list(request):
    documents = Document.objects.filter(owner=request.user)
    return render(request, 'editor/document_list.html', {'documents': documents})

@login_required
def document_create(request):
    doc = Document.objects.create(title="Untitled Document", owner=request.user)
    return redirect('document_edit', pk=doc.pk)

@login_required
def document_edit(request, pk):
    doc = get_object_or_404(Document, pk=pk, owner=request.user)
    if request.method == 'POST':
        doc.title = request.POST.get('title')
        doc.content = request.POST.get('content')
        doc.save()
    return render(request, 'editor/document_edit.html', {'document': doc})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'editor/signup.html')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('document_list')

    return render(request, 'editor/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('document_list')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'editor/login.html')

    return render(request, 'editor/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')