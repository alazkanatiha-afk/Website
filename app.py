# app.py - Flask Backend for ProjectClassicControl Website

from flask import Flask, render_template_string, send_from_directory
import os

# Flask uygulaması oluştur
app = Flask(__name__, static_folder='static')

# HTML içeriği (artifact'teki HTML kodu buraya gelecek)
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ProjectClassicControl - UAV Kontrol Sistemi</title>
    <!-- Buraya artifact'teki tüm HTML kodu gelecek -->
    <!-- index.html dosyasını templates klasörüne kopyalayın -->
</head>
<body>
    <h1>Lütfen index.html dosyasını templates klasörüne kopyalayın</h1>
    <p>Artifact'teki HTML kodunu templates/index.html olarak kaydetmelisiniz.</p>
</body>
</html>
"""

# Ana sayfa route'u
@app.route('/')
def index():
    """Ana sayfa - HTML içeriğini render eder"""
    # templates/index.html varsa onu kullan, yoksa HTML_CONTENT'i kullan
    try:
        from flask import render_template
        return render_template('index.html')
    except:
        return render_template_string(HTML_CONTENT)

# Dil sayfaları
@app.route('/index_en.html')
def index_en():
    """İngilizce sayfa"""
    try:
        from flask import render_template
        return render_template('index_en.html')
    except:
        return render_template_string(HTML_CONTENT)

@app.route('/index_ru.html')
def index_ru():
    """Rusça sayfa"""
    try:
        from flask import render_template
        return render_template('index_ru.html')
    except:
        return render_template_string(HTML_CONTENT)

@app.route('/index_de.html')
def index_de():
    """Almanca sayfa"""
    try:
        from flask import render_template
        return render_template('index_de.html')
    except:
        return render_template_string(HTML_CONTENT)

# Hakkında sayfası
@app.route('/about')
def about():
    """Hakkında sayfası"""
    return index()

# Özellikler sayfası
@app.route('/features')
def features():
    """Özellikler sayfası"""
    return index()

# Gelecek planları sayfası
@app.route('/future')
def future():
    """Gelecek planları sayfası"""
    return index()

# GitHub yönlendirme
@app.route('/github')
def github():
    """GitHub sayfasına yönlendirme"""
    return index()

# Static dosyalar için route (CSS, JS, resimler)
@app.route('/static/<path:filename>')
def static_files(filename):
    """Static dosyaları serve et"""
    return send_from_directory('static', filename)

# Favicon route'u
@app.route('/favicon.ico')
def favicon():
    """Favicon serve et"""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Hata sayfaları
@app.errorhandler(404)
def page_not_found(e):
    """404 Hata sayfası"""
    return index(), 404

@app.errorhandler(500)
def internal_server_error(e):
    """500 Hata sayfası"""
    return index(), 500

# Debug modunda çalıştır
if __name__ == '__main__':
    # templates klasörünü oluştur
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("⚠️  'templates' klasörü oluşturuldu!")
        print("📝 Lütfen artifact'teki HTML kodunu 'templates/index.html' olarak kaydedin.")
    
    # static klasörünü oluştur
    if not os.path.exists('static'):
        os.makedirs('static')
        print("⚠️  'static' klasörü oluşturuldu!")
    
    # Development server
    print("\n🚀 Flask server başlatılıyor...")
    print("🌐 Tarayıcınızda şu adresi açın: http://localhost:5000")
    print("⏹️  Durdurmak için: CTRL+C\n")
    
    app.run(
        host='0.0.0.0',  # Tüm network interface'lerinden erişim
        port=5000,        # Port numarası
        debug=True        # Debug modu (geliştirme için)
    )