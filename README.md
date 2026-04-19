#  Phimart — E-Commerce REST API

A full-featured e-commerce backend API built with **Django REST Framework**, featuring JWT authentication, product/category management, shopping cart, and order processing.

---

## 📋 Table of Contents

- [Phimart — E-Commerce REST API](#phimart--e-commerce-rest-api)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [🛠 Tech Stack](#-tech-stack)
  - [📁 Project Structure](#-project-structure)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Environment Variables](#environment-variables)
    - [Running the Server](#running-the-server)
  - [📄 API Documentation](#-api-documentation)
  - [🔗 API Endpoints](#-api-endpoints)
    - [Authentication](#authentication)
    - [Products](#products)
    - [Categories](#categories)
    - [Cart](#cart)
    - [Orders](#orders)
  - [🔐 Authentication Flow](#-authentication-flow)
  - [🤝 Contributing](#-contributing)
  - [👨‍💻 Author](#-author)
  - [📜 License](#-license)

---

## ✨ Features

- 🔐 **JWT Authentication** via Djoser (register, login, token refresh, logout)
- 📦 **Product Management** — list, detail, create, update, delete products
- 🗂️ **Category Management** — organize products into categories
- 🛒 **Shopping Cart** — add, update, and remove items from cart
- 📋 **Order Processing** — place orders and manage order history
- 📄 **Swagger/OpenAPI Documentation** — interactive API docs via drf-yasg
- 🔒 **Permission-based access control** — public browsing, authenticated actions

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Framework | Django, Django REST Framework |
| Authentication | Djoser + SimpleJWT |
| API Docs | drf-yasg (Swagger / ReDoc) |
| Database | PostgreSQL / SQLite (dev) |

---

## 📁 Project Structure

```
phimart/
│
├── phimart/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── product/                  # Products & Categories app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── order/                    # Orders app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── cart/                     # Cart app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── requirements.txt
├── manage.py
└── README.md
└── LICENSE
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Virtualenv (recommended)
- PostgreSQL (optional; SQLite used by default)

---

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/phimart.git
cd phimart
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Apply migrations**

```bash
python manage.py migrate
```

**5. Create a superuser** *(optional, for admin access)*

```bash
python manage.py createsuperuser
```

---

### Environment Variables

Create a `.env` file in the project root and configure the following:

```env
SECRET_KEY=your-secret-key
DEBUG=True

# Database (leave blank to use SQLite)
DATABASE_URL=postgres://user:password@localhost:5432/phimart_db

# JWT settings (optional overrides)
ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=7
```

---

### Running the Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

---

## 📄 API Documentation

Phimart ships with interactive API documentation powered by **drf-yasg**.

| Interface | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/swagger/` |
| ReDoc | `http://127.0.0.1:8000/redoc/` |

You can explore and test all endpoints directly from the Swagger UI. For protected endpoints, click **Authorize** and enter your JWT access token as:

```
Bearer <your_access_token>
```

---

## 🔗 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/auth/users/` | Register a new user | ❌ |
| `POST` | `/auth/jwt/create/` | Obtain JWT (login) | ❌ |
| `POST` | `/auth/jwt/refresh/` | Refresh access token | ❌ |
| `POST` | `/auth/jwt/verify/` | Verify a token | ❌ |
| `GET` | `/auth/users/me/` | Get current user profile | ✅ |
| `POST` | `/auth/users/set_password/` | Change password | ✅ |

---

### Products

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/products/` | List all products | ❌ |
| `POST` | `/api/products/` | Create a product | ✅ Admin |
| `GET` | `/api/products/{id}/` | Retrieve a product | ❌ |
| `PUT` | `/api/products/{id}/` | Update a product | ✅ Admin |
| `PATCH` | `/api/products/{id}/` | Partially update a product | ✅ Admin |
| `DELETE` | `/api/products/{id}/` | Delete a product | ✅ Admin |

---

### Categories

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/categories/` | List all categories | ❌ |
| `POST` | `/api/categories/` | Create a category | ✅ Admin |
| `GET` | `/api/categories/{id}/` | Retrieve a category | ❌ |
| `PUT` | `/api/categories/{id}/` | Update a category | ✅ Admin |
| `DELETE` | `/api/categories/{id}/` | Delete a category | ✅ Admin |

---

### Cart

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/carts/` | View current user's cart | ✅ |
| `POST` | `/api/carts/` | Create a cart | ✅ |
| `GET` | `/api/carts/{id}/items/` | List items in a cart | ✅ |
| `POST` | `/api/carts/{id}/items/` | Add item to cart | ✅ |
| `PATCH` | `/api/carts/{id}/items/{item_id}/` | Update item quantity | ✅ |
| `DELETE` | `/api/carts/{id}/items/{item_id}/` | Remove item from cart | ✅ |

---

### Orders

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/orders/` | List user's orders | ✅ |
| `POST` | `/api/orders/` | Place a new order | ✅ |
| `GET` | `/api/orders/{id}/` | Retrieve order detail | ✅ |
| `PATCH` | `/api/orders/{id}/` | Update order status | ✅ Admin |
| `DELETE` | `/api/orders/{id}/` | Cancel/delete an order | ✅ Admin |

---

## 🔐 Authentication Flow

Phimart uses **JWT (JSON Web Tokens)** via Djoser + SimpleJWT.

```
1. Register       POST /auth/users/           → Create account
2. Login          POST /auth/jwt/create/      → Get access + refresh tokens
3. Access API     Header: Authorization: Bearer <access_token>
4. Token Expired  POST /auth/jwt/refresh/     → Get new access token using refresh token
```

**Example login request:**

```bash
curl -X POST http://127.0.0.1:8000/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

**Example response:**

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6..."
}
```

Use the `access` token in the `Authorization` header for all protected requests:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure your code follows PEP 8 and includes relevant tests where applicable.

---

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <b>Anayet Hasan Niloy</b><br/>
      <i>Software Engineer & Competitive Programmer</i><br/><br/>
      <a href="https://github.com/anayethasan">GitHub</a> •
      <a href="https://www.linkedin.com/in/anayet-hasan-niloy-0a25b5204/">LinkedIn</a> •
      <a href="mdneloy256@gmail.com">Email</a>
    </td>
  </tr>
</table>

> Passionate about building clean, scalable backend systems and solving algorithmic challenges. Phimart is a reflection of that — a production-ready REST API designed with best practices in mind.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ by <strong>Anayet Hasan Niloy</strong> using Django REST Framework</p>