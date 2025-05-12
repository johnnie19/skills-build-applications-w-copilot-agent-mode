from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    pass

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    pass
