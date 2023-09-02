nama_saya= str(input("nagita brenda silvia = "))

print(nama_saya,"bertipe",type(nama_saya)) 
umur = str(input("18 = "))
print(umur, "bertipe", type(umur))

IPK = float(input("4.00 = "))
print(IPK, "bertipe", type(IPK))

menikah = bool(input("sudah menikah? = "))
print("menikah?",menikah, "bertipe", type(menikah))

matkul_diambil = ["alpro", "sig"]
print("Matkul : ",matkul_diambil, "bertipe", type(matkul_diambil))

matkul_diambil2 = ("web","pemvis")
print("Matkul Lain: ",matkul_diambil2, "bertipe", type(matkul_diambil2))

matkul_diambil3 = {"Alpro", "Alpro", "PemWeb", "Data Science", "Data Science"}
print("Matkul Lain-Lain: ",matkul_diambil3, "bertipe", type(matkul_diambil3))


matkul = ["pemweb", "data science"]
# matkul.append("Alpro")
print(matkul)
matkul.insert(1, "Alpro")
print(matkul)

nama_universitas = "Universitas Trunojoyo"
print(nama_universitas)

nama_universitas = str(input())