from django.shortcuts import render, redirect
from .models import Post, Category, Comment, Profile
from django.db.models import Q
from .forms import CommentForm
from datetime import datetime
from .forms import SearchForm
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MyUserCreationForm, PostForm, ProfileForm
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import get_user_model




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exit")


        user = authenticate(request, username=username, password = password)

        if user is not None:
                login(request, user)
                return redirect('home')
            
    context = {}
    return render(request, 'login_page.html', context)






def logout_user(request):
    logout(request)
    return redirect('home')



def registerPage(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = MyUserCreationForm()
    return render(request, 'register_page.html', {'form': form})





def post_search(request):
    query = request.GET.get('query', '')  # Get the search term from the URL query parameters
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)  # Use Q for OR condition
        )

    return render(request, 'search_page.html', {'posts': posts, 'query': query})


def home(request):


    posts = Post.objects.all()
    
    categories = Category.objects.all()
    all_news = Post.objects.all()
    featured_news = Post.objects.filter(category__name='Featured News')
    main_news = Post.objects.filter(category__name='Main News')[0:1]
    latest_news = Post.objects.filter(category__name='Latest News')[0:5]
    advertisement_news = Post.objects.filter(category__name='Advertisement News')[0:1]
    trending_news = Post.objects.filter(category__name='Trending News')[0:1]
    breaking_news = Post.objects.filter(category__name='Breaking News')[0:1]
    popular_news = Post.objects.filter(category__name='Popular News')[0:5]
    current_date = datetime.now()

    
    return render(request, 'home.html', {'posts': posts, 'featured_news': featured_news, 'main_news': main_news, 'latest_news': latest_news, 'advertisement_news': advertisement_news, 'trending_news': trending_news, 'categories': categories, 'breaking_news': breaking_news, 'popular_news': popular_news, 'all_news': all_news, 'current_date': current_date})




def profile_page(request, pk):
    # Get the user and profile instance
    user = get_user_model().objects.get(pk=pk)
    
    # Get the total views for all posts by the user
    total_views = Post.objects.filter(profile__user=user).aggregate(Sum('view_count'))['view_count__sum'] or 0
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_page', pk=pk)
    
    return render(request, 'profile.html', {'user': user, 'total_views': total_views})



def update_profile(request, pk):
    user = get_user_model().objects.get(id=pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to the profile page after updating
            return redirect('profile-page', pk=user.pk)
    else:
        # Pre-populate the form with existing user data
        form = ProfileForm(instance=user)

    return render(request, 'update_profile.html', {'form': form, 'user': user})

def view_profile(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    return render(request, 'profile.html', {'user': user})




def articlePage(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()  # Fetch all comments related to this post
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # Don't commit to DB yet
            comment.post = post  # Associate comment with the correct post
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()  # Save the comment to DB
            return redirect('article', pk=pk)
        else:
            # If the user is not logged in, redirect to the login page
            return redirect('login')

    # Check if the user has already viewed this post in the session
    if not request.session.get(f'viewed_post_{post.id}', False):
        # Increment the view count for the post
        post.view_count += 1
        post.save()
        # Mark this post as viewed in the session
        request.session[f'viewed_post_{post.id}'] = True

    # Fetch other related posts (for trending, advertisements, categories)
    trending_news = Post.objects.filter(category__name='Trending News')[:1]
    advertisement_news = Post.objects.filter(category__name='Advertisement News')[:1]
    categories = Category.objects.all()
    current_date = datetime.now()

    # Pass everything to the template
    return render(request, 'article.html', {
        'article': post,
        'categories': categories,
        'trending_news': trending_news,
        'advertisement_news': advertisement_news,
        'comments': comments,
        'comment_form': comment_form,
        'current_date': current_date,
    })


def create_Post(request, pk=None):
    # Check if the user belongs to the 'Poster' group
    if not request.user.groups.filter(name='Poster').exists():
        return redirect('home')  # Redirect if the user is not in the 'Poster' group

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new post instance but don't save it yet
            post = form.save(commit=False)

            # Get or create the Profile instance linked to the current user
            profile_instance, _ = Profile.objects.get_or_create(user=request.user)

            # Assign the profile instance to the post
            post.profile = profile_instance  # ForeignKey assignment works here
            
            # Save the post first to generate its ID
            post.save()  # Save first to generate the primary key
            
            # Handle the categories (ManyToManyField)
            categories = form.cleaned_data.get('category')
            post.category.set(categories)  # Assign selected categories

            # Save the post again after the categories are set
            post.save()  # Final save to persist the category relationships

            # Redirect to the home page or newly created post detail page
            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})



def all_news(request):


    categories_not_to_display = ['Advertisement News'] 

    # Filter posts by category
    all_news = Post.objects.all().exclude(category__name__in=categories_not_to_display)

    
    # Filter posts for the "Advertisement News" category
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'all_news.html', {'all_news': all_news, 'advertisement_news': advertisement_news, 'current_date': current_date})


def main_news(request):
    main_news = Post.objects.filter(category__name='Main News')
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'main_news.html', {'main_news': main_news, 'advertisement_news': advertisement_news, 'current_date': current_date})

def featured_news(request):
    featured_news = Post.objects.filter(category__name='Featured News')
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'featured_news.html', {'featured_news': featured_news, 'advertisement_news': advertisement_news, 'current_date': current_date})

def breaking_news(request):
    breaking_news = Post.objects.filter(category__name='Breaking News')
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'breaking_news.html', {'breaking_news': breaking_news, 'advertisement_news': advertisement_news, 'current_date': current_date})

def latest_news(request):
    latest_news = Post.objects.filter(category__name='Latest News')
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'latest_news.html', {'latest_news': latest_news, 'advertisement_news': advertisement_news, 'current_date': current_date})

def trending_news(request):
    trending_news = Post.objects.filter(category__name='Trending News')
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'trending_news.html', {'trending_news': trending_news, 'advertisement_news': advertisement_news, 'current_date': current_date})

def popular_news(request):
    popular_news = Post.objects.filter(category__name='Popular News')
    advertisement_news = Post.objects.filter(category__name='Advertisement News')
    current_date = datetime.now()
    
    return render(request, 'popular_news.html', {'popular_news': popular_news, 'advertisement_news': advertisement_news, 'current_date': current_date})