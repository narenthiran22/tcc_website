from django.shortcuts import render
from .models import Player, Match, News

def home(request):
    latest_matches = Match.objects.order_by('-date')[:3]
    latest_news = News.objects.order_by('-published_date')[:5]
    return render(request, 'cricket/home.html', {
        'latest_matches': latest_matches,
        'latest_news': latest_news,
    })

def players(request):
    players_list = Player.objects.all()
    return render(request, 'cricket/players.html', {
        'players': players_list,
    })

def matches(request):
    matches_list = Match.objects.order_by('-date')
    return render(request, 'cricket/matches.html', {
        'matches': matches_list,
    })

def news(request):
    news_list = News.objects.order_by('-published_date')
    return render(request, 'cricket/news.html', {
        'news': news_list,
    })
