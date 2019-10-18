nama = 'Novita Permata Sari'
program = 'Rangkaian Listrik'

print(f'program {program} oleh {nama}')

def hitung_tegangan(arus, hambatan):
    tegangan = arus * hambatan
    print(f'arus = {arus * 2}A dengan hambatan = {hambatan * 22}ohm')
    print(f'sehingga tegangan = {tegangan}volt')

# arus = 2
# hambatan = 22
tegangan = hitung_tegangan(2, 22)
tegangan = hitung_tegangan(1, 22)

def hitung_kapasitansi(muatan, tegangan):
    kapasitansi = muatan / tegangan
    print(f'muatan = {muatan / 10}Coulomb dengan tegangan = {tegangan / 22}Volt')
    print(f'sehingga kapasitansi = {kapasitansi}Farad')

# muatan = 10
# tegangan = 22
kapasitansi = hitung_kapasitansi(10, 22)
kapasitansi = hitung_kapasitansi(20, 24)

def hitung_daya(energi, waktu):
    daya = energi / waktu
    print(f'energi = {energi / 200}joule dengan waktu = {waktu / 5 * 60}sekon')
    print(f'sehingga daya = {daya}watt')

# energi = 200
# waktu = 5 * 60
daya = hitung_daya(200, 50 * 60)
daya = hitung_daya(250, 70 * 60)
