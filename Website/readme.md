# ProjectClassicControl - Proje Yapısı

## 📁 Klasör Yapısı

```
ProjectClassicControl/
│
├── app.py                      # Flask ana uygulama dosyası
├── requirements.txt            # Python bağımlılıkları
├── README.md                   # Proje açıklaması
│
├── templates/                  # HTML şablonları
│   └── index.html             # Ana sayfa (artifact'teki HTML kodu)
│
├── static/                     # Static dosyalar
│   ├── css/
│   │   └── style.css          # CSS dosyaları (isteğe bağlı)
│   ├── js/
│   │   └── main.js            # JavaScript dosyaları (isteğe bağlı)
│   └── images/
│       └── favicon.ico        # Site ikonu
│
└── .gitignore                 # Git ignore dosyası
```

## 🚀 Kurulum ve Çalıştırma

### 1. Sanal Ortam Oluşturma (Önerilen)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Bağımlılıkları Yükleme

```bash
pip install -r requirements.txt
```

### 3. Proje Yapısını Oluşturma

```bash
# Klasörleri oluştur
mkdir templates static
mkdir static/css static/js static/images

# HTML dosyasını templates klasörüne kopyala
# (Artifact'teki HTML kodunu templates/index.html olarak kaydet)
```

### 4. Uygulamayı Çalıştırma

```bash
python app.py
```

Tarayıcınızda şu adresi açın: **http://localhost:5000**

## 🔧 Geliştirme Modu

Flask otomatik olarak debug modunda çalışır. Dosyalarda değişiklik yaptığınızda server otomatik yeniden başlar.

## 📦 Production Deployment

### Gunicorn ile (Linux/Mac)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### uWSGI ile

```bash
pip install uwsgi
uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app
```

### Docker ile (Opsiyonel)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## 🌐 Nginx Reverse Proxy (Önerilen)

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/ProjectClassicControl/static;
    }
}
```

## 📝 .gitignore Dosyası

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Flask
instance/
.webassets-cache

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

## 🔐 Güvenlik Notları

Production için:
- `debug=False` yapın
- SECRET_KEY ekleyin
- HTTPS kullanın
- CORS ayarlarını yapılandırın
- Rate limiting ekleyin

## 📚 Ek Özellikler Eklemek İçin

### API Endpoint Örneği

```python
from flask import jsonify

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'online',
        'version': '1.0.0',
        'demo': True
    })
```

### Form İşleme

```python
from flask import request

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Email gönderme veya veritabanına kaydetme
    return jsonify({'success': True})
```

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request açın

## 📄 Lisans

MIT License - Detaylar için LICENSE dosyasına bakın.

## 📧 İletişim

- Email: alazkanatiha@gmail.com
- Instagram: [@classic_iha](https://www.instagram.com/classic_iha/)
- Instagram: [@alazkanathtk](https://www.instagram.com/alazkanathtk/)