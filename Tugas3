CREATE DATABASE toko_online;
USE toko_online;

-- 1. Tabel Pembeli
CREATE TABLE pembeli (
    email VARCHAR(100) PRIMARY KEY,
    nama VARCHAR(100),
    alamat TEXT
);

-- 2. Tabel Penjual
CREATE TABLE penjual (
    email VARCHAR(100) PRIMARY KEY,
    nama VARCHAR(100)
);

-- 3. Tabel Barang
CREATE TABLE barang (
    sku VARCHAR(20) PRIMARY KEY,
    tanggal_jual DATE,
    stok INT,
    harga_jual DECIMAL(12,2)
);

-- 4. Tabel Membeli (Relasi Pembeli - Barang)
CREATE TABLE membeli (
    sku VARCHAR(20),
    email_pembeli VARCHAR(100),
    tanggal_beli DATE,
    jumlah INT,
    total_harga DECIMAL(12,2),

    FOREIGN KEY (sku) REFERENCES barang(sku),
    FOREIGN KEY (email_pembeli) REFERENCES pembeli(email)
);

-- 5. Tabel Menjual (Relasi Barang - Penjual)
CREATE TABLE menjual (
    sku VARCHAR(20),
    email_penjual VARCHAR(100),

    FOREIGN KEY (sku) REFERENCES barang(sku),
    FOREIGN KEY (email_penjual) REFERENCES penjual(email)
);
