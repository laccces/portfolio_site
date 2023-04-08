<!DOCTYPE html>
<html>
<head>
    <title>My Playlist</title>
</head>
<body>
    <h1>My Playlist</h1>

    <div id="spotify-player"></div>

    <script src="https://sdk.scdn.co/spotify-player.js"></script>
    <script>
        window.onSpotifyWebPlaybackSDKReady = () => {
            const token = 'your_access_token'; // replace with your access token
            const player = new Spotify.Player({
                name: 'My Playlist',
                getOAuthToken: cb => { cb(token); }
            });

            // Error handling
            player.addListener('initialization_error', ({ message }) => { console.error(message); });
            player.addListener('authentication_error', ({ message }) => { console.error(message); });
            player.addListener('account_error', ({ message }) => { console.error(message); });
            player.addListener('playback_error', ({ message }) => { console.error(message); });

            // Playback status updates
            player.addListener('player_state_changed', state => { console.log(state); });

            // Ready
            player.addListener('ready', ({ device_id }) => {
                console.log('Ready with Device ID', device_id);
                const track_uris = {{ track_uris|tojson }};
                const play = ({
                    spotify_uri,
                    playerInstance: {
                        _options: {
                            getOAuthToken,
                            id
                        }
                    }
                }) => {
                    getOAuthToken(access_token => {
                        fetch(`https://api.spotify.com/v1/me/player/play?device_id=${id}`, {
                            method: 'PUT',
                            body: JSON.stringify({ uris: [spotify_uri] }),
                            headers: {
                                'Content-Type': 'application/json',
                                'Authorization': `Bearer ${access_token}`
                            },
                        });
                    });
                };

                // Play playlist
                const playPlaylist = () => {
                    track_uris.forEach(track_uri => {
                        play({
                            spotify_uri: track_uri,
                            playerInstance: player
                        });
                    });
                };

                // Play button
                const playButton = document.createElement('button');
                playButton.innerText = 'Play Playlist';
                playButton.onclick = playPlaylist;
                document.getElementById('spotify-player').appendChild(playButton);
            });

            // Connect to the player
            player.connect();
        };
    </script>
</body>
</html>
