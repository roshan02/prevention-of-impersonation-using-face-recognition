from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import Day, Todo
from .forms import TaskForm
from django.template import RequestContext
# Create your views here.
def index(request, day):
    wday = get_object_or_404(Day, name = day)
    adays = Day.objects.all()
    tasks = Todo.objects.all()
    context = {
        "wday" : wday,
        "adays" : adays,
        "tasks" : tasks,
    }
    return render(request, 'timetable/index.html', context)

def create_task(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = TaskForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request , "Monday")
        else:
            # The supplied form contained errors - just print them to the terminal.
            print( form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = TaskForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('timetable/create_task.html', {'form': form}, context)
