audioPriority{
    'AV': 1
}

videoPriority{
    'MPEG4' : 1,
    'MP4' : 2
}

subtitlePriority{
    'SubtitleStationAlpha' : 1,
    'SRT' : 2,
    'PGS' : 3
}

def priorityCheck(codec:str, category:str):
    if category == "audio":
        try:
            priority = audioPriority[codec]
        except KeyError:
            priority = 7
    elif category == "subtitles":
        try:
            priority = subtitlePriority[codec]
        except KeyError:
            priority = 7
    elif category == "video":
        try:
            priority = videoPriority[codec]
        except KeyError:
            priority = 7
    else
        raise Exception(f'{category} is not an acceptable track type. Make sure category is of audio, subtitles, or video.')
    return priority

if __name__ == "__main__":
    from _track import Track
    