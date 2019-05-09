from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    
    return  render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordsplit = fulltext.split()

    word_dict = {}
    for word in wordsplit:
        if word in word_dict:
            word_dict[word] +=1

        else:
            word_dict[word] = 1

    x = sorted(word_dict.items(), reverse=True, key=lambda kv:kv[1])

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordsplit), 'word_dict' : x})

def about(request):
    return  render(request,'about.html')
