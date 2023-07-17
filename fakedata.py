from faker import Faker
import random
import pandas as pd
from tqdm import tqdm
import numpy as np

# Initialize Faker library
fake = Faker()

# Define genres
genres = ["Pop", "Rock", "Hip-Hop", "Country", "Jazz", "Electronic", "Folk", "Blues", "R&B", "Indie"]

# Create random artists
artists = []
for _ in tqdm(range(200), desc='Generating artists'):
    artist = {
        "name": fake.name(),
        "about": fake.sentence()
    }
    artists.append(artist)

# Create random albums for each artist
albums = []
for i in tqdm(range(200), desc='Generating albums'):
    album = {
        "name": fake.catch_phrase(),
        "genre": random.choice(genres),
        "artist": artists[i % 200]  # assign artists in a round-robin fashion
    }
    albums.append(album)

# Create random tracks for each album
tracks = []
for i in tqdm(range(200), desc='Generating tracks'):
    track = {
        "name": fake.bs(),
        "genre": albums[i % 200]["genre"],  # the genre of the track is the same as the album's genre
        "description": fake.sentence(),
        "album": albums[i % 200],  # assign albums in a round-robin fashion
        "artist": albums[i % 200]["artist"]  # assign artists in a round-robin fashion
    }
    tracks.append(track)

# Create random playlists
playlists = []
for _ in tqdm(range(200), desc='Generating playlists'):
    playlist = {
        "name": fake.catch_phrase(),
        "tracks": [tracks[i] for i in random.sample(range(200), 5)]  # select 5 random tracks for each playlist
    }
    playlists.append(playlist)

# Create random wallet assets
wallet_assets = []
for _ in tqdm(range(200), desc='Generating wallet assets'):
    wallet_asset = {
        "name": fake.md5(),
        "fingerprint": fake.sha256(),
        "policyId": fake.sha1(),
        "quantity": random.randint(1, 100),
        "metadata": fake.word(),
        "assetSubjectId": fake.unique.random_number(digits=8),
        "logosphereId": fake.sha256()
    }
    wallet_assets.append(wallet_asset)

# Create random wallets
wallets = []
for _ in tqdm(range(200), desc='Generating wallets'):
    wallet = {
        "name": fake.catch_phrase(),
        "walletId": fake.sha1(),
        "address": fake.sha256(),
        "publicKey": fake.sha256()
    }
    wallets.append(wallet)

# Convert to pandas DataFrames
artists_df = pd.DataFrame(artists)
albums_df = pd.DataFrame(albums)
tracks_df = pd.DataFrame(tracks)
playlists_df = pd.DataFrame(playlists)
wallet_assets_df = pd.DataFrame(wallet_assets)
wallets_df = pd.DataFrame(wallets)

# Combine all dataframes into one
combined_df = pd.concat([artists_df, albums_df, tracks_df, playlists_df, wallet_assets_df, wallets_df], axis=1)

# Write to CSV
combined_df.to_csv("/Users/rajan/Documents/Github/logosphere-chat/data/music_data.csv", index=False)
