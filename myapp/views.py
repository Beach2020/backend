from django.shortcuts import render
from .forms import DownVoteForm
from .models import DownVote


# Create your views here.

def downvote(request):
    form = DownVoteForm(request.POST or None)
    if form.is_valid():
        # form.save()
        # form = DownVoteForm()
        url = request.POST.get('url')
        userId = url.split('/')[-1]
        postId = url.split('/')[-2]
        data = DownVote(post_id=postId, user_profile=userId)
        data.save()
        form = DownVoteForm()
  
        
    
    context = {
        'form': form
    }
    return render(request, "myapp/form_input.html", context)
