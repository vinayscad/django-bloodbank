from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import BloodDonor

def donor_list(request):
    donors = BloodDonor.objects.all()
    return render(request, 'donors.html', {'donors': donors})


# CREATE
def add_donor(request):
    if request.method == 'POST':
        BloodDonor.objects.create(
            name=request.POST.get('name'),
            blood_group=request.POST.get('blood_group'),
            age=request.POST.get('age'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
        )
        return redirect('donor_list')

    return render(request, 'add_donor.html')


# UPDATE
def edit_donor(request, donor_id):
    donor = get_object_or_404(BloodDonor, id=donor_id)

    if request.method == 'POST':
        donor.name = request.POST.get('name')
        donor.blood_group = request.POST.get('blood_group')
        donor.age = request.POST.get('age')
        donor.phone = request.POST.get('phone')
        donor.city = request.POST.get('city')
        donor.save()

        return redirect('donor_list')

    return render(request, 'edit_donor.html', {'donor': donor})


# DELETE
def delete_donor(request, donor_id):
    donor = get_object_or_404(BloodDonor, id=donor_id)
    donor.delete()
    return redirect('donor_list')