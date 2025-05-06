"""Question 1: Task Manager Application
Project Description: In this assignment, you will create a task manager application using the Python programming language. This application will allow users to add, complete, delete, and list their tasks.

Requirements:
1- Tasks will be stored in a Python list and each task will be represented as a dictionary. Each task must have the following properties:

Sequence Number (Automatically assigned)

Task Name

Status (Completed, Pending, or Deleted)

2- Operations that the user can perform:

Add a new task

Complete a task

Delete a task

List completed tasks

List all tasks with their status

Exit

3- Tasks should automatically receive a sequence number in the order they are added.

4- New tasks should be saved in place of the numbers of deleted tasks.

5- When listing tasks, they should be sorted by their sequence number.

6- Appropriate feedback should be given to the user after each operation. For example, when a new task is added, they should see a message indicating that the task has been added."""

gorevlerim ={}
ide = 0
tamalanan_gorevler ={}
def gorev_ekle():
    global ide
    while True:
        gorev =input("Gorevini giriniz: (Cikmak icin 'q'):\n")
        if gorev.lower()=="q":
            break
        durum =input("Durumu giriniz \nBeklemede  \nTamamlandi \nSilindi \n")
        if durum.lower()=="Silindi":
            for key, value in gorevlerim.items():
                if "Silindi" in value[1]:
                    gorevlerim[key]= ["Görev: " + gorev, "Durum: " + durum]
        else:         
            ide +=1
            gorevlerim[ide]=["Gorev:" +gorev, "Durum:" +durum]
    return gorevlerim
def gorev_tamamla():
    no=input("Durumunu degistireceginiz gorevin numarasini girin\n")
    if int(no) in gorevlerim:
        gorevlerim[int(no)][1]="Durum: Tamamlandi"
    return gorevlerim

def gorev_sil():
    no=input("Silmek istediginiz gorevin numarasini girin \n")
    if int(no) in gorevlerim:
        gorevlerim[int(no)][1]="Durum: Silindi"
    return gorevlerim
def tamamlanan_listele():
    for id, (gorev, durum) in gorevlerim.items():
        if durum =="Durum:Tamamlandi":
            print(f"{id}.{gorev} | {durum}")

def tum_gorevleri_listele():
    for id, (gorev, durum) in gorevlerim.items():
        print(f"{id}.{gorev} | {durum}")
while True:
    secim = input(" Seciminizi Giriniz: (1-6) \n")
    if secim =="1":
        gorev_ekle()
    elif secim=="2":
        gorev_tamamla()
    elif secim =="3":
        gorev_sil()
    elif secim =="4":
        tamamlanan_listele()
    elif secim=="5":
        tum_gorevleri_listele()
    elif secim =="6":
        print("Programdan cikiliyor")
        break
    else:
         print("Geçersiz seçim, lütfen 1-6 arasında bir değer giriniz.\n")
    
