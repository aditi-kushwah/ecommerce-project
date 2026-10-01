# E-Commerce Backend API

A resume-ready **E-Commerce Backend API** built with Python and FastAPI. The project provides secure authentication, product management, shopping cart functionality, order processing, wishlist and review systems, address management, and an admin dashboard.

## 🚀 Features

### Authentication & Authorization

* User registration and login
* JWT-based authentication
* Password hashing with Argon2
* Protected API endpoints
* Role-based authorization
* Admin-only operations

### Product Management

* Create, update and delete products
* View product details
* Search products by name
* Filter by category
* Filter by price range
* Sort by price and name
* Pagination
* Stock management

### Shopping Cart

* Add products to cart
* Update item quantities
* Remove individual items
* Clear cart
* Stock availability validation
* User-specific carts

### Orders & Checkout

* Cart checkout
* Automatic order total calculation
* Order item creation
* Automatic stock reduction after checkout
* View personal orders
* View individual order details
* Admin order status management
* Order cancellation
* Automatic stock restoration after cancellation

### Wishlist

* Add products to wishlist
* View wishlist
* Remove products from wishlist
* Duplicate wishlist prevention

### Reviews & Ratings

* Add product reviews
* 1–5 star rating validation
* Update own reviews
* Delete own reviews
* View reviews for a product
* Prevent duplicate reviews by the same user

### Address Management

* Add delivery addresses
* View saved addresses
* View individual addresses
* Update addresses
* Delete addresses
* Phone and pincode validation
* User-specific address access

### Admin Dashboard

* Total users
* Total products
* Total orders
* Pending orders
* Confirmed orders
* Shipped orders
* Delivered orders
* Cancelled orders
* Total non-cancelled order value

## 🛠️ Technology Stack

* **Python 3.13**
* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**
* **JWT**
* **pwdlib + Argon2**
* **Uvicorn**
* **Swagger UI / OpenAPI**
* **Git & GitHub**

## 📁 Project Structure

```text
ecommerce-project/
│
├── app/
│   ├── database/
│   │   ├── database.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── wishlist.py
│   │   ├── review.py
│   │   └── address.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── wishlist.py
│   │   ├── review.py
│   │   └── address.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── products.py
│   │   ├── cart.py
│   │   ├── orders.py
│   │   ├── wishlist.py
│   │   ├── reviews.py
│   │   ├── address.py
│   │   └── admin.py
│   │
│   ├── utils/
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   └── main.py
│
├── ecommerce.db
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/aditi-kushwah/ecommerce-project.git
cd ecommerce-project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Initialize the database

```bash
python -m app.database.init_db
```

### 6. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

The project also provides an OpenAPI schema through FastAPI.

## 🔐 Authentication Flow

1. Register a user using `/auth/register`
2. Login using `/auth/login`
3. Receive a JWT access token
4. Authorize protected endpoints using the Bearer token
5. Admin users can access admin-only operations

## 🔄 Example E-Commerce Flow

```text
Register
   ↓
Login
   ↓
Browse Products
   ↓
Search / Filter / Sort
   ↓
Add Product to Cart
   ↓
Checkout
   ↓
Order Created
   ↓
Stock Reduced
   ↓
Admin Updates Order Status
   ↓
Order Delivered
```

## 🧪 Testing

The API was tested using FastAPI Swagger UI, including:

* Authentication
* JWT authorization
* Admin authorization
* Product CRUD
* Product search and filtering
* Sorting and pagination
* Cart operations
* Checkout
* Stock management
* Order cancellation and stock restoration
* Wishlist operations
* Reviews and ratings
* Address management
* Admin dashboard

## 🔒 Security

* Passwords are securely hashed using **Argon2**
* JWT tokens are used for authentication
* Protected endpoints require authentication
* Admin endpoints require admin authorization
* Users can access and modify only their own protected resources

## 🎯 Project Purpose

This project was developed as a **backend-focused portfolio project** to demonstrate practical knowledge of:

* REST API development
* FastAPI
* Python
* SQLAlchemy ORM
* Database design
* Authentication and authorization
* CRUD operations
* Business logic
* API validation
* Role-based access control
* E-commerce workflows

## 🚀 Future Improvements

Possible future enhancements include:

* Payment gateway integration
* Email notifications
* Product image upload
* Advanced analytics
* Deployment using a cloud platform
* PostgreSQL for production environments

## 👩‍💻 Author

**Aditi Kushwah**

GitHub: https://github.com/aditi-kushwah
