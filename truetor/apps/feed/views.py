from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Tweet

@login_required
def feed(request):
    user_ids = [request.user.id]

    for user in request.user.userprofile.follows.all():
        user_ids.append(user.user.id)

    tweets = Tweet.objects.filter(created_by_id__in=user_ids)

    return render(request, 'feed/feed.html', { 'oinks': tweets })


@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        tweets = User.objects.filter(username__icontains=query)
    else:
        tweets = []

    context = {
        'query': query,
        'tweets': tweets
    }

    return render(request, 'feed/search.html', context)
