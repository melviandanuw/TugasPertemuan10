# <p align="center"> TUGAS PEMROGRAMAN Pertemuan 10 - Latihan1.py & TugasPraktikum.py
[![melvian](./images/melvian.png)](https://www.linkedin.com/in/melvian-wijaya-760b371b1/)


<br>


# [Latihan.py]

<p align="justify">Menampilkan, Delete, Ubah data dari Dictionary.

- Print Kontak berdasarkan Key.
```sh
kontakDict['Ari'];
```
- Tambah Kontak Dict.
```sh
kontakDict['Riko'] = '087654544';
```
- Ubah Kontak.
```sh
kontakDict['Dina'] = '088999776';
```
- Tampilkan semua data berdasarkan Key.
```sh
print('Print semua nama:', kontakDict.keys());
```
- Tampilkan semua data berdasarkan Value.
```sh
print('Print semua nomor:', kontakDict.values());
```
- Tampilkan semua data.
```sh
print('Tampilkan nama dan nomor:\n', kontakDict);
```
- Hapus data berdasarkan Key.
```sh
kontakDict.pop('Dina');
```
----

# Hasil Output Latihan.py
![Output](./images/latihan.png)

----

<br>

<br>

<br>

# [TugasPraktikum.py](https://github.com/melviandanuw/TugasKelilingLuasLingkaran/blob/main/tugas.py)

<p align="justify">Program Data sederhana menggunakan List & Dictionary dengan menu Tambah, Ubah, Tampilkan, Hapus, dan Cari.

- Import Libary Tabulate untuk membuat table.
```sh
from tabulate import tabulate;
```
- Membuat Dictionary.
```sh
datas = [{
    'nama' : 'No Data Found!'    
}];
```
- Menggunakan perulangan While, selama masih true maka program akan tetap berjalan.
```sh
while (True):
```
- Menggunakan If Else untuk menentukan menu.
```sh
if inputs == 't':
```
- Membuat proses input, append, dan menghapus data.
```sh
    // Input data untuk ditambahkan ke dalam Dict.
        inputNama = str(input('Masukan Nama: '));
        inputNik = int(input('Masukan NIK: '));
        inputNilaiTugas = int(input('Masukan Nilai Tugas: '));
        inputNilaiUTS = int(input('Masukan Nilai UTS: '));
        inputNilaiUAS = int(input('Masukan Nilai UAS: '));

    // Proses aritmatika untuk menghitung Nilai Akhir.
        nilaiAkhir = (inputNilaiTugas * 0.30) + (inputNilaiUAS * 0.35) + (inputNilaiUTS * 0.35);
        
    // Menghapus 'Data Not Found'.
        if datas[0]['nama'] == 'No Data Found!':
            del datas[0];
    
    //Data Append ke List yang berisi Dict.
        dataAppend = {'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS, 'nAkhir' : nilaiAkhir};    
        datas.append(dataAppend);
        print('Data Telah Terinput');
```
- Proses mengubah data pada menu Ubah.
```sh
                datas[i]['nTugas'] = inputNilaiTugas;
                datas[i]['nUTS'] = inputNilaiUTS;
                datas[i]['nUAS'] = inputNilaiUAS;
                datas[i]['nAkhir'] = nilaiAkhir;
```
- Proses menghapus data pada menu Hapus.
```sh
                del datas[i]['nama'];
                del datas[i]['nik'];
                del datas[i]['nTugas'];
                del datas[i]['nUTS'];
                del datas[i]['nUAS'];
                del datas[i]['nAkhir'];
```
- Proses mencari data pada menu Cari.
```sh
                for i in range(0, len(datas)):
                if inputNamaUpdate in datas[i]['nama']:
                
                headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
    
                print(tabulate(datas[i]['nama'], headers=headers, tablefmt='fancy_grid', stralign='center'));

```
- Proses menampilkan data menggunakan Library Tabulate.
```sh
        if datas[0]['nama'] == 'No Data Found!':
            print(tabulate([datas], tablefmt='fancy_grid', stralign='center'));
        
        else:
            rows =  [x.values() for x in datas];
            headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
            print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
```
----

# Hasil Output TugasPraktikum.py
![Output](./images/tugasPraktikum.png)


# Flowchart
![Output](./images/Flowchart.png)

