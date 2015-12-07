# Livestreamer.bundle
Plex Media Server channel that makes use of the Livestreamer API to get video urls for services.

You should be able to use any url that is supported by Livestreamer.

### Usage:
The list of videos is created by editing the file:

`Plug-in Support\Data\com.plexapp.plugins.livestreamer\DataItems\streams.json`

Example `streams.json` file:
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
