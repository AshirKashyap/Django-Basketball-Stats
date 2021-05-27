from models import NBAPlayer

f = open("data.txt", "r")

for line in f:
    strSpl = line.split(",")
    rebounds = strSpl[23]
    ppg = strSpl[29]

    newPlayer = NBAPlayer(
        totalRebounds = rebounds,
        totalPoints = ppg,
    )

    newPlayer.save()


f.close()
