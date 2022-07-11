from django.http import HttpResponse
from django.shortcuts import render
import json


f = open('IFSC(1).json', encoding="mbcs")
data = json.load(f)
a = {}

def index(request):
    return render(request, 'index.html')

def analyze(request):

    # Get the text
        text = "words"
        djtext = request.POST.get('text', 'default')
        djtext1 = request.POST.get('text1', 'default')
        djtext2 = request.POST.get('text2', 'default')
        analyzed = djtext + djtext1
        
        arr = "No such branch :("
        bank = djtext1
        district = djtext
        branch = djtext2
        add = ""
        con = ""
        for i in data:
            
            
            if (i["BANK"] == djtext1 and i["DISTRICT"] == djtext and i["BRANCH"] == djtext2):
                arr = i["IFSC"]
                bank = djtext1
                district = djtext
                branch = djtext2
                add = i["ADDRESS"]
                con = i["CONTACT"]
                
                
                
        params = {'a': arr, 'b': bank, 'c': district, 'd':branch, 'e': add, 'f': con}
        return render(request,'index.html',params)