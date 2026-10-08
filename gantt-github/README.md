# Proyek PPSI: RAN Partner Bekasi

## Gantt Chart

<!-- GANTT:START -->
**Diperbarui:** 8 Oktober 2026 (otomatis oleh GitHub Actions)

- Task selesai: **0 dari 52**
- Progres rata-rata semua task: **0%**
- Progres tertimbang bobot nilai: **0%**
- Task terlambat: **0**

```mermaid
gantt
    dateFormat YYYY-MM-DD
    axisFormat %d/%m
    todayMarker stroke-width:3px,stroke:#d73a4a,opacity:0.7
    section Fase 1 - Definisi Proyek
    Membentuk tim dan membagi peran :active, t1_1, 2026-10-05, 2026-10-12
    Menetapkan Project Manager dan ketua peran :active, t1_2, 2026-10-05, 2026-10-12
    Mencari calon klien dan memahami masalahnya :active, t1_3, 2026-10-05, 2026-10-19
    Mendiskusikan calon klien dan topik dengan dosen :active, t1_4, 2026-10-05, 2026-10-12
    Mengunduh paket template dan membaca petunjuk pengisian :active, t1_5, 2026-10-05, 2026-10-12
    Menyusun profil klien (slide singkat) :active, t1_6, 2026-10-05, 2026-10-12
    Membandingkan alternatif solusi (misal web vs desktop) :t1_7, 2026-10-12, 2026-10-19
    Memilih metodologi (Waterfall Agile Scrum) dan mengenali risiko :t1_8, 2026-10-12, 2026-10-19
    Menyusun Requirement Document (3 sampai 5 halaman) :t1_9, 2026-10-12, 2026-10-19
    Melampirkan lembar persetujuan klien bertanda tangan :t1_10, 2026-10-12, 2026-10-19
    Menyiapkan presentasi 3 sampai 5 slide :t1_11, 2026-10-12, 2026-10-19
    Hasil - Requirement Document + persetujuan klien :t1_12, 2026-10-12, 2026-10-19
    section Fase 2 - Perencanaan Proyek
    Menggambarkan proses bisnis dan gambaran sistem :t2_1, 2026-10-19, 2026-10-26
    Menilai kelayakan - teknis ekonomi operasional :t2_2, 2026-10-19, 2026-11-02
    Memecah pekerjaan dengan WBS :t2_3, 2026-10-26, 2026-11-02
    Menyusun jadwal dengan Gantt Chart :t2_4, 2026-10-26, 2026-11-02
    Hasil - Dokumen 01 Bagian II + Gantt Chart (Excel) :t2_5, 2026-10-26, 2026-11-02
    section Fase 3 - Analisis Kebutuhan
    Wawancara dan observasi bersama klien :t3_1, 2026-11-02, 2026-11-09
    Menyusun kebutuhan fungsional dan non-fungsional :t3_2, 2026-11-02, 2026-11-16
    Membuat use case / user story :t3_3, 2026-11-02, 2026-11-16
    Menentukan prioritas kebutuhan (MoSCoW) :t3_4, 2026-11-09, 2026-11-16
    Hasil - Software Requirement Specification (SRS) :t3_5, 2026-11-09, 2026-11-16
    Kuis 1 - analisis kebutuhan (vclass) :t3_6, 2026-11-09, 2026-11-16
    Peer assessment ke-1 (vclass) :t3_7, 2026-11-09, 2026-11-16
    section Fase 4 - Desain Sistem
    Merancang arsitektur sistem :t4_1, 2026-11-16, 2026-11-23
    Merancang proses bisnis dan basis data (ERD) :t4_2, 2026-11-16, 2026-11-30
    Membuat wireframe / mockup antarmuka :t4_3, 2026-11-16, 2026-11-30
    Mulai menyiapkan lingkungan pemrograman :t4_4, 2026-11-23, 2026-11-30
    Hasil - Software Design Description (SDD) :t4_5, 2026-11-23, 2026-11-30
    Kuis 2 - desain sistem (vclass) :t4_6, 2026-11-23, 2026-11-30
    Peer assessment ke-2 (vclass) :t4_7, 2026-11-23, 2026-11-30
    section Fase 5 - Pemrograman
    Sprint 1 - fitur dasar + demo progres di kelas :t5_1, 2026-11-30, 2026-12-07
    Sprint 2 - fitur lanjutan + demo progres di kelas :t5_2, 2026-12-07, 2026-12-14
    Deploy awal ke server uji :t5_3, 2026-12-07, 2026-12-14
    Melanjutkan pemrograman saat pekan UTS :t5_4, 2026-12-14, 2026-12-21
    Sprint 3 - semua fitur lengkap + demo progres di kelas :t5_5, 2026-12-21, 2026-12-28
    Memperbarui realisasi di Gantt Chart setiap sprint :t5_6, 2026-11-30, 2026-12-28
    Hasil - Aplikasi + Dokumen Implementasi dan Kode Modul :t5_7, 2026-12-21, 2026-12-28
    section Fase 6 - Pengujian Sistem
    Menyusun skenario pengujian modul dan integrasi :t6_1, 2026-12-28, 2027-01-04
    Menyusun skenario UAT bersama klien :t6_2, 2026-12-28, 2027-01-04
    Menjalankan pengujian dan mencatat bug :t6_3, 2026-12-28, 2027-01-04
    Memperbaiki bug lalu menguji ulang :t6_4, 2026-12-28, 2027-01-04
    Hasil - Skenario pengujian dan rencana UAT (Excel) :t6_5, 2026-12-28, 2027-01-04
    Kuis 3 - pengujian sistem (vclass) :t6_6, 2026-12-28, 2027-01-04
    Peer assessment ke-3 (vclass) :t6_7, 2026-12-28, 2027-01-04
    section Fase 7 - Penerapan dan Presentasi Akhir
    Menjalankan UAT dan memperbaiki temuan :t7_1, 2027-01-04, 2027-01-11
    Deploy final di lingkungan klien :t7_2, 2027-01-04, 2027-01-11
    Melatih pengguna dan membuat user manual :t7_3, 2027-01-04, 2027-01-18
    Serah terima (BAST) :t7_4, 2027-01-11, 2027-01-18
    Hasil - Dokumen Penerapan + User Manual :t7_5, 2027-01-04, 2027-01-11
    Menyusun laporan akhir dan presentasi akhir :t7_6, 2027-01-11, 2027-01-18
    Hasil - Laporan akhir dan presentasi :t7_7, 2027-01-11, 2027-01-18
    section Milestone Akademik
    UTS (Ujian Tengah Semester) :milestone, tM1, 2026-12-14, 0d
    UAS (Ujian Akhir Semester) :milestone, tM2, 2027-01-18, 0d
```

