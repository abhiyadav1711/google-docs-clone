from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document

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