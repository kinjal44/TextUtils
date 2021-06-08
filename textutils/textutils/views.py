# I have Done This Project - Kinjal Goswami

from django.http import HttpResponse
from django.shortcuts import render
import csv

def index(request):
   return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):

    #get the text
    djtext = request.POST.get('text', 'default')

    #checking checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charcounter = request.POST.get('charcounter','off')
    wordcounter = request.POST.get('wordcounter', 'off')
    capitalized = request.POST.get('capitalized', 'off')

    punctuations = ''':()-[]{};"'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if djtext == "":
        return HttpResponse("Please Enter Text")
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremove=="on":
        analyzed = ""
        for char in djtext:
            if char != "/n":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremove=="on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if not(djtext[i] == " " and djtext[i+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcounter=="on":
        count=0
        for c in djtext:
            if c!="":
                count+=1
        analyzed = f" Total Characters = {str(count)}"
        params = {'purpose': 'Counting Character', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if wordcounter == "on":
        count = 0
        count = len(djtext.split())
        analyzed = f" Total Words = {str(count)}"
        params = {'purpose': 'Counting Words', 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalized == "on":
        analyzed = djtext.title()
        params = {'purpose': 'Counting Words', 'analyzed_text': analyzed}
        djtext = analyzed

    if(removepunc!="on" and extraspaceremove!="on" and newlineremove!="on" and fullcaps!="on" and charcounter!="on" and wordcounter!="on" and capitalized!="on"):
                return HttpResponse("Please select any operation and try again..")

    return render(request, 'analyze.html', params)