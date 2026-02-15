# [VLR](https://vlr.gg) Data Scrapper

### Working with Teams, players, events and matches IDs:
The vlr.gg website is organised by a bunch of different IDs and this scripts take advantage of it.

In most of the scripts you'll find an "id" variable with a random value asigned to it, this value isn't random it's the team/match/event I used to test these scripts.

### How can I know which ID I need?
When you're inside any part of vlr.gg you'll notice the link has a bunch of numbers followed by a "/" and then the description of the page, for example:

https://www.vlr.gg/event/2682/vct-2026-americas-kickoff/main-event

Now this link can be shorted and it'll work the same way as it does with the link:

https://www.vlr.gg/event/2682

This way we can find our ID, in this case it's an event ID so if you use this ID make sure you use it in one of the scripts meant for events (some scripts will have a comment saying what kind of ID it's expecting to use)

#### You can find a list of different ID's here: [IDsList](./IDsList/README.md)

---
##### v0.1:
scrapcomps.py -> Gets all the recent comps that a team has been using on all maps

resultscrapper.py -> Gets all the results of different matchs inside the same event

scrapteams.py -> Gets all the teams that participates in an event
