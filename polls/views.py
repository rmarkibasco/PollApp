from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from polls.models import Poll
# from django.template import RequestContext, loader

# first part (page 3)
# def index(request):
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
# 	output = ', '.join([p.question for p in latest_poll_list])
# 	return HttpResponse(output)
	# return HttpResponse("Hello, world. You're at the poll index.")

# second part (page 3)
# def index(request):
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = RequestContext(request, {
# 		'latest_poll_list': latest_poll_list
# 	})

# 	return HttpResponse(template.render(context))

# third part (page 3)
def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

# first part (page 3)
# def detail(request, poll_id):
# 	return HttpResponse("You're looking at poll %s." % poll_id)

# second part (page 3)
# def detail(request, poll_id):
# 	try:
# 		poll = Poll.objects.get(pk=poll_id) 
# 		pass
# 	except Poll.DoesNotExist:
# 		raise Http404

# 	return render(request, 'polls/detail.html', {'poll' : poll})

# third part (page 3)
def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll' : poll})


def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)