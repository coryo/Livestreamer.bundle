# Livestreamer.bundle
Plex Media Server channel that makes use of the Livestreamer API to get video urls for services.

You should be able to use any url that is supported by [Livestreamer](http://docs.livestreamer.io/plugin_matrix.html).

### Usage:
The list of videos is created by editing the file:

`Livestreamer.bundle/Resources/default.json`

Example `default.json` file:
```json
[
    {
        "name": "Previously Recorded",
        "url": "http://www.twitch.tv/previouslyrecorded_live"
    },
    {
        "name": "Batman v Superman: Dawn of Justice - Official Trailer 2 [HD]",
        "url": "https://www.youtube.com/watch?v=fis-9Zqu2Ro"
    }
]
```
