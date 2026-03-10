# VSK Bike Spare Parts – Django Shop

A production-ready Django website for a bike spare parts retail shop with WhatsApp ordering.

## 🚀 Quick Start (Local Development)

### 1. Create virtual environment & install dependencies

```bash
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Configure environment variables

Edit the `.env` file:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
SHOP_OWNER_PHONE=919876543210   # WhatsApp number with country code, no +
SHOP_NAME=VSK Bike Spare Parts
```

### 3. Run migrations & create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run development server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000  
Admin: http://127.0.0.1:8000/admin

---

## 📦 Adding Products (Admin Panel)

1. Go to http://127.0.0.1:8000/admin
2. Log in with your superuser credentials
3. Click **Products → Add Product**
4. Fill in Name, Description, Price, Image, Stock
5. Save – product appears on the homepage immediately

---

## 💬 WhatsApp Ordering Flow

```
Customer browses products
    ↓
Clicks "Order Now"
    ↓
Fills Name, Phone, Address, Pincode, Quantity
    ↓
Order saved to database
    ↓
Success page shown
    ↓
WhatsApp opens automatically with pre-filled message
    ↓
Shop owner receives complete order on WhatsApp
```

---

## 🏭 Production Deployment (Linux VPS + Gunicorn + Nginx)

### Step 1 – Server setup

```bash
sudo apt update && sudo apt install python3-pip python3-venv nginx -y
```

### Step 2 – Upload project & install dependencies

```bash
cd /var/www/
git clone <your-repo> bikeshop
cd bikeshop
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3 – Configure .env for production

```env
SECRET_KEY=<generate-strong-secret-key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SHOP_OWNER_PHONE=919876543210
SHOP_NAME=VSK Bike Spare Parts
```

### Step 4 – Collect static files & migrate

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### Step 5 – Gunicorn systemd service

Create `/etc/systemd/system/bikeshop.service`:

```ini
[Unit]
Description=VSK Bike Shop Gunicorn
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/bikeshop
ExecStart=/var/www/bikeshop/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/run/bikeshop.sock \
    config.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable bikeshop
sudo systemctl start bikeshop
```

### Step 6 – Nginx configuration

Create `/etc/nginx/sites-available/bikeshop`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    client_max_body_size 10M;

    location /static/ {
        alias /var/www/bikeshop/staticfiles/;
    }

    location /media/ {
        alias /var/www/bikeshop/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/bikeshop.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/bikeshop /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 7 – SSL with Certbot (HTTPS)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## 🗂️ Project Structure

```
bike_shop/
├── config/               ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── context_processors.py
├── apps/
│   ├── products/         ← Product catalog app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   └── orders/           ← Order & WhatsApp app
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── admin.py
├── templates/
│   ├── base.html
│   ├── products/product_list.html
│   └── orders/
│       ├── order_form.html
│       └── order_success.html
├── static/
│   ├── css/style.css
│   └── js/main.js
├── media/                ← Uploaded product images
├── requirements.txt
├── .env
└── manage.py
```

---

## 📱 WhatsApp Number Format

The `SHOP_OWNER_PHONE` in `.env` must be in international format **without** `+`:

| Country | Example |
|---------|---------|
| India   | `919876543210` |
| US      | `14155552671`  |
| UK      | `447911123456` |
