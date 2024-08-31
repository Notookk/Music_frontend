let time_elapsed = 0;
let response_time = 0;
let player
let isStarted = false;
let currentUserID

function InitWebsite(user_id, group_id) {
    currentUserID = user_id
    player = new Plyr('#player', {
        controls: [
            'progress', // The progress bar and scrubber for playback and buffering
        ]
    });

    const audioElement = document.getElementById('player')
    audioElement.src = 'no-sound.mp3';
    audioElement.load();

    player.on('timeupdate', () => {
        const currentTime = player.currentTime;
        document.getElementById('current-time').innerHTML = formatTime(currentTime);
    });


    player.on('loadedmetadata', () => {
        if (isStarted === true) {
            const totalTime = player.duration;
            document.getElementById('total-time').innerHTML = formatTime(totalTime);
            if (isPaused === true) {
                player.pause()
            }
            else {
                player.play()
            }

            const time_spent_on_response = new Date().getTime() - response_time; // in milliseconds
            player.currentTime = time_elapsed + time_spent_on_response / 1000;
        }
        else {
            // running no-sound.mp3
            player.play()
        }
    });

    initSocket(user_id, group_id, telegram.initData);
}

addEventListener(
    'DOMContentLoaded',
    () => {
        document.getElementById('queue-tab').addEventListener('click', () => {
            document.getElementById('queue-tab').classList.add('active-tab');
            document.getElementById('users-tab').classList.remove('active-tab');

            document.getElementById('queue-div').style.display = 'flex';
            document.getElementById('users-div').style.display = 'none';
        });

        document.getElementById('users-tab').addEventListener('click', () => {
            document.getElementById('users-tab').classList.add('active-tab');
            document.getElementById('queue-tab').classList.remove('active-tab');

            document.getElementById('users-div').style.display = 'flex';
            document.getElementById('queue-div').style.display = 'none';
        });
    }
)
