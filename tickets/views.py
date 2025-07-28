from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Ticket, TicketFeedback
from .forms import TicketForm, TicketFeedbackForm


def is_admin(user):
    return user.is_staff or user.is_superuser


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if is_admin(user):
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def employee_dashboard(request):
    if is_admin(request.user):
        return redirect('admin_dashboard')
    
    tickets = Ticket.objects.filter(employee=request.user)
    
    # Calculate statistics
    stats = {
        'total': tickets.count(),
        'open': tickets.filter(status='open').count(),
        'ongoing': tickets.filter(status='ongoing').count(),
        'resolved': tickets.filter(status='resolved').count(),
        'closed': tickets.filter(status='closed').count(),
    }
    
    return render(request, 'employee_dashboard.html', {
        'tickets': tickets,
        'stats': stats
    })


@login_required
def create_ticket(request):
    if is_admin(request.user):
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.employee = request.user
            ticket.save()
            messages.success(request, 'Ticket created successfully!')
            return redirect('employee_dashboard')
    else:
        form = TicketForm()
    
    return render(request, 'create_ticket.html', {'form': form})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    # Check if user can view this ticket
    if not is_admin(request.user) and ticket.employee != request.user:
        messages.error(request, 'You can only view your own tickets.')
        return redirect('employee_dashboard')
    
    feedback_list = ticket.feedback.all()
    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        'feedback_list': feedback_list
    })


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    tickets = Ticket.objects.all().select_related('employee')
    
    # Calculate statistics
    stats = {
        'total': tickets.count(),
        'open': tickets.filter(status='open').count(),
        'ongoing': tickets.filter(status='ongoing').count(),
        'resolved': tickets.filter(status='resolved').count(),
        'closed': tickets.filter(status='closed').count(),
    }
    
    return render(request, 'admin_dashboard.html', {
        'tickets': tickets,
        'stats': stats
    })


@login_required
@user_passes_test(is_admin)
def admin_ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    if request.method == 'POST':
        if 'feedback' in request.POST:
            form = TicketFeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.ticket = ticket
                feedback.admin_user = request.user
                feedback.save()
                messages.success(request, 'Feedback added successfully!')
                return redirect('admin_ticket_detail', ticket_id=ticket.id)
        
        elif 'status' in request.POST:
            new_status = request.POST.get('status')
            if new_status in ['open', 'ongoing', 'resolved', 'closed']:
                old_status = ticket.status
                ticket.status = new_status
                ticket.save()
                
                # Add automatic feedback when status changes to resolved
                if new_status == 'resolved' and old_status != 'resolved':
                    TicketFeedback.objects.create(
                        ticket=ticket,
                        admin_user=request.user,
                        message=f"This ticket has been marked as resolved. The issue should now be fixed. If you continue to experience problems, please create a new ticket."
                    )
                    messages.success(request, 'Ticket marked as resolved! An automatic feedback message has been sent to the employee.')
                else:
                    messages.success(request, f'Ticket status updated to {new_status}!')
                
                return redirect('admin_ticket_detail', ticket_id=ticket.id)
    
    form = TicketFeedbackForm()
    feedback_list = ticket.feedback.all()
    
    return render(request, 'admin_ticket_detail.html', {
        'ticket': ticket,
        'form': form,
        'feedback_list': feedback_list
    })
