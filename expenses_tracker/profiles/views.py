from django.shortcuts import render, redirect

from expenses_tracker.profiles.forms import ProfileForm, ExpenseForm, DeleteExpenseForm
from expenses_tracker.profiles.models import Profile, Expense


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = Expense.objects.all()
    budget = profile.budget
    budget_left = budget - sum(e.price for e in expenses)
    context = {
        'expenses': expenses,
        'budget': budget,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context=context)


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context=context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-edit.html', context=context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-delete.html', context=context)


def profile_info(request):
    profile = get_profile()
    budget = profile.budget
    expenses = Expense.objects.all()
    budget_left = budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile info')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-edit.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home')
    context = {
        'profile': profile,
    }
    return render(request, 'profile-delete.html', context=context)
