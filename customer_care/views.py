from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})


def metrics(request):
    return render(request, "metrics.html", {})


def reports(request):
    return render(request, "reports.html", {})


def notifications(request):
    return render(request, "notifications.html", {})


def chats(request):
    return render(request, "chats.html", {})


