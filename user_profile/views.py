from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from account.models import CustomUser
from products.models import Product
from .models import Profile
from django.conf import settings
import redis

r = redis.Redis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    db = settings.REDIS_DB,
)

def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile = Profile.objects.get(user=user)
    products = Product.objects.filter(user=user)
    product_count = products.count()

    #total_views = r.incr(f'{user.id}')


    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    return render(
        request,
        'profile.html',
        {
            'products': products,
            'profile': profile,
            'product_count': product_count,
            #'total_views': total_views
        }
    )

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_edit = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_edit.is_valid():
            user_form.save()
            profile_edit.save()

            return redirect('user_profile:profile', username=profile.user.username)

    else:
        user_form = UserEditForm(instance=request.user)
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_edit = ProfileEditForm(instance=profile)
    
    return render(
        request,
        'edit_profile.html',
        {
            'user_form': user_form,
            'profile_edit': profile_edit
        }
    )