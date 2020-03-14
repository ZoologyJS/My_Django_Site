from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Chris Fradella',
        'title' : 'A day in the park',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce commodo mattis lacus nec efficitur. Nullam ante dui, sodales quis leo a, iaculis tincidunt orci. Sed lorem lectus, tempus a luctus ac, fermentum tristique ligula. Morbi lorem nulla, lacinia sed nisi at, luctus lacinia quam. Aenean rhoncus scelerisque ante, ac convallis leo sagittis id. Vivamus elementum, sem sed malesuada pellentesque, augue libero ornare libero, id ultricies tellus velit eu nisi. Duis gravida quam ligula, quis iaculis nunc iaculis a. In in accumsan justo. ',
        'date_posted' : 'March 09, 2020'
    },
    {
        'author' : 'Chris Fradella',
        'title' : 'Coding for fun',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce commodo mattis lacus nec efficitur. Nullam ante dui, sodales quis leo a, iaculis tincidunt orci. Sed lorem lectus, tempus a luctus ac, fermentum tristique ligula. Morbi lorem nulla, lacinia sed nisi at, luctus lacinia quam. Aenean rhoncus scelerisque ante, ac convallis leo sagittis id. Vivamus elementum, sem sed malesuada pellentesque, augue libero ornare libero, id ultricies tellus velit eu nisi. Duis gravida quam ligula, quis iaculis nunc iaculis a. In in accumsan justo. ',
        'date_posted' : 'March 10, 2020'
    },
    {
        'author' : 'Chris Fradella',
        'title' : 'When to take a nap',
        'content' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce commodo mattis lacus nec efficitur. Nullam ante dui, sodales quis leo a, iaculis tincidunt orci. Sed lorem lectus, tempus a luctus ac, fermentum tristique ligula. Morbi lorem nulla, lacinia sed nisi at, luctus lacinia quam. Aenean rhoncus scelerisque ante, ac convallis leo sagittis id. Vivamus elementum, sem sed malesuada pellentesque, augue libero ornare libero, id ultricies tellus velit eu nisi. Duis gravida quam ligula, quis iaculis nunc iaculis a. In in accumsan justo. ',
        'date_posted' : 'March 11, 2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, "home/home.html", context)

def about(request):
    return render(request, "home/about.html")
