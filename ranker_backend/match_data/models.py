from django.db import models


class Player(models.Model):
	name = models.CharField(max_length=200)
	steam_id = models.CharField(max_length=200)
	match_history_key = models.CharField(max_length=200, default=None, null=True)

class Matchcode(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	matchcode = models.CharField(max_length=200)

class PlayerRankInstance(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	rank = models.IntegerField()

class Team(models.Model):
	player_1 = models.ManyToManyField(PlayerRankInstance, related_name="player_1")
	player_2 = models.ManyToManyField(PlayerRankInstance, related_name="player_2")
	player_3 = models.ManyToManyField(PlayerRankInstance, related_name="player_3")
	player_4 = models.ManyToManyField(PlayerRankInstance, related_name="player_4")
	player_5 = models.ManyToManyField(PlayerRankInstance, related_name="player_5")
	rank_averge = models.FloatField()
	rank_variance = models.FloatField()

class Match(models.Model):
	demo_url = models.CharField(max_length=200)
	datetime = models.DateTimeField()
	team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_1")
	team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_2")
