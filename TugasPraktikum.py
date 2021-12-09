from tabulate import tabulate;

start = True;

datas = [{
    'nama' : 'No Data Found!'    
}];

print('Program Data Sederhana'.center(80,' '));

while (start):
    print('(T) Tambah Data, (U) Ubah Data, (H) Hapus Data, (S) Tampilkan Data, (F) Cari Data', '(E) Exit Program');

    inputUser = str(input('Pilih Menu: '));
    inputs = inputUser.lower();

    if inputs == 't':
        inputNama = str(input('Masukan Nama: '));
        inputNik = int(input('Masukan NIK: '));
        inputNilaiTugas = int(input('Masukan Nilai Tugas: '));
        inputNilaiUTS = int(input('Masukan Nilai UTS: '));
        inputNilaiUAS = int(input('Masukan Nilai UAS: '));
        
        nilaiAkhir = (inputNilaiTugas * 0.30) + (inputNilaiUAS * 0.35) + (inputNilaiUTS * 0.35);
        
        if datas[0]['nama'] == 'No Data Found!':
            del datas[0];
            
        dataAppend = {'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS, 'nAkhir' : nilaiAkhir};    
        datas.append(dataAppend);
        print('Data Telah Terinput');
        # print(datas);

    elif inputs == 'u':
        print('Data Akan diubah, silahkan masukan nama dari data dibawah ini: ');
        
        rows =  [x.values() for x in datas];
        headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
        
        inputNamaUpdate = str(input('Masukan Nama: '));
        for i in range(0, len(datas)):
            
            if datas[i]['nama'] == inputNamaUpdate:
                inputNilaiTugas = int(input('Masukan Nilai Tugas: '));
                inputNilaiUTS = int(input('Masukan Nilai UTS: '));
                inputNilaiUAS = int(input('Masukan Nilai UAS: '));
                nilaiAkhir = (inputNilaiTugas * 0.30) + (inputNilaiUAS * 0.35) + (inputNilaiUTS * 0.35);

                datas[i]['nTugas'] = inputNilaiTugas;
                datas[i]['nUTS'] = inputNilaiUTS;
                datas[i]['nUAS'] = inputNilaiUAS;
                datas[i]['nAkhir'] = nilaiAkhir;
                # datas.append({'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS});
                print('Data Telah Terupdate');
                # print(datas);

    elif inputs == 'h':
        print('Data akan dihapus, silahkan masukan nama dari data dibawah ini: ');
        
        rows =  [x.values() for x in datas];
        headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
        
        inputNamaUpdate = str(input('Masukan Nama: '));
        for i in range(0, len(datas)):
            
            if datas[i]['nama'] == inputNamaUpdate:
                del datas[i]['nama'];
                del datas[i]['nik'];
                del datas[i]['nTugas'];
                del datas[i]['nUTS'];
                del datas[i]['nUAS'];
                del datas[i]['nAkhir'];
                # datas.append({'nama' : inputNama, 'nik' : inputNik, 'nTugas' : inputNilaiTugas, 'nUTS' : inputNilaiUTS, 'nUAS' : inputNilaiUAS});
                print('Data Telah Dihapus');
                print(datas);
        

    elif inputs == 'f':
        print('Mencari data, silahkan masukan nama untuk mencari data: ');
        
        # rows =  [x.values() for x in datas];
        # headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
        # print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
        
        inputNamaUpdate = str(input('Masukan Nama: '));
        for i in range(0, len(datas)):
            
            if inputNamaUpdate in datas[i]['nama']:
                # rows =  datas[i];
                headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
                print(tabulate(datas[i]['nama'], headers=headers, tablefmt='fancy_grid', stralign='center'));
                # print(datas[i][inputNamaUpdate, 'nik']);
        

    elif inputs == 's':
        if datas[0]['nama'] == 'No Data Found!':
            print(tabulate([datas], tablefmt='fancy_grid', stralign='center'));
        else:
            rows =  [x.values() for x in datas];
            headers = ['Nama', 'NIK', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'];
            print(tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center'));
            
    elif inputs == 'e':
        print("Program dihentikan");
        start = False;
    
    else:
        print('Input Salah!');