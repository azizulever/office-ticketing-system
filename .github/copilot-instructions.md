<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Office Ticketing System - Copilot Instructions

This is a Django-based office ticketing system with the following characteristics:

## Project Structure
- Django backend with simple, clean code
- HTML/CSS/JS frontend using Bootstrap 5
- SQLite database for simplicity
- Two main user roles: Employees and Administrators

## Code Style Guidelines
- Keep code simple and readable
- Use Django best practices
- Maintain consistent naming conventions
- Comment code where necessary for clarity
- Follow DRY (Don't Repeat Yourself) principles

## Key Models
- `Ticket`: Main ticket model with title, description, priority, status, employee
- `TicketFeedback`: Admin feedback on tickets

## Important Features
- Role-based access control (employees vs admins)
- Ticket priority system (low, medium, high, urgent)
- Status tracking (open, ongoing, resolved, closed)
- Admin feedback system
- Bootstrap-based responsive UI

## When making changes:
- Ensure proper authentication checks in views
- Maintain the simple, clean design aesthetic
- Test both employee and admin workflows
- Keep database queries efficient
- Follow Django security best practices
