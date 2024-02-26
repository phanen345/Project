from django.shortcuts import render,redirect, get_object_or_404
from .models import Profile
from .forms import ProfileForm,ComplaintForm

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')  # Redirect to a view that lists all complaints
    else:
        form = ProfileForm()

    return render(request, 'profile_create.html', {'form': form})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def complaint(request):
      if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
        else:
            return render(request, 'complaint.html', {'form': form})


def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')
    return render(request, 'profile_delete.html', {'profile': profile})
def all_table(request):
    return render(request, 'index.html')

# def update_profile(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
    
    
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_list')
#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'profile_update.html', {'form': form, 'profile': profile})
   


