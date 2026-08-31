# Modern Görev ve Proje Takip Uygulaması (CRUD)

Bu proje; modern web geliştirme temellerini pekiştirmek amacıyla React, Tailwind CSS ve tarayıcı tabanlı LocalStorage kullanılarak geliştirilmiş bir CRUD (Create, Read, Update, Delete) uygulamasıdır.

## 🚀 Proje Özellikleri
- **Create (Ekle):** Yeni görev başlığı, kategorisi ve açıklaması ekleme.
- **Read / List (Listele):** Kayıtlı görevleri kategori rozetleri ve tarih bilgisiyle listeleme, toplam görev sayısını görüntüleme.
- **Update (Güncelle):** Mevcut görevin başlık, kategori ve açıklamasını form üzerinden düzenleme ve tamamlama durumunu (checkbox) değiştirme.
- **Delete (Sil):** Görevi listeden ve LocalStorage üzerinden kalıcı olarak kaldırma.
- **LocalStorage Kalıcılığı:** Tarayıcı yenilendiğinde verilerin kaybolmaması.
- **Duyarlı (Responsive) Tasarım:** Tailwind CSS ile mobil ve masaüstü uyumlu modern arayüz.

## 📁 Proje Dosya Ağacı
```text
src/
├── components/       # Tekrar kullanılabilir UI bileşenleri
│   ├── TaskForm.jsx  # Ekleme ve düzenleme formu
│   ├── TaskList.jsx  # Liste sarmalayıcısı
│   └── TaskItem.jsx  # Tekil görev kartı ve aksiyon butonları
├── pages/            # Sayfa bileşenleri
│   └── Dashboard.jsx # Ana ekran ve LocalStorage CRUD fonksiyonları
├── interfaces/       # Veri tipleri ve şablonlar
│   └── taskTypes.js  # Görev şablon modeli
├── App.jsx           # Ana sarmalayıcı bileşen
├── index.css         # Tailwind direktifleri
└── main.jsx          # React DOM render başlangıcı
```

## 🛠️ Kurulum ve Çalıştırma

1. Bağımlılıkları yükleyin:
```bash
npm install
```

2. Geliştirme sunucusunu başlatın:
```bash
npm run dev
```

3. Canlı / Üretim derlemesi (Build) almak için:
```bash
npm run build
```

## 🌐 Netlify Dağıtımı (Deployment)
1. GitHub reponuzu Netlify'a bağlayın.
2. Build Settings:
   - **Build command:** `npm run build`
   - **Publish directory:** `dist`
3. Projeniz saniyeler içinde canlıya alınacaktır.

## 📸 Ekran Görüntüsü
Ekran görüntüsü projenin çalıştığı ekrandan alınarak `screenshot.png` olarak eklenecektir.
