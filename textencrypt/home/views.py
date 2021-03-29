from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AllData
def home(request):
    return render(request,'home.html')
def encrypt(request):
    if request.method == 'POST':
        allData=AllData()
        allData.passkey = request.POST['passkey']
        allData.encrytext = request.POST['enctext']
        print('ak')
        allData.save()
        return redirect('/encrypted/')
    return render(request, 'encrypt.html')
def decrypt(request):
    return render(request, 'decrypt.html')
def encrypted(request):
    return render(request, 'encrypted.html')
def decrypted(request):
    return render(request, 'decrypted.html')
    
  