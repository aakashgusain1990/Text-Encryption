from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AllData
def home(request):
    return render(request,'home.html')

    
def encrypt(request):
    if request.method == 'POST':
        allData=AllData()
        allData.passkey = request.POST['passkey']
        pwd = request.POST['passkey']
        text = request.POST['enctext']
        encryptext=""
        j=0
        for i in range(len(text)):
            if j==len(pwd):
                j=0
            val = ((ord(text[i])-33)+(ord(pwd[j])-33))%89
            val+=33
            char = chr(val)
            encryptext+=char
            j+=1
        allData.encrytext = encryptext
        allData.save()
        return redirect('/encrypted/',{'result': encryptext})
    return render(request, 'encrypt.html')


def decrypt(request):
    if request.method == 'POST':
        pwd = request.POST['pwdd']
        text = request.POST['etext']
        j=0
        decryptext=""
        for i in text:
            if j == len(pwd):
                j=0
            val = ((ord(i)-33)-(ord(pwd[j])-33)+89)%89
            val+=33
            char = chr(val)
            decryptext+=char
            j+=1
        print(decryptext)
        return redirect('/decrypted/')
    return render(request, 'decrypt.html')
def encrypted(request):
    return render(request, 'encrypted.html')
def decrypted(request):
    return render(request, 'decrypted.html')
    
  