from django.shortcuts import render

tasks = ["fap", "wank", "jizz"]
# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "tasks" : tasks
    })