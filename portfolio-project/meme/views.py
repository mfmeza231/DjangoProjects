from django.shortcuts import render, get_object_or_404
from .models import Meme

def allmemes(request):
	memes = Meme.objects
	return render(request, 'meme/allmemes.html', {'memes':memes})
