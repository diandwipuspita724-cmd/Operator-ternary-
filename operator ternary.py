
print("===== DATA PASIEN RAWAT INAP =====")

nama = input("Masukkan nama pasien: ")
umur = int(input("Masukkan umur pasien: "))

print("\nPILIH JENIS PASIEN:")
print("1. Pasien Anak")
print("2. Pasien Dewasa")
print("3. Pasien Lansia")
print("4. Pasien Umum")
print("5. Pasien BPJS")
print("6. Pasien VIP")
print("7. Pasien VVIP")
print("8. Pasien Bedah")
print("9. Pasien Penyakit Dalam")
print("10. Pasien Intensif (ICU)")

pilihan = int(input("\nMasukkan pilihan (1-10): "))

jenis_pasien = "Pasien Anak" if pilihan == 1 else "Pasien Dewasa" if pilihan == 2 else "Pasien Lansia" if pilihan == 3 else "Pasien Umum" if pilihan == 4 else "Pasien BPJS" if pilihan == 5 else "Pasien VIP" if pilihan == 6 else "Pasien VVIP" if pilihan == 7 else "Pasien Bedah" if pilihan == 8 else "Pasien Penyakit Dalam" if pilihan == 9 else "Pasien Intensif (ICU)" if pilihan == 10 else "Pilihan Tidak Valid"

print("\n===== HASIL DATA PASIEN =====")
print("Nama Pasien  :", nama)
print("Umur         :", umur, "tahun")
print("Jenis Pasien :", jenis_pasien)
