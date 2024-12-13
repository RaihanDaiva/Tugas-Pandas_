import pandas as pd
    
# No 1 ()
print("No 1")
data_sampah = pd.read_excel('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx')
print(data_sampah[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']])
data_sampah.to_csv('no_1.csv', index=False)
data_sampah.to_excel('no_1.xlsx', index=False)


# No 2 ()
print("\nNo 2")
jumlah_2018 = {2018: 0}
thn = 2018
for index, row in data_sampah.iterrows():
    if row['tahun'] == thn:
        jmlh = row['jumlah_produksi_sampah']
        jumlah_2018[thn] += jmlh
    
print(jumlah_2018)
df_jumlah_2018 = pd.DataFrame(list(jumlah_2018.items()), columns=['Tahun', 'Jumlah Produksi Sampah'])
df_jumlah_2018.to_csv('no_2.csv', index=False)
df_jumlah_2018.to_excel('no_2.xlsx', index=False)

# No 3 ()
print("\nNo 3")
jumlah_per_tahun = {}
for index, row in data_sampah.iterrows():
    tahun3 = row['tahun']
    jumlah3 = row['jumlah_produksi_sampah']  
    if tahun3 not in jumlah_per_tahun:
        jumlah_per_tahun[tahun3] = 0
    jumlah_per_tahun[tahun3] += jumlah3
    jumlah_per_tahun[tahun3] = round(jumlah_per_tahun[tahun3], 2)
    
df_jumlah_per_tahun = pd.DataFrame(list(jumlah_per_tahun.items()), columns=['Tahun', 'Jumlah Produksi Sampah'])
print(df_jumlah_per_tahun)
df_jumlah_per_tahun.to_csv('no_3.csv', index=False)
df_jumlah_per_tahun.to_excel('no_3.xlsx', index=False)   

# No 4 ()
print("\nNo 4")
jumlah_perkota_perthn = {}
for index, row in data_sampah.iterrows():
    kota4 = row['nama_kabupaten_kota']
    tahun4 = row['tahun']
    jumlah4 = row['jumlah_produksi_sampah']
    
    if kota4 not in jumlah_perkota_perthn:
        jumlah_perkota_perthn[kota4] = {}
        
    if tahun4 not in jumlah_perkota_perthn[kota4]:
        jumlah_perkota_perthn[kota4][tahun4] = 0
    jumlah_perkota_perthn[kota4][tahun4] += jumlah4
     
data_list = []
for kota, tahun_data in jumlah_perkota_perthn.items():
    for tahun, jumlah in tahun_data.items():
        data_list.append({'Kota': kota, 'Tahun': tahun, 'Jumlah_Produksi_sampah': jumlah})
        
df_jumlah_perkota_pertahun = pd.DataFrame(data_list)
print(df_jumlah_perkota_pertahun)
df_jumlah_perkota_pertahun.to_csv('no_4.csv', index=False)
df_jumlah_perkota_pertahun.to_excel('no_4.xlsx', index=False)   