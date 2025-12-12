# Online Food Delivery System
Tugas Besar II3160 Teknologi Sistem Terdistribusi
> 18223122 Anggita Najmi Layali

Aplikasi ini merupakan tugas besar mata kuliah II3160 Teknologi Sistem Terdistribusi. Sistem yang dikembangkan berfokus pada Customer-facing Ordering Context, yaitu proses inti pemesanan makanan pada layanan food delivery: membuat order, menambah item, menjadwalkan, checkout, membatalkan, hingga konfirmasi pesanan selesai. Proyek dibangun menggunakan arsitektur Domain-Driven Design (DDD) dengan FastAPI sebagai web framework.

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688?logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-499848?logo=gunicorn&logoColor=white)

---

## Daftar Isi

- [Cara Menjalankan Aplikasi](#cara-menjalankan-aplikasi)
- [Struktur Folder Utama](#struktur-folder-utama)
- [Arsitektur Domain-Driven Design](#arsitektur-domain-driven-design)
- [Daftar Fitur yang Diimplementasi](#daftar-fitur-yang-diimplementasi)
- [Contributors](#contributors)

---

## Cara Menjalankan Aplikasi

**Prasyarat:**  
- Python 3.13 atau lebih baru
- pip (Python package manager)

**Langkah-langkah:**
1. Clone repository:
   ```bash
   git clone https://github.com/gitaa001/II3160_TB_18223122.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd II3160_TB_18223122
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Atau install secara manual:
   ```bash
   pip install fastapi uvicorn python-multipart
   ```
4. Jalankan aplikasi:
   ```bash
   python -m uvicorn main:app --reload
   ```
   Atau:
   ```bash
   python main.py
   ```
5. Akses aplikasi di browser:
   ```
   http://localhost:8000
   ```
   Dokumentasi API tersedia di:
   ```
   http://localhost:8000/docs
   ```

---

## Struktur Folder Utama

Struktur folder utama pada aplikasi ini mengikuti prinsip Domain-Driven Design (DDD), memisahkan kode berdasarkan layer tanggung jawab:

```
II3160_TB_18223122/
├── main.py                          # Entry point aplikasi
├── README.md                        # Dokumentasi proyek
└── src/
    ├── api/                         # API Layer (Controllers)
    │   ├── AuthController.py        # Endpoint autentikasi
    │   └── CustomerController.py    # Endpoint customer & order
    ├── application/                 # Application Layer (Services)
    │   └── OrderService.py          # Business logic pemesanan
    ├── auth/                        # Authentication & Authorization
    │   ├── auth.py                  # JWT token handler
    │   ├── config.py                # Konfigurasi security
    │   └── dependency.py            # FastAPI dependencies
    ├── domain/                      # Domain Layer
    │   ├── entities/                # Domain Entities
    │   │   ├── Order.py             # Entitas Order
    │   │   └── OrderItem.py         # Entitas OrderItem
    │   ├── events/                  # Domain Events
    │   │   ├── OrderCreated.py      # Event pembuatan order
    │   │   └── OrderDelivered.py    # Event pengiriman selesai
    │   └── value_objects/           # Value Objects
    │       ├── Money.py             # Value object uang
    │       ├── Quantity.py          # Value object kuantitas
    │       └── ScheduledTime.py     # Value object jadwal
    └── infrastructure/              # Infrastructure Layer
        └── OrderRepository.py       # Data persistence
```

---

## Arsitektur Domain-Driven Design

Aplikasi ini menerapkan arsitektur DDD dengan pembagian layer sebagai berikut:

### 1. **Domain Layer** (`src/domain/`)
Layer inti yang berisi business logic murni, tidak bergantung pada framework atau infrastruktur:
- **Entities**: Objek dengan identitas unik (Order, OrderItem)
- **Value Objects**: Objek tanpa identitas, immutable (Money, Quantity, ScheduledTime)
- **Domain Events**: Event yang terjadi dalam domain (OrderCreated, OrderDelivered)

### 2. **Application Layer** (`src/application/`)
Orchestration layer yang mengkoordinasikan use case dan business logic:
- **Services**: Mengelola alur bisnis kompleks yang melibatkan multiple entities

### 3. **API Layer** (`src/api/`)
Interface layer untuk komunikasi dengan client:
- **Controllers**: REST API endpoints yang menerima HTTP requests

### 4. **Infrastructure Layer** (`src/infrastructure/`)
Layer untuk integrasi dengan sistem eksternal:
- **Repositories**: Abstraksi akses data dan persistence

### 5. **Auth Module** (`src/auth/`)
Cross-cutting concern untuk autentikasi dan otorisasi menggunakan JWT.

---

## Daftar Fitur yang Diimplementasi

### Customer-Facing Ordering Context
1. **Autentikasi & Otorisasi**
   - Login customer dengan JWT token
   - Protected endpoints dengan role-based access

2. **Order Management**
   - Membuat order baru
   - Menambah item ke order
   - Menjadwalkan waktu pengiriman
   - Checkout order
   - Membatalkan order
   - Konfirmasi pesanan selesai (delivered)

3. **Domain Events**
   - Event `OrderCreated` dipublikasikan saat order dibuat
   - Event `OrderDelivered` dipublikasikan saat pesanan selesai

4. **Value Objects**
   - `Money`: Mengelola nilai uang dengan validasi
   - `Quantity`: Mengelola kuantitas item dengan validasi
   - `ScheduledTime`: Mengelola waktu penjadwalan