### Task terlambat

Tidak ada task yang melewati deadline.
<!-- GANTT:END -->

## Cara memakai

1. **Atur tanggal.** Ubah `start_date` di `config.json` menjadi tanggal Senin Minggu 1.
2. **Perbarui progres.** Edit kolom `progres` (0 sampai 100) di `tasks.csv` setiap sprint, lalu commit. Task dengan progres 100 dianggap selesai.
3. **Buat issue (sekali saja).** Buka tab Actions, pilih workflow "Gantt dan deteksi deadline", klik Run workflow, centang `create_issues`. Setiap task menjadi issue berjudul `[ID] nama task`.
4. **Selesai.** Setiap hari pukul 00:00 WIB workflow memperbarui Gantt di atas. Task yang lewat deadline dan progresnya belum 100 otomatis diberi label `terlambat` beserta komentar. Label dicabut sendiri saat progres menjadi 100 atau issue ditutup.

## Aturan deadline

Deadline sebuah task adalah hari Minggu di akhir `minggu_selesai`. Contoh dengan `start_date` 2026-10-05: task Minggu 1 sampai 2 berakhir pada 18 Oktober 2026.

## Uji coba lokal

```bash
python scripts/generate_gantt.py
GANTT_TODAY=2026-11-20 python scripts/sync_issues.py --dry-run   # simulasi tanggal tertentu
```

## Izin yang dibutuhkan

Di Settings, Actions, General, Workflow permissions, pilih **Read and write permissions** agar workflow bisa commit dan mengelola issue.
