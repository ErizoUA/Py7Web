from django.shortcuts import render, redirect, get_object_or_404

from .forms import TagForm, NoteForm
from .models import Tag, Note


# Create your views here.
def main(request):
    return render(request, 'noteapp/index.html', context={"notes": Note.objects.all()})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="noteapp:main")
        else:
            return render(request, 'noteapp/tag.html', context={'form': form})

    return render(request, 'noteapp/tag.html', context={'form': TagForm()})


def note(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags:
                note.tags.add(tag)

            return redirect(to="noteapp:main")
        else:
            return render(request, 'noteapp/note.html',  context={'form': form, 'tags': tags})

    return render(request, 'noteapp/note.html', context={'form': NoteForm(), 'tags': tags})


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'noteapp/detail.html', context={"note": note})


def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to="noteapp:main")


def delete_note(request, note_id):
    Note.objects.get(pk=note_id).delete()
    return redirect(to="noteapp:main")
