from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AllData
def home(request):
    return render(request,'home.html')
def encryption(request):
    if request.method == 'POST':
        allData=AllData()
        allData.passkey = request.POST['passkey']
        allData.encrytext = request.POST['enctext']
    
        allData.save()
    return render(request, 'encryption.html')
def decryption(request):
    return render(request, 'decryption.html')
def encrypted(request):
    return render(request, 'encrypted.html')
def decrypted(request):
    return render(request, 'decrypted.html')
    
  