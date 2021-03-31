from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import AllData,ImgData
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
        request.session['resp'] = encryptext
        return render(request,'encrypted.html',{'enc':encryptext})
    return render(request, 'encrypt.html')


def decrypt(request):
    if request.method == 'POST':
        try:
            pwd = request.POST['pwdd']
            text = request.POST['etext']
            j=0
            decryptext=""
            q = AllData.objects.filter(passkey = request.POST["pwdd"], encrytext=request.POST["etext"]).first()
            print(q)         
            for i in text:
                if j == len(pwd):
                    j=0
                val = ((ord(i)-33)-(ord(pwd[j])-33)+89)%89
                val+=33
                char = chr(val)
                decryptext+=char
                j+=1
            print(decryptext)
            return render(request,'decrypted.html',{'decryptext':decryptext})
        except:
            messages.warning(request, "INCORRECT PASSWORD OR TEXT")
    return render(request, 'decrypt.html')
def encrypted(request):
    q = AllData.objects.filter(passkey = "sds").first()
    return render(request, 'encrypted.html', {'resp': q})
def decrypted(request):
    return render(request, 'decrypted.html')
    
def imgencrypt(request):
    if request.method=='POST':
        key=request.POST['passkey']
        image=request.FILES['image']
        imgdata=ImgData()
        imgdata.imgpasskey=key
        imgdata.encryptimg=image
        ###############################################
        # file_name=imgdata.encryptimg.name
        # fi=open(file_name,'rb')
        # image=fi.read()
        # fi.close()
        # with open("image", "rb") as image:
        #     f = image.read()
        #     img = bytearray(f)
        keys=0
        for i in key:
            keys+=ord(i)
        l=len(key)
        key=keys%l
        print(key)
        image=image.name
        img=bytearray(image)
        for index,values in enumerate(img):
            img[index]=values^int(key)
        # fi1=open(file_name,'wb')
        # fi1.write(image)
        # fi1.close()
        imgdata.encryptimg=img
        #######################################################
        imgdata.save()
    return render(request,'imgencrypt.html')

def imgdecrypt(request):
    return render(request,'imgdecrypt.html')
   