from django.shortcuts import render

posts = [
    {
        "author": "Jawwad",
        "title": "Blog 1",
        "content": "First Post Content",
        "date_posted": "December 30, 2025"
    },
    {
        "author": "Hammad",
        "title": "Blog 2",
        "content": "Second Post Content",
        "date_posted": "December 31, 2025"
    },
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "about"})
