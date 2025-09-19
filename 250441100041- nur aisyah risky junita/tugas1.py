# 1. Kamu sedang marathon TV series di netflix
#    1 episode berdurasi 35 min dengan total 10 episode
#    berapa jam kamu menonton TV series tersebut?

# durasi 1 episode dalam menit 
durasi_episode = 35  

# jumblah episode
total_episode = 10

# total nonton dalam menit
total_menit = durasi_episode * total_episode

# pindah dalam bentuk jam dan menit
jam = total_menit // 60
menit = total_menit % 60

print("total waktu menonton",jam, "jam", menit, "menit")

# ------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------

# 2. Kamu ingin membeli cupang dg harga 10rb dan koi dg harga 20rb
#    uang yg kamu bawa sebesar Rp.XXX000 (ganti XXX dg 3 angka terakhir NIM + 100)
#    kamu hanya beli 5 cupang dan 2 koi
#    berapa sisa uang kamu?

# harga cupang dan koi
harga_cupang = 10000
harga_koi = 20000

# jumlah ikan yang dibeli
jumlah_cupang = 5
jumlah_koi = 2

# uang yang dibawa
uang = (41 + 100) * 1000

# total harga cupang dan koi
total_belanja = (harga_cupang * jumlah_cupang) + (harga_koi * jumlah_koi)

# sisa uang yang dibawa
sisa_uang = uang - total_belanja

print("sisa uang kamu adalah", sisa_uang)


# ------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------

# # 3. Kamu ingin pergi liburan dg sepeda motor
#    total jarak perjalanan XXX KM (ganti XXX dg 3 angka terakhir NIM)
#    konsumsi BBM sepeda motor 2.7 KM per Liter
#    kapasitas tangki sepeda motor X Liter (ganti X dg 1 angka terakhir NIM)
#    harga bensin per liter Rp.1XXX0 (ganti XXX dg 3 angka terakhir NIM)
#    jika total bensin yg dibutuhkan > 3 liter, maka dapat diskon Rp.500 per liter
#    berapa total bensin yg dibutuhkan, harga bensin per liter setelah diskon (jika ada)- 
#    total biaya bensin, dan prakiraan berapa kali kamu harus mengisi bensin (dengan asumsi tangki penuh setiap kali isi)?
#    NB: HARUS PAKAI INPUT !!!!!

jarak = float(input("Masukkan jarak tempuh (dalam km): "))
konsumsi_bbm_per_liter = float(input("Masukkan konsumsi BBM per liter (km/liter): "))
kapasitas_tangki = float(input("Masukkan kapasitas tangki (dalam liter): "))
harga_bbm_per_liter = float(input("Masukkan harga BBM per liter (Rp): "))

# menghitung total bbm yang dibutuhkan
total_bbm_dibutuhkan = jarak / konsumsi_bbm_per_liter

# cek apakah ada diskon 
if total_bbm_dibutuhkan > 3:
    harga_bbm_diskom = harga_bbm_per_liter - 500
else:
    harga_bbm_diskom = harga_bbm_per_liter

# menghitung total biaya
total_biaya = total_bbm_dibutuhkan * harga_bbm_diskom

# hitung berapa kali isi ulang
import math
jumlah_isi_ulang = math.ceil(total_bbm_dibutuhkan / kapasitas_tangki)

print ( "total bensin yang di butuhkan : liter", total_bbm_dibutuhkan)
print ("harga bensin per liter setelah diskon : Rp", harga_bbm_diskom)
print ("total biaya yang harus di keluarkan : Rp", total_biaya)
print ("jumlah isi ulang : ", jumlah_isi_ulang, "kali")
  



# ------------------------------------------------------------------------------------------------