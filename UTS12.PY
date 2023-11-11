pendapatan = 12000000
biaya = 1000000
jumlah_karyawan = 120

if pendapatan > biaya and jumlah_karyawan > 100 :
	print ("Perusahaan menghasilkan laba dan jumlah karyawan lebih dari 100.")
elif pendapatan > biaya or jumlah_karyawan > 100:
	print ("Perusahaan menghasilkan laba atau jumlah karyawan lebih dari 100.")
else:
	print ("Perusahaan tidak menghasilkan laba dan jumlah karyawan 100 atau lebih.")