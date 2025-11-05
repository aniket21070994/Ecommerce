# E-Commerce REST API with Role-Based Access (Django REST Framework)

## Overview

This document defines the complete database schema and API structure for an E-Commerce backend built using Django REST Framework (DRF) with role-based access control. The project supports three user roles: **Super Admin**, **Admin**, and **User**.

The system includes features like product and category management, cart, orders, discounts, coupons, and product reviews.

## User Roles

| Role        | Description              | Permissions                                                                                             |
|-------------|--------------------------|---------------------------------------------------------------------------------------------------------|
| **Super Admin** | Top-level administrator  | Can manage Admins, Users, Categories, Products, Orders, and Discounts.                                  |
| **Admin**     | Product and order manager| Can manage Categories, Products, Orders, and Discounts.                                                 |
| **User**      | Customer                 | Can browse products, manage cart, place orders, and post reviews.                                       |

## Workflow

The application follows a standard e-commerce workflow:

1.  **Authentication**:
    *   Users register for an account.
    *   Users log in to obtain a JWT token for authenticating subsequent requests.
    *   Authenticated users can log out.

2.  **Product Discovery**:
    *   All users (authenticated or not) can browse and view products and categories.
    *   The API supports filtering and pagination for product listings.

3.  **Cart Management**:
    *   Authenticated users can add items to their shopping cart.
    *   They can view, update quantities, and remove items from their cart.

4.  **Ordering**:
    *   Users create an order from their cart.
    *   Discount coupons can be applied during checkout.
    *   Admins/Super Admins manage orders by updating their status (e.g., "pending" to "shipped") and approving them.

5.  **Store Management (Admin/Super Admin)**:
    *   Manage product categories, brands, products, and product variants.
    *   Manage discounts and coupons.

6.  **User Feedback and Notifications**:
    *   Users can write reviews for products.
    *   The system sends notifications for events like order updates.

## API Endpoints

### 1. Authentication and User Management

| Endpoint                  | Method      | Role          | Description               |
|---------------------------|-------------|---------------|---------------------------|
| `/auth/register/`         | `POST`      | Public        | Register new user         |
| `/auth/login/`            | `POST`      | Public        | Obtain JWT token          |
| `/auth/logout/`           | `POST`      | Authenticated | Logout user               |
| `/auth/profile/`          | `GET`/`PUT` | User/Admin    | View or update profile    |
| `/auth/users/`            | `GET`       | Super Admin   | List all users            |
| `/auth/create-admin/`     | `POST`      | Super Admin   | Create new Admin          |

### 2. Category and Brand Management

| Endpoint                  | Method          | Role                | Description                  |
|---------------------------|-----------------|---------------------|------------------------------|
| `/categories/`            | `GET`           | All                 | List categories              |
| `/categories/`            | `POST`          | Admin/Super Admin   | Create category              |
| `/categories/{id}/`       | `PUT`/`DELETE`  | Admin/Super Admin   | Update or delete category    |
| `/brands/`                | `GET`           | All                 | List brands                  |
| `/brands/`                | `POST`          | Admin/Super Admin   | Create brand                 |

### 3. Product Management

| Endpoint                      | Method          | Role                | Description                 |
|-------------------------------|-----------------|---------------------|-----------------------------|
| `/products/`                  | `GET`           | All                 | List products with filters  |
| `/products/`                  | `POST`          | Admin/Super Admin   | Create product              |
| `/products/{id}/`             | `GET`           | All                 | View product details        |
| `/products/{id}/`             | `PUT`/`DELETE`  | Admin/Super Admin   | Update or delete product    |
| `/products/{id}/variants/`    | `POST`          | Admin/Super Admin   | Add product variants        |
| `/products/{id}/images/`      | `POST`          | Admin/Super Admin   | Upload product images       |

### 4. Cart Management

| Endpoint                      | Method   | Role | Description           |
|-------------------------------|----------|------|-----------------------|
| `/cart/`                      | `GET`    | User | Retrieve cart items   |
| `/cart/add/`                  | `POST`   | User | Add item to cart      |
| `/cart/update/{item_id}/`     | `PUT`    | User | Update quantity       |
| `/cart/remove/{item_id}/`     | `DELETE` | User | Remove item           |

### 5. Orders

| Endpoint                         | Method   | Role                  | Description                 |
|----------------------------------|----------|-----------------------|-----------------------------|
| `/orders/create/`                | `POST`   | User                  | Create order from cart      |
| `/orders/`                       | `GET`    | User/Admin/Super Admin| List orders (Admin sees all)|
| `/orders/{id}/`                  | `GET`    | User/Admin/Super Admin| Get order details           |
| `/orders/{id}/update-status/`    | `PUT`    | Admin/Super Admin     | Update order status         |
| `/orders/{id}/approve/`          | `POST`   | Admin/Super Admin     | Approve order               |

### 6. Discounts and Coupons

| Endpoint                       | Method   | Role                | Description               |
|--------------------------------|----------|---------------------|---------------------------|
| `/discounts/`                  | `POST`   | Admin/Super Admin   | Create discount           |
| `/discounts/`                  | `GET`    | All                 | View active discounts     |
| `/coupons/`                    | `POST`   | Admin/Super Admin   | Create coupon             |
| `/coupons/{code}/validate/`    | `GET`    | User                | Validate coupon code      |

### 7. Reviews

| Endpoint                      | Method   | Role                | Description           |
|-------------------------------|----------|---------------------|-----------------------|
| `/products/{id}/reviews/`     | `GET`    | All                 | List product reviews  |
| `/products/{id}/reviews/`     | `POST`   | User                | Create review         |
| `/reviews/{id}/`              | `DELETE` | Admin/Super Admin   | Delete review         |

### 8. Notifications

| Endpoint                         | Method   | Role          | Description                  |
|----------------------------------|----------|---------------|------------------------------|
| `/notifications/`                | `GET`    | User/Admin    | Fetch notifications          |
| `/notifications/{id}/mark-read/` | `POST`   | User/Admin    | Mark as read                 |
| `/notifications/send/`           | `POST`   | Super Admin   | Send notification manually   |

## Technical Requirements

*   **Authentication**: JWT-based authentication (`djangorestframework-simplejwt`).
*   **Role-Based Access Control**: Custom DRF permission classes (`IsSuperAdmin`, `IsAdminOrSuperAdmin`, `IsUserOnly`).
*   **Custom UserProfile Model**: The `role` field is stored in `UserProfile`, not in the `auth_user` table.
*   **Nested Serializers**: For `Product` -> `Variant` -> `Images`.
*   **Signals**:
    *   Reduce stock after order confirmation.
    *   Send notifications on order updates.
*   **Filtering and Pagination**: For product listings.
*   **Logging Middleware**: To log API hits with user details and role information.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```