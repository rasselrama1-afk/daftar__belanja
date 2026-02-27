import database  # Wajib ada agar backend bisa akses database

def tambah_item(nama):
    # Gunakan database.baca_data() bukan baca_data() saja
    daftar = database.baca_data() 
    daftar.append(nama)
    database.tulis_data(daftar)
    return f"✅ '{nama}' berhasil ditambahkan."

def semua_item():
    return database.baca_data()

def hapus_item(no):
    daftar = database.baca_data()
    if 1 <= no <= len(daftar):
        item = daftar.pop(no - 1)
        database.tulis_data(daftar)
        return f"❌ '{item}' dihapus."
    else:
        return "⚠️ Nomor tidak valid."

def edit_item(no,nama_baru):
    """mengedit item pada nomor urut tertentu"""
    daftar = database.baca_data()
    if 1 <= no <= len(daftar):
        item_lama = daftar[no - 1]
        daftar[no - 1] = nama_baru
        database.tulis_data(daftar)
        return f" '{item_lama}' diubah menjadi '{nama_baru}'."
   
    else:
        
        return "nomor tidak valid"
        
def cari_item(kata_kunci):
    """mengembalikan daftar item yang mengandung kata kunci"""
    daftar = database.baca_data()
    hasil = [item for item in daftar if kata_kunci.lower() in item.lower()]
    return hasil
    
def tambah_item_handler():
    item = input("Nama item: ")
    if item.strip() == "":
        print("⚠️ Nama item tidak boleh kosong.")
        logger.tulis_log("Peringatan: input item kosong")
    else:
        pesan = backend.tambah_item(item)
        print(pesan)
        logger.tulis_log(f"Menambah item: {item}")
        
def lihat_item_handler():
    daftar = backend.semua_item()
    if not daftar:
        print("📭 Daftar belanja kosong.")
        logger.tulis_log("Melihat daftar {kosong}.")
    else:
        print("\n Daftar belanja:")
        tampilkan_daftar(daftar)
        logger.tulis_log("Melihat daftar item")