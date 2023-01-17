# LATIHAN 1

kalimat = 'Hello World'
print (kalimat)

# Hitung Jumlah Karakter 
jumlah_karakter = len(kalimat)
print (f'\nJumlah Karakter = {jumlah_karakter}')

# Ambil Karakter Terakhir
karakter_terakhir = kalimat[10:11]
print (f'\nKarakter Terakhir = {karakter_terakhir}')

# Ambil karakter index ke-2 sampai index ke-4 (llo)
index_ke2ke4 = kalimat [2:5]
print (f'\nIndex ke-2 sampai ke-4 = {index_ke2ke4}')

# Hilangkan spasi pada text tersebut (HelloWorld)
hilangkan_spasi = kalimat.replace (' ','')
print (f'\nSpasi dihilangkan = {hilangkan_spasi}')

# Ubah text menjadi huruf besar
huruf_besar = kalimat.upper()
print (f'\nMenjadi huruf besar = {huruf_besar}')

# Ubah text menjadi huruf kecil
huruf_kecil = kalimat.lower()
print (f'\nMenjadi huruf kecil = {huruf_kecil}')

# Ganti karakter H dengan karakter J
ganti_karakter = kalimat.replace('H','J')
print (f'\nKarakter J diganti dengan H, Menjadi {ganti_karakter}')

# LATIHAN 2

umur = '24'
txt = 'Hello, nama saya john, dan umur saya adalah {} tahun'

print ('\n',txt.format(umur))