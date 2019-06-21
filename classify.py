import shutil,os


for line in open("C:\\...\\MNIST\\raw\\test.txt"):
    label = line[-3]
    adress = line[0:(len(line)-11)]
    adress = adress[:17] + adress[18:]
    adress = adress.replace('/','\\\\')
    # print(adress)
    #print(label)
    if label == '0':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\0")
    if label == '2':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\2")
    if label == '3':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\3")
    if label == '4':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\4")
    if label == '5':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\5")
    if label == '6':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\6")
    if label == '7':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\7")
    if label == '8':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\8")
    if label == '9':
        shutil.move(adress,"C:\\U...\\MNIST\\raw\\9")
    if label == '1':
        shutil.move(adress,"C:\\...\\MNIST\\raw\\1")




