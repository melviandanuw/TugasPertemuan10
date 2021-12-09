kontakDict = {
    'Ari' : "085267888", 
    'Dina' : '087677776'
};

#Print Kontak Ari
print('Menampilkan kontak Ari:',kontakDict['Ari']);

#Tambah Kontak Riko
kontakDict['Riko'] = '087654544';

#Ubah Kontak Dina
kontakDict['Dina'] = '088999776';

#Print semua nama
print('Print semua nama:', kontakDict.keys());

#Print semua nomor
print('Print semua nomor:', kontakDict.values());

#Tampilkan nama dan nomor
print('Tampilkan nama dan nomor:\n', kontakDict);

#Hapus Kontak Dina
kontakDict.pop('Dina');

#Tampilkan nama dan nomor
print('Tampilkan nama dan nomor:\n', kontakDict);