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
        imgdata.save()
        imgObj = ImgData.objects.filter(imgpasskey=key).last()
        passwd=0
        j=1
        for i in key:
            passwd+=j*(ord(i))
            j+=1
        key=(passwd)%256
        print(imgObj.encryptimg.path)
        fi=open(imgObj.encryptimg.path,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        # print(image)
        for index, values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(imgObj.encryptimg.path,'wb') 
        fi1.write(image)
        fi1.close()
        return render(request, 'imgencrypted.html',{'imgdata':imgdata})
    return render(request,'imgencrypt.html')

def imgdecrypt(request):
    if request.method=='POST':
        key=request.POST['passkey']
        image=request.FILES['image']
        imgObj = ImgData.objects.filter(imgpasskey=key).last()
        imgObj.decryptimg=image
        imgObj.save()
        passwd=0
        j=1
        for i in key:
            passwd+=j*(ord(i))
            j+=1
        key=(passwd)%256
        print(imgObj.decryptimg.path)
        fi=open(imgObj.decryptimg.path,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        # print(image)
        for index, values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(imgObj.decryptimg.path,'wb') 
        fi1.write(image)
        fi1.close()
        return render(request, 'imgdecrypted.html',{'imgdata':imgObj})
    return render(request,'imgdecrypt.html')
def imgdecrypted(request):
    return render(request,'imgdecrypted.html')
def imgencrypted(request):
    return render(request,'imgencrypted.html')