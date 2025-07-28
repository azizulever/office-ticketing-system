from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tickets.models import Ticket, TicketFeedback


class Command(BaseCommand):
    help = 'Create sample data for the ticketing system'

    def handle(self, *args, **options):
        # Set admin password
        try:
            admin = User.objects.get(username='admin')
            admin.set_password('admin123')
            admin.is_staff = True
            admin.is_superuser = True
            admin.save()
            self.stdout.write(self.style.SUCCESS('Admin password set to: admin123'))
        except User.DoesNotExist:
            admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user with password: admin123'))

        # Create sample employees
        employees = [
            {'username': 'john_doe', 'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'},
            {'username': 'jane_smith', 'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com'},
            {'username': 'bob_wilson', 'first_name': 'Bob', 'last_name': 'Wilson', 'email': 'bob@example.com'},
        ]

        created_employees = []
        for emp_data in employees:
            user, created = User.objects.get_or_create(
                username=emp_data['username'],
                defaults={
                    'first_name': emp_data['first_name'],
                    'last_name': emp_data['last_name'],
                    'email': emp_data['email'],
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created employee: {user.username} (password: password123)')
            created_employees.append(user)

        # Create sample tickets
        sample_tickets = [
            {
                'title': 'Printer not working in Office 101',
                'description': 'The printer in office 101 is not responding. It shows an error message when trying to print documents.',
                'priority': 'high',
                'employee': created_employees[0],
            },
            {
                'title': 'Computer running very slow',
                'description': 'My computer has been running extremely slow for the past few days. It takes forever to open applications.',
                'priority': 'medium',
                'employee': created_employees[1],
            },
            {
                'title': 'Email not syncing',
                'description': 'My email is not syncing properly. I\'m not receiving new emails and sent emails are not showing up.',
                'priority': 'urgent',
                'employee': created_employees[2],
            },
            {
                'title': 'Keyboard keys sticking',
                'description': 'Several keys on my keyboard are sticking and not registering properly when pressed.',
                'priority': 'low',
                'employee': created_employees[0],
            },
        ]

        for ticket_data in sample_tickets:
            ticket, created = Ticket.objects.get_or_create(
                title=ticket_data['title'],
                defaults=ticket_data
            )
            if created:
                self.stdout.write(f'Created ticket: {ticket.title}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write(self.style.SUCCESS('Login credentials:'))
        self.stdout.write(self.style.SUCCESS('Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('Employees: john_doe, jane_smith, bob_wilson / password123'))
