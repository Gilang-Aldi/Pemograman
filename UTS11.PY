harga = [5000, 12000, 7500, 20000, 14000]
i=0

while i < len (harga) :
	harga[i] = 'Rp' + str(harga[i])
	i += 1

print ('Harga dalam format mata uang:', harga)
'Rp20000', 'Rp14000' 