let queuedSongs = [];
let ConnectedUsers = []
let isPaused = false;

function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = Math.floor(seconds % 60);

    if (hours > 0) {
        return `${hours}:${minutes < 10 ? '0' : ''}${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    } else {
        return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    }
}

const styleElem = document.createElement('style');
document.head.appendChild(styleElem);

function changeSong(data) {
    console.log('Changing song to:', data);
    if (isStarted === true) {
        player.pause()
    }

    if (data === 'None') {
        document.getElementById('loader').style.display = 'none';
        document.getElementById('main-container').style.display = 'none';
        document.getElementById('no-song').style.display = 'flex';
        return;
    }

    isStarted = true;
    document.getElementById('loader').style.display = 'flex';
    document.getElementById('no-song').style.display = 'none';
    document.getElementById('main-container').style.display = 'none';

    const videoid = data['videoid']
    const title = data['title']
    const file_url = data['file'];
    isPaused = data['paused']

    time_elapsed = data['time_elapsed'];
    response_time = data['response_time'];

    // Change the song data on the page
    document.getElementById('song-title').innerHTML = title;

    const imageUrl = `https://mainmusic.4.213.40.172.sslip.io/yt_img/${videoid}/max`;
    document.getElementById('bg-image').src = imageUrl

    styleElem.innerHTML = `
.overlay-img:after {
    background: url('${imageUrl}') no-repeat center/cover;
}
    .bg-container{
    background: linear-gradient(to bottom, transparent 0%, var(--background-color) 100%), url('${imageUrl}') no-repeat center/cover;
}`

    // Set the audio element source
    const audioElement = document.getElementById('player');
    audioElement.src = file_url;
    audioElement.load();

    document.getElementById('loader').style.display = 'none';
    document.getElementById('main-container').style.display = 'flex';
}

function updateQueueList() {
    if (queuedSongs.length === 0) {
        document.getElementById('queue-tab').innerHTML = `Queue`;
        document.getElementById('song-list').innerHTML = `<p class="info">No Queued Songs</p>`;
        console.log('Queue is empty');
        return;
    }
    console.log('Updating queue:', queuedSongs);

    document.getElementById('queue-tab').innerHTML = `Queue (${queuedSongs.length} Songs)`;
    let html = ''

    for (let i = 0; i < queuedSongs.length; i++) {
        const song = queuedSongs[i];
        const title = song['title'];

        let duration = '0:00';
        if (song['duration'].toString().includes(':')) {
            // If the duration is in minutes:seconds format
            duration = song['duration']
        }
        else {
            // If the duration is in seconds, convert it to minutes:seconds
            duration = formatTime(song['duration']);
        }
        const videoid = song['videoid'];

        html += `<div class="song-item">
        <div class="song-img" style="background: url('https://mainmusic.4.213.40.172.sslip.io/yt_img/${videoid}/min') no-repeat center/cover;">
        </div>
        <div class="queue-name">
        <p>${title}</p>
        <p class="time-p">${duration}</p>
        </div>
        </div>`
    }

    document.getElementById('song-list').innerHTML = html;
}

function updateUsersList() {
    console.log('Updating Users List:', ConnectedUsers);

    const addedUsers = [];

    let html = '';

    ConnectedUsers.forEach(user => {
        const id = user[0];
        let name = user[2];
        let imgUrl;

        if (!addedUsers.includes(id)) {
            addedUsers.push(id);

            if (id === currentUserID) {
                name += ' (You)';
            }

            imgUrl = user[1] === 'None'
                ? 'https://mainmusic.4.213.40.172.sslip.io/static/default-profile-photo.jpg'
                : `https://mainmusic.4.213.40.172.sslip.io/user_img/${id}.jpg`;

            html += `
            <div class="song-item">
            <div class="song-img" style="background: url('${imgUrl}') no-repeat center/cover;"></div>
                    <div class="queue-name">
                        <p>${name}</p>
                    </div>
                    </div>`;
        }
    });

    document.getElementById('user-list').innerHTML = html;
    document.getElementById('users-tab').innerHTML = `Users (${addedUsers.length})`;
}
