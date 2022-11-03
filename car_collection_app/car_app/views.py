from django.shortcuts import render, redirect

# Create your views here.
from car_collection_app.car_app.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from car_collection_app.car_app.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'index.html', context)


def catalogue(request):
    profile = get_profile()
    if profile is None:
        return render('index.html')

    context = {'cars': Car.objects.all(), 'profile': profile}
    return render(request, 'catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form}
    return render(request, 'profile-create.html', context)


def profile_details(request):
    total_price = sum([car.price for car in Car.objects.all()])
    profile = get_profile()
    context = {'profile': profile, 'total_price': total_price}
    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {'form': form, 'profile': profile}
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'profile': profile}
    return render(request, 'profile-delete.html', context)


def car_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form, 'profile': profile}
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()
    context = {'car': car, 'profile': profile}
    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form':form, 'profile': profile, 'car': car}
    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {'form': form, 'profile': profile, 'car':car}
    return render(request, 'car-delete.html', context)
