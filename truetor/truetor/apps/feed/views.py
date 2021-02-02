from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Tweet

from django.contrib.auth.models import User

@login_required
def feed(request):
    user_ids = [request.user.id]

    for user in request.user.userprofile.follows.all():
        user_ids.append(user.user.id)

    tweets = Tweet.objects.filter(created_by_id__in=user_ids)

    for tweet in tweets:
        likes = tweet.likes.filter(created_by_id=request.user.id)

        if likes.count() > 0:
            tweet.liked = True
        else:
            tweet.liked = False

    return render(request, 'feed/feed.html', { 'tweets': tweets })


@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        users = User.objects.filter(username__icontains=query)
    else:
        users = []

    context = {
        'query': query,
        'users': users
    }

    return render(request, 'feed/search.html', context)
