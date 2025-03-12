from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee  # Import Employee model

# Display all employees
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
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
            return redirect('/employee/list')

# Delete employee
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
# views.py
from django.shortcuts import render

def employee_view(request):
    return render(request, 'employee/employee.html')
