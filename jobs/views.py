from django.shortcuts import render, get_object_or_404

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    prev_element = job_detail.pk - 1
    next_element = job_detail.pk + 1

    # make sure next and prev aren't out of bounds
    if prev_element < Job.objects.all().order_by("id")[0].pk:
        prev_element = Job.objects.all().order_by("id")[0].pk
    
    if next_element > Job.objects.all().order_by("-id")[0].pk:
        next_element = Job.objects.all().order_by("-id")[0].pk

    return render(request, 'jobs/detail.html', {'job': job_detail, 
    'prev': prev_element, 'next': next_element})




from django.shortcuts import render
from django.http import FileResponse, Http404
def resume(request):
    try:
        return FileResponse(open('static/RyanACookResume1-16-21.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')




