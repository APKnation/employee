from django.shortcuts import render, redirect
from django.urls import reverse  # Don't forget to import reverse
from .forms import EmployeeForm
from .models import Employee  # Import Employee model

# Display all employees
def employee_list(request):
    context =   Employee.objects.all()
    return render(request, "register/employee_list.html", context)

# Create or update employee form
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # If no ID, create a new form
            form = EmployeeForm()
        else:  # If ID exists, load employee details
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "register/employee_form.html", {'form': form})  # Fixed render function

    else:  # POST request - form submission
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)  # Fixed syntax error

        if form.is_valid():
            form.save()
        return redirect(reverse('employee_list'))

# Delete employee
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect(reverse('employee_list'))

# Optionally, delete the commented-out employee_view function if you're not using it
# def employee_view(request):
#     return render(request, 'employee/employee_list.html')
