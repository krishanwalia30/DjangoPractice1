# i have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # For getting the data
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    purpose = ""
    # writing the code to remove punctuations
    analyzed_text = ""
    punctuations = ''',./;'[]\=-`~!@#$%^&*()_+{}|":><'''
    if removepunc == 'on':
        purpose += "Removing Punctuations, "
        for char in djtext:
            if char in punctuations:
                continue
            else:
                analyzed_text += char
    else:
        analyzed_text = djtext

    # writing code to convert the string to uppercase
    if uppercase == 'on':
        purpose += "CAPITALIZING, "
        analyzed_text = analyzed_text.upper()

    # writing code to remove new lines in the text
    if newlineremove == 'on':
        purpose += "REMOVING NEW LINES, "
        new = ''
        for char in analyzed_text:
            if char == '\n' or char == '\r':
                continue
            else:
                new += char
        analyzed_text = new

    # writing code to remove spaces in the text
    if extraspaceremove == 'on':
        purpose += "REMOVING EXTRA-SPACES, "
        new = ""
        for index, char in enumerate(analyzed_text):
            if index+1 != len(analyzed_text):
                if not(analyzed_text[index] == ' ' and analyzed_text[index+1]== " "):
                    new += char
        analyzed_text = new

    # writing code to calculate the length of the string
    if charcount == 'on':
        purpose += "COUNTING THE LENGTH OF THE STRING"
        analyzed_text = analyzed_text + ' ==>[THE LENGTH OF THE TEXT IS ' + str(len(analyzed_text)) + ']'

    params = {'purpose': purpose, 'analyzed_text': analyzed_text}

    return render(request, 'analyze.html', params)
