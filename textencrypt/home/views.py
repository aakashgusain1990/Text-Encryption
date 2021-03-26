from django.shortcuts import render,redirect
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def encryption(request):
    return render(request, 'encryption.html')
def decryption(request):
    return render(request, 'decryption.html')
def encrypted(request):
    return render(request, 'encrypted.html')
def decrypted(request):
    return render(request, 'decrypted.html')
    
  