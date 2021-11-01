import fetch
import pandas as pd

def test_getTrackIDs():
    ids = fetch.getPlaylistTracks('robbie.veglahn', '1Axb5oyohOnMjtzLPNoHoh') # retrieve autumnal playlist ids
    assert(len(ids) == 18)

def test_getTrackFeatures():
    ids = fetch.getPlaylistTracks('robbie.veglahn', '1Axb5oyohOnMjtzLPNoHoh') # retrieve autumnal playlist ids
    track = fetch.getTrackFeatures(ids[0]) 
    assert (len(track) == 16)

def test_getPlaylistDataSet():
    df = fetch.getPlaylistDataSet('robbie.veglahn', '1Axb5oyohOnMjtzLPNoHoh')
    ids = fetch.getPlaylistTracks('robbie.veglahn', '1Axb5oyohOnMjtzLPNoHoh') # retrieve autumnal playlist ids
    assert(len(df) == len(ids))