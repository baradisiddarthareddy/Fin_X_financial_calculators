from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'calculators/signup.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'calculators/dashboard.html')

@login_required
def home(request):
    return render(request, 'calculators/home.html')


import math
@login_required
def rd_calculator(request):
    if request.method == "GET":
        # Default values for the input sliders and output fields
        monthly_deposit = 5000
        months = 24
        interest_rate = 12.0

        # Calculate RD Maturity Amount
        total_deposit = monthly_deposit * months
        quarterly_rate = (interest_rate / 4) / 100
        total_quarters = months / 3

        # Apply RD Maturity Formula
        maturity_amount = (
            monthly_deposit
            * (pow(1 + quarterly_rate, total_quarters) - 1)
            / (1 - pow(1 + quarterly_rate, -1 / 3))
        )
        total_interest = maturity_amount - total_deposit

        # Pass data to template
        context = {
            "monthly_deposit": monthly_deposit,
            "months": months,
            "interest_rate": interest_rate,
            "total_deposit": round(total_deposit, 2),
            "total_interest": round(total_interest, 2),
            "maturity_amount": round(maturity_amount, 2),
        }
    return render(request, "calculators/rd_calculator.html", context)

@login_required
def mis_calculator(request):
    return render(request, 'calculators/mis_calculator.html')
@login_required
def gst_calculator(request):
    return render(request, 'calculators/gst_calculator.html')


@login_required
# Simple Interest Calculator View
def simple_interest_calculator(request):
    principal = 10000
    rate = 5
    time = 3
    time_unit = 'years'
    interest_earned = (principal * rate * time) / 100
    total_amount = principal + interest_earned
    summary_table = []

    if request.method == 'POST':
        try:
            principal = float(request.POST['principal'])
            rate = float(request.POST['rate'])
            time = float(request.POST['time'])
            time_unit = request.POST['time_unit']

            # Convert time to years if in months
            if time_unit == 'months':
                time = time / 12

            interest_earned = (principal * rate * time) / 100
            total_amount = principal + interest_earned

            # Generate year-by-year breakdown
            summary_table = []
            accumulated_amount = principal
            for year in range(1, int(time) + 1):
                year_interest = (principal * rate * 1) / 100
                accumulated_amount += year_interest
                summary_table.append({
                    'year': year,
                    'interest': year_interest,
                    'total_amount': accumulated_amount
                })
        except ValueError:
            interest_earned = total_amount = "Invalid input, please enter valid values."

    return render(request, 'calculators/simple_interest_calculator.html', {
        'principal': principal,
        'rate': rate,
        'time': time,
        'time_unit': time_unit,
        'interest_earned': interest_earned,
        'total_amount': total_amount,
        'summary_table': summary_table,
    })


@login_required
# Compound Interest Calculator View
def compound_interest_calculator(request):
    principal = 10000
    rate = 5
    time = 3
    time_unit = 'years'
    compounding_frequency = 1  # Annually by default

    total_amount = principal * (1 + (rate / (compounding_frequency * 100))) ** (compounding_frequency * time)
    compound_interest = total_amount - principal
    summary_table = []

    if request.method == 'POST':
        try:
            principal = float(request.POST['principal'])
            rate = float(request.POST['rate'])
            time = float(request.POST['time'])
            time_unit = request.POST['time_unit']
            compounding_frequency = int(request.POST['compounding_frequency'])

            # Convert time to years if in months
            if time_unit == 'months':
                time = time / 12

            total_amount = principal * (1 + (rate / (compounding_frequency * 100))) ** (compounding_frequency * time)
            compound_interest = total_amount - principal

            # Generate year-by-year breakdown
            summary_table = []
            accumulated_amount = principal
            for year in range(1, int(time) + 1):
                accumulated_amount = principal * (1 + (rate / (compounding_frequency * 100))) ** (compounding_frequency * year)
                year_interest = accumulated_amount - (principal * (1 + (rate / (compounding_frequency * 100))) ** (compounding_frequency * (year - 1)))
                summary_table.append({
                    'year': year,
                    'interest': year_interest,
                    'total_amount': accumulated_amount
                })
        except ValueError:
            compound_interest = total_amount = "Invalid input, please enter valid values."

    return render(request, 'calculators/compound_interest_calculator.html', {
        'principal': principal,
        'rate': rate,
        'time': time,
        'time_unit': time_unit,
        'compounding_frequency': compounding_frequency,
        'compound_interest': compound_interest,
        'total_amount': total_amount,
        'summary_table': summary_table,
    })



@login_required
def sukanya_calculator(request):
    return render(request, 'calculators/sukanya_calculator.html')



@login_required
def sip_calculator(request):
    return render(request, 'calculators/sip_calculator.html')


@login_required
def fd_calculator(request):
    return render(request, 'calculators/fd_calculator.html')


@login_required
def loan_foreclosure_calculator(request):
    return render(request, 'calculators/foreclosure_calculator.html')




