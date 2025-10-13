# LN Collection - Perpustakaan Light Novel Pribadi

Aplikasi web berbasis Django untuk mengelola koleksi Light Novel pribadi. Pengguna dapat mendaftar, login, dan mengelola koleksi buku mereka sendiri secara privat, lengkap dengan foto profil dan detail buku.

![Screenshot Aplikasi LN Collection](https://github.com/Kemalhafizh/Perpustakaan-Digital-Pribadiku/blob/main/screenshot.png?raw=true)

---

## ✨ Fitur Utama (Features)

* **Autentikasi Pengguna:** Sistem registrasi, login, dan logout yang aman menggunakan sistem bawaan Django.
* **Manajemen Profil:** Pengguna dapat memperbarui info akun (username, email) dan mengunggah foto profil (avatar).
* **CRUD Penuh:** Fungsionalitas Tambah, Lihat, Edit, dan Hapus (Create, Read, Update, Delete) untuk setiap entri buku di koleksi.
* **Koleksi Pribadi:** Setiap pengguna hanya dapat melihat dan mengelola koleksi buku miliknya sendiri.
* **Pencarian Real-time:** Bar pencarian untuk memfilter koleksi berdasarkan judul atau penulis.
* **Desain Modern & Interaktif:** UI dengan tema gelap, efek hover, dan animasi yang dibuat dengan CSS modern.

---

## 🛠️ Teknologi yang Digunakan (Tech Stack)

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite3 (untuk development)
* **Lainnya:** Pillow (untuk pemrosesan gambar)

---

## 🚀 Cara Menjalankan Proyek Secara Lokal (Setup & Installation)

Berikut adalah langkah-langkah untuk menjalankan proyek ini di komputer Anda.

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/Kemalhafizh/Perpustakaan-Digital-Pribadiku.git
    cd Perpustakaan-Digital-Pribadiku
    ```

2.  **Masuk ke folder proyek Django:**
    ```bash
    cd myproject
    ```

3.  **Buat dan aktifkan virtual environment:**
    ```bash
    # (Pastikan Anda berada di folder yang berisi 'venv')
    # Jika menggunakan PowerShell di Windows:
    .\venv\Scripts\Activate.ps1
    ```

4.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Jalankan migrasi database:**
    ```bash
    python manage.py migrate
    ```

6.  **Buat akun superuser (admin):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Jalankan server pengembangan:**
    ```bash
    python manage.py runserver
    ```

8.  Buka browser Anda dan kunjungi `http://127.0.0.1:8000/`.