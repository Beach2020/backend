from django.shortcuts import render
from .forms import DownVoteForm
from .models import DownVote
from django.http import HttpResponse
import json

# Create your views here.

def downvote(request):
    form = DownVoteForm(request.POST or None)
    if form.is_valid():
        url = request.POST.get('url')
        userId = url.split('/')[-1]
        postId = url.split('/')[-2]
        all_data = DownVote.objects.all()
        flag = 0
        for data in all_data:
            if data.user_profile == userId:
                if data.post_id == postId:
                    flag = 0
                    break
                else:
                    flag = 1
            else:
                flag = 1
        if flag == 1:
            new_data = DownVote(post_id=postId, user_profile=userId)
            new_data.save()
        form = DownVoteForm()
    context = {
        'form': form
    }
    return render(request, "myapp/form_input.html", context)


def downvote_ext(request):
    url = request.POST.get('url')
    userId = url.split('/')[-1]
    postId = url.split('/')[-2]
    all_data = DownVote.objects.all()
    flag = 0
    for data in all_data:
        if data.user_profile == userId:
            if data.post_id == postId:
                flag = 0
                break
            else:
                flag = 1
        else:
            flag = 1
    if flag == 1:
        new_data = DownVote(post_id=postId, user_profile=userId)
        new_data.save()
    vote_list = []
    all_data = DownVote.objects.all()
    for data in all_data:
        if data.post_id == postId:
            vote_list.append(data)
    return HttpResponse(
        json.dumps({'total_downvote': len(vote_list), 'msg': 'Update Success.'}),
        content_type="application/json"
    )