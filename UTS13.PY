data_penjualan = [
	{'nama':'Minyak goreng', "penjualan" : 5000},
	{"nama": "Tepung", "penjualan": 15000}, 
	{"nama": "Telor" , "penjualan": 3000},
	{"nama": "Mentega" , "penjualan": 10000},
]
total_penjualan = sum([item["penjualan"] for item in data_penjualan])
rata_rata_penjualan = total_penjualan / len(data_penjualan)
for item in data_penjualan:
	if item["penjualan"] > rata_rata_penjualan:
		print(f"(item['nama']penjualannya di atas rata-rata.")
	else:
		print (f"(item['nama'] penjualannya di bawah rata-rata.")
