str = input("Masukan sebuah kata/kalimat : ")
sisipkan = input("Masukan karakter yang ingin di sisipkan : ")
def sisipHuruf(str,sisip):
    cap =str.upper()
    print(sisip.join(list(cap)))
def sisipKata(str,sisip):
    cap=str.titel()
    print(sisip.join(cap.split()))
    
    sisipHuruf(str,sisip)
    sisipKata(str,sisip)