import csv

def load():
    # Database user.csv
    user = [["" for j in range(7)] for i in range(100)]
    #[nama,tanggal,tinggi,username,pwd,role,saldo]

    # Database wahana.csv
    wahana = [["" for j in range(5)] for i in range(100)]
    #[id wahana,nama wahana,harga wahana,batas umur, batas tinggi]

    # Database pembelian.csv
    pembelian = [["" for j in range(4)] for i in range(100)]
    #[username,tanggal beli,id wahana, jumlah tiket]

    # Database penggunaan.csv
    penggunaan = [["" for j in range(4)] for i in range(100)]
    #[username,tanggal beli,id wahana, jumlah tiket]

    # Database tiket.csv
    tiket = [["" for j in range(3)] for i in range(100)]
    #[username,id wahana,jumlah tiket]

    # Database refund.csv
    refund = [["" for j in range(4)] for i in range(100)]
    #[username,tanggalrefund,id wahana,jumlah tiket]

    # Database kritiksaran.csv
    kritiksaran = [["" for j in range(4)] for i in range(100)]
    #[username,tanggalkritik,idwahana,isikritik]

    # Database kehilangan.csv
    kehilangan = [["" for j in range(4)] for i in range(100)]
    #[username,tanggalkehilangan,idwahana,jumlahtiket]

    print("Masukkan nama File {:18}: ".format("User"),end="")
    usdb = input()
    with open(usdb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                user[i] = tp

    print("Masukkan nama File {:18}: ".format("Daftar Wahana"),end="")
    wadb = input()
    with open(wadb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                wahana[i] = tp

    print("Masukkan nama File {:18}: ".format("Pembelian Tiket"),end="")
    bedb = input()
    with open(bedb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                pembelian[i] = tp

    print("Masukkan nama File {:18}: ".format("Penggunaan Tiket"),end="")
    gudb = input()
    with open(gudb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                penggunaan[i] = tp

    print("Masukkan nama File {:18}: ".format("Kepemilikan Tiket"),end="")
    tidb = input()
    with open(tidb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                tiket[i] = tp

    print("Masukkan nama File {:18}: ".format("Refund Tiket"),end="")
    redb = input()
    with open(redb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                refund[i] = tp

    print("Masukkan nama File {:18}: ".format("Kritik dan Saran"),end="")
    krdb = input()
    with open(krdb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                kritiksaran[i] = tp

    print("Masukkan nama File {:18}: ".format("Kehilangan Tiket"),end="")
    hidb = input()
    with open(hidb) as f:
        s = csv.reader(f)
        s.__next__() # Skip baris teratas
        for i in range(99):
            tp = s.__next__()
            if tp[0] == "~~~":
                break
            else:
                kehilangan[i] = tp

    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.\n")
    return (user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan)
