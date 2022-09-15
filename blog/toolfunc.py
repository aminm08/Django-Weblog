from django.contrib.auth import get_user_model

def best_users():
    best = {}
    for user in get_user_model().objects.all():
        best[user.username] = len(user.blogs.all())
    best = sorted(best.values())
    print(best)
