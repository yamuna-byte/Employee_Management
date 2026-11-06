
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


# Dashboard
def home(request):

    employees = Employee.objects.all()

    # Search employees
    search = request.GET.get('search')

    if search:
        employees = employees.filter(name__icontains=search)

    # Department filter
    department = request.GET.get('department')

    if department:
        employees = employees.filter(department=department)

    # Get department names
    departments = Employee.objects.values_list(
        'department', flat=True
    ).distinct()

    context = {
        'employees': employees,
        'total_employees': Employee.objects.count(),
        'total_departments': departments.count(),
        'departments': departments,
    }

    return render(request, 'employee/home.html', context)


# Add Employee
def add_employee(request):

    if request.method == 'POST':

        Employee.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            position=request.POST.get('position'),
            department=request.POST.get('department'),
            date_joined=request.POST.get('date_joined')
        )

        return redirect('home')

    return render(request, 'employee/add_employee.html')


# Edit Employee
def edit_employee(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':

        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')
        employee.department = request.POST.get('department')
        employee.date_joined = request.POST.get('date_joined')

        employee.save()

        return redirect('home')

    return render(
        request,
        'employee/edit_employee.html',
        {'employee': employee}
    )


# Delete Employee
def delete_employee(request, id):

    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()

    return redirect('home')
