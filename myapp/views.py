from .models import DownVote
from django.http import HttpResponse
from json import dumps


def d(request, pid, uid):
    try:
        adownvote = DownVote.objects.get(post_id=pid, user_profile=uid)
        adownvote.delete()
    except DownVote.DoesNotExist:
        new_dv = DownVote(post_id=pid, user_profile=uid)
        new_dv.save()

    all_data = DownVote.objects.filter(post_id=pid)

    return HttpResponse(
        dumps({'total_downvote': len(all_data)}),
        content_type="application/json"
    )

def s(request, pid, uid):
    try:
        adownvote = DownVote.objects.get(post_id=pid, user_profile=uid)
        this_user_downvoted = "yes"
    except DownVote.DoesNotExist:
        this_user_downvoted = "no"

    all_data = DownVote.objects.filter(post_id=pid)

    return HttpResponse(
        dumps({'total_downvote': len(all_data), 'thisuser': this_user_downvoted}),
        content_type="application/json"
    )