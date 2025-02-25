#vendor and shop managment system
# Vendor and Shop Management System

A Django-based system to manage vendors, shops, and search nearby shops using JWT authentication.

## Features

- **Vendor Registration**: Register new vendors with business information.
- **JWT Authentication**: Secure login and logout with JWT tokens.
- **Shop Management**: Create, update, delete shops.
- **Nearby Shops**: Search for shops within a specified radius.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/vendor-shop-management.git
   cd vendor-shop-management
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## API Endpoints

### Authentication

1. **Register**: `POST /api/register/`
   ```json
   {
     "username": "vendor1",
     "password": "password123",
     "business_name": "My Shop"
   }
   ```

2. **Login**: `POST /api/login/`
   ```json
   {
     "username": "vendor1",
     "password": "password123"
   }
   ```

   Response:
   ```json
   {
     "access": "<access_token>",
     "refresh": "<refresh_token>"
   }
   ```

3. **Refresh Token**: `POST /api/token/refresh/`

4. **Logout**: `POST /api/logout/`

### Shop Management

1. **List/Create Shops**: `GET/POST /api/shops/`

2. **Retrieve/Update/Delete Shop**: `GET/PUT/DELETE /api/shops/<id>/`

3. **Search Nearby Shops**: `GET /api/shops/nearby/?latitude=12.97&longitude=77.59&radius=5`

## Running Tests

Run unit tests to verify the system's functionality:

```bash
python manage.py test
```

## Directory Structure

```
.
├── shop/                  # Shop app
│   ├── migrations/        # Database migrations
│   ├── models.py          # Database models
│   ├── serializers.py     # API serializers
│   ├── views.py           # API views
│   └── tests.py           # Unit tests
├── vendor_shop/           # Main project
│   ├── settings.py        # Django settings
│   └── urls.py            # Project-level URLs
└── manage.py              # Django management script
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License.

