# Office Ticketing System

A simple Django-based office ticketing system that allows employees to create support tickets and administrators to manage them.

## Features

### Employee Panel
- Create new tickets with title, description, and priority
- View all personal tickets and their status
- See feedback from administrators
- Simple and clean interface

### Admin Panel
- View all tickets from all employees
- Update ticket status (Open, Ongoing, Resolved, Closed)
- Send feedback messages to employees
- Manage tickets efficiently

## Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Database**: SQLite (default Django database)
- **Authentication**: Django built-in authentication

## Installation & Setup

1. **Clone or navigate to the project directory**
   ```
   cd "Office Ticketing System"
   ```

2. **Activate the virtual environment** (already configured)
   ```
   .venv\Scripts\activate
   ```

3. **Install dependencies** (already installed)
   ```
   pip install django pillow
   ```

4. **Run migrations** (already done)
   ```
   python manage.py migrate
   ```

5. **Create sample data** (already created)
   ```
   python manage.py setup_sample_data
   ```

6. **Start the development server**
   ```
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to: http://127.0.0.1:8000/

## Login Credentials

### Administrator
- **Username**: admin
- **Password**: admin123
- **Access**: Full admin panel with ticket management capabilities

### Sample Employees
- **Username**: john_doe, jane_smith, bob_wilson
- **Password**: password123 (for all employees)
- **Access**: Employee panel for creating and viewing personal tickets

## Usage

### For Employees
1. Login with employee credentials
2. View your dashboard showing all your tickets
3. Click "Create New Ticket" to submit a new support request
4. Fill in the title, description, and select priority level
5. View ticket details and admin feedback by clicking "View" on any ticket

### For Administrators
1. Login with admin credentials
2. View all tickets from all employees in the admin dashboard
3. Click "Manage" on any ticket to:
   - Update the ticket status
   - Send feedback messages to the employee
   - View complete ticket history

## Project Structure

```
Office Ticketing System/
├── manage.py
├── db.sqlite3
├── ticketing_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tickets/
│   ├── __init__.py
│   ├── models.py          # Ticket and TicketFeedback models
│   ├── views.py           # All view functions
│   ├── forms.py           # Django forms
│   ├── urls.py            # URL patterns
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # App configuration
│   ├── migrations/        # Database migrations
│   └── management/        # Custom management commands
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── employee_dashboard.html
│   ├── admin_dashboard.html
│   ├── create_ticket.html
│   ├── ticket_detail.html
│   └── admin_ticket_detail.html
└── static/               # Static files (CSS, JS, images)
```

## Key Features Implemented

1. **User Authentication**: Separate login system with role-based access
2. **Ticket Management**: CRUD operations for tickets
3. **Priority System**: Low, Medium, High, Urgent priority levels
4. **Status Tracking**: Open, Ongoing, Resolved, Closed statuses
5. **Feedback System**: Admin-to-employee communication
6. **Responsive Design**: Mobile-friendly Bootstrap interface
7. **Security**: CSRF protection, proper authentication checks

## Development Notes

- The code is intentionally kept simple and readable
- Bootstrap 5 is used for styling to maintain a clean, professional look
- SQLite database for easy setup and development
- Django's built-in admin interface is available at `/admin/`
- All templates use Bootstrap components for consistency

## Future Enhancements

- Email notifications for ticket updates
- File attachment support
- Advanced filtering and search
- Ticket assignment to specific administrators
- Dashboard analytics and reports
