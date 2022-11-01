# 3. Buat contoh kode program untuk logika pencabangan if


falkultas_ubj =['hukum', 'teknik', 'psikologi', 'ilmu komunikasi', 'ilmu pendidikan', 'ilmu komputer', 'ekonomi dan bisnis']
hukum =['ilmu hukum']
teknik =['teknik industri', 'teknik kimia', 'teknik lingkungan', 'teknik perminyakan']
psikologi =['psikologi']
ilmu_komunikasi =['ilmu komunikasi']
ilmu_pendidikan =['pendidikan guru sekolah dasar', 'pendidikan kepelatihan olahraga']
ilmu_komputer =['informatika']
ekonomi_dan_bisnis =['akuntansi', 'manajemen']


fakultas_yang_dicari = input('Masukan fakultas yang ingin dicari dengan huruf kecil: fakultas ')

if (fakultas_yang_dicari in falkultas_ubj):
  print('fakultas yang anda cari tersedia')
  prodi_yang_dicari = input('Masukan prodi yang ingin dicari dengan huruf kecil: prodi ')
  if (prodi_yang_dicari in hukum):
    print('Prodi yang anda cari tersedia')
  elif (prodi_yang_dicari in teknik):
    print('Prodi yang anda cari tersedia')
  elif (prodi_yang_dicari in psikologi):
    print('Prodi yang anda cari tersedia')
  elif (prodi_yang_dicari in ilmu_komunikasi):
    print('Prodi yang anda cari tersedia')
  elif (prodi_yang_dicari in ilmu_pendidikan):
    print('Prodi yang anda cari tersedia')
  elif (prodi_yang_dicari in ilmu_komputer):
    print('Prodi yang anda cari tersedia')
  elif (prodi_yang_dicari in ekonomi_dan_bisnis):
    print('Prodi yang anda cari tersedia')
  else:
    print('Maaf prodi yang anda cari tidak tersedia')
else:
  print('Maaf fakultas yang anda cari tidak tersedia')