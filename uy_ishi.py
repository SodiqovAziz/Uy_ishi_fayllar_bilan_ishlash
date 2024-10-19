#1-topshiriq
def topshiriq_1():
    import os
    os.chdir("D:/")
    if not os.path.exists("D:/Men_bekorchiman"):
        os.mkdir("Men_bekorchiman")
        print('D: diskda papka ochildi')
    else:
        print('Bunday papka mavjud.')

#2-topshiriq
def topshiriq_2():
    import os
    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        open("D:/Men_bekorchiman/Bir.txt", "w")
        open("D:/Men_bekorchiman/Ikki.txt", "w")
        open("D:/Men_bekorchiman/Uch.txt", "w")
        open("D:/Men_bekorchiman/Tort.txt", "w")

        papka = "D:/Men_bekorchiman"
        for x in os.listdir(papka):
            print(x)
        print('4 ta txt fayl yaratildi:')

#3-topshiriq
def topshiriq_3():
    import shutil
    import os
    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        D_disk = "D:/Men_bekorchiman"
        C_disk = "C:/Men_bekorchiman"

        if not os.path.exists(C_disk):
            os.makedirs(C_disk)

        try:
            shutil.copytree(D_disk, C_disk, dirs_exist_ok=True)
            print(f"Papka muvaffaqiyatli nusxalandi: {C_disk}")
        except Exception as e:
            print(f"Nusxalashda xatolik yuz berdi: {e}")

#4-topshiriq
def topshiriq_4():
    import shutil
    import os

    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        D_disk = "D:/Men_bekorchiman"

        if not os.path.exists(D_disk):
            print('Papka mavjud emas:')

        if not os.listdir(D_disk):
            print('Ichida fayllar yo`q.')
        else:
            try:
                shutil.rmtree(D_disk)
                print('O`chirildi.')
            except Exception as e:
                print(f'O`chirishda xatolik yuz berdi: {e}')

#5-topshiriq
def topshiriq_5():
    import os
    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        folder_path = "D:/Men_bekorchiman"
        file_name = "Bir.txt"

        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"{file_name} fayli o'chirildi.")
            except Exception as e:
                print(f"O'chirishda xatolik yuz berdi: {e}")
        else:
            print(f"{file_name} fayli topilmadi.")

#6-topshiriq
def topshiriq_6():
    import shutil
    import os

    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        D_disk = "D:/Men_bekorchiman"

        if not os.path.exists(D_disk):
            print('Papka mavjud emas:')

        if not os.listdir(D_disk):
            try:
                shutil.rmtree(D_disk)
                print('O`chirildi.')
            except Exception as e:
                print(f'O`chirishda xatolik yuz berdi: {e}')
        else:
            print('Ichida fayllar bor.')

#7-topshiriq
def topshiriq_7():
    import os

    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        D_disk = "D:/Men_bekorchiman"

        if os.path.exists(D_disk):
            fayl = [f for f in os.listdir(D_disk) if os.path.isfile(os.path.join(D_disk, f))]
            print(f"Papkada {len(fayl)} ta fayl bor.")
        else:
            print("Papka topilmadi.")

#8-topshiriq
def topshiriq_8():
    import os

    if not os.path.exists("D:/Men_bekorchiman"):
        print('Papka yoq papka oching.')
    else:
        D_disk = "D:/Men_bekorchiman"

        if os.path.exists(D_disk):
            papka = [d for d in os.listdir(D_disk) if os.path.isdir(os.path.join(D_disk, d))]
            print(f"Papkada {len(papka)} ta papka bor.")
        else:
            print("Papka topilmadi.")

k=0
while 1:
    if k == 1:
        print('Davom etish (1)')
        print('Dasturni toxtatish (0)')
        davom = int(input('>>> '))
        if davom != 1:
            break
    print('1) D: diskga “Men_bekorchiman” degan popka ochish. ')
    print('2) “Men_bekorchiman” degan papkani ichida 4 ta fayl yaratish. ')
    print('3) “Men_bekorchiman” papkasini fayllari bilan nusxalab C: diskga tashlash.')
    print('4) Fayllar bor popkani o‘chirish.')
    print('5) Ko‘rsatilgan manzildan faylni o‘chirish.')
    print('6) Ko‘rsatilgan manzildan bo‘sh popkani o‘chirish.')
    print('7) Ko‘rsatilgan manzildagi popkada nechta fayl borligini aniqlash')
    print('8) Ko‘rsatilgan manzildagi popkada nechta papka borligini aniqlash')
    k=1
    n = int(input('Birini tanlang: '))
    if n == 1:
        topshiriq_1()
    if n == 2:
        topshiriq_2()
    if n == 3:
        topshiriq_3()
    if n == 4:
        topshiriq_4()
    if n == 5:
        topshiriq_5()
    if n == 6:
        topshiriq_6()
    if n == 7:
        topshiriq_7()
    if n == 8:
        topshiriq_8()
    if n > 8:
        print('8 gacha bolgan son orasidan birini tanlang!!!')