from django.db import models
from django.utils import timezone

class Player(models.Model):
    PLAYER_ROLES = [
        ('BAT', 'Batsman'),
        ('BWL', 'Bowler'),
        ('AR', 'All-Rounder'),
        ('WK', 'Wicket Keeper'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=3, choices=PLAYER_ROLES)
    jersey_number = models.IntegerField()
    image = models.ImageField(upload_to='players/', null=True, blank=True)
    matches_played = models.IntegerField(default=0)
    runs_scored = models.IntegerField(default=0)
    wickets_taken = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Match(models.Model):
    MATCH_TYPES = [
        ('T20', 'Twenty20'),
        ('ODI', 'One Day'),
        ('TEST', 'Test Match'),
    ]
    
    match_type = models.CharField(max_length=4, choices=MATCH_TYPES)
    opponent = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    result = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.opponent} - {self.date.strftime('%d %b %Y')}"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
