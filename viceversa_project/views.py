from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def reverse(request):
    text = request.GET['message']
    words = text.split()




    reversed = text[::-1]
    return render(request,"reverse.html", {"usertext":text, "reversed":reversed, "words": len(words)})
