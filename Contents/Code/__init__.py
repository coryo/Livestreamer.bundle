import livestreamer

NAME = 'Livestreamer'
PREFIX = '/video/livestreamer'
ICON = 'icon-default.png'
DATA_FILE = 'streams.json'

def stream_type(stream):
    """ get a string for the stream type """
    if isinstance(stream, livestreamer.stream.HLSStream):
        return "HLSStream"
    elif isinstance(stream, livestreamer.stream.HDSStream):
        return "HDSStream"
    elif isinstance(stream, livestreamer.stream.AkamaiHDStream):
        return "AkamaiHDStream"
    elif isinstance(stream, livestreamer.stream.HTTPStream):
        return "HTTPStream"
    elif isinstance(stream, livestreamer.stream.RTMPStream):
        return "RTMPStream"
    return None

@route(PREFIX+'/loadfile')
def load_file(file=DATA_FILE):
    try:
        data = Data.Load(DATA_FILE)
    except Exception:
        Log("Unable to load file.")
        return ObjectContainer()

    try:
        Dict['streams'] = JSON.ObjectFromString(data)
    except Exception:
        Log("Unable to parse JSON.")

    return ObjectContainer()

################################################################################
def Start():
    ObjectContainer.title1 = NAME

    if not Data.Exists(DATA_FILE):
        Data.Save(DATA_FILE, "[]")

    load_file(DATA_FILE)

@handler(PREFIX, NAME, ICON)
def MainMenu():       

    oc = ObjectContainer(no_cache=True)

    for item in Dict['streams']:
        oc.add(DirectoryObject(
            key=Callback(Qualities, url=item['url']),
            title=u'%s' % item['name']
        ))

    oc.add(DirectoryObject(
        key=Callback(load_file, file=DATA_FILE),
        title=u'%s' % "Reload streams.json"
    ))

    return oc

@route(PREFIX+'/qualities')
def Qualities(url):
    """ get streams from url with livestreamer, list the qualities """
    oc = ObjectContainer()
    try:
        streams = livestreamer.streams(url)
    except livestreamer.NoPluginError:
        Log("Livestreamer can't handle the url %s" % url)
        return oc
    except livestreamer.PluginError as err:
        Log("Livestreamer plugin error: %s" % err)
        return oc

    for quality in streams:
        oc.add(VideoClipObject(
            url="livestreamer://%s|%s" % (stream_type(streams[quality]),
                                          streams[quality].url),
            title=quality
        ))

    return oc
