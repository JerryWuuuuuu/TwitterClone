from django.shortcuts import render, redirect
from core.models import Tweet, Hashtag
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.
def splash(request):
    return render(request, "splash.html", {})

def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
					email=request.POST['email'],
					password= request.POST['password'])
        login(request, user)
        return redirect('/')
    return render(request, "signup.html", {})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home")
    return render(request, "login.html", {})

@login_required
def home_view(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "home.html", {"tweets":tweets, "user": request.user})

@login_required
def tweet(request):
    body = request.POST["body"]
    words = body.split(" ")
    new_tweet = Tweet.objects.create(body=body, author=request.user, likes = 0)
    new_tweet.save()
    for word in words: 
        if word != "" and word[0] == "#":
            if Hashtag.objects.filter(hashtag = word[1:]).exists():
                Hashtag.objects.get(hashtag = word[1:]).tweets.add(new_tweet) 
            else:
                new_hashtag = Hashtag.objects.create(hashtag = word[1:])
                new_hashtag.save()
                new_hashtag.tweets.add(new_tweet)
    return redirect('/home')

@login_required
def profile_view(request, author):
    user = User.objects.get(username = author)
    tweets = Tweet.objects.filter(author = user).order_by('-created_at')
    return render(request, "profile.html", {"tweets": tweets, "author":author, "user": user})

@login_required
def logout_action(request):
    logout(request)
    return redirect('/') 

@login_required
def hashtag_view(request, hashtag):
    hashtag = Hashtag.objects.get(hashtag = hashtag) 
    tweets = hashtag.tweets.all().order_by('-likes')
    return render(request, "hashtag.html", {"tweets":tweets, "hashtag":hashtag.hashtag})

@login_required
def hashtag_all_view(request):
    hashtags = Hashtag.objects.all().annotate(num_tweets=Count('tweets')).order_by('-num_tweets')
    return render(request, "hashtag_all.html", {"hashtags":hashtags})


@login_required
def like_tweet(request, id):
    tweet = Tweet.objects.get(id = id) 
    if request.user in tweet.liked_users.all():
        tweet.likes -= 1 
        tweet.liked_users.remove(request.user)
    else:
        tweet.likes +=1 
        tweet.liked_users.add(request.user)
    tweet.save(update_fields=["likes"])
    return redirect('/home')

@login_required
def delete_tweet(request, id):
    tweet = Tweet.objects.get(id = id)
    tweet.delete()
    return redirect('/home') 

