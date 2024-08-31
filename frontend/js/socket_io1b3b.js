function initSocket(user_id, group_id, init_data) {
    const socket = io('https://mainmusic.4.213.40.172.sslip.io', {
        transports: ['websocket'],
        path: '/ws/socket.io', query: { 'user_id': user_id, 'group_id': group_id }
    });

    socket.on('connect', () => {
        console.log('Connected to server');

        socket.emit('verify_user', init_data);

    });

    socket.on('change_song', (data) => {
        changeSong(data);
    });

    socket.on('skip_songs', (no_of_skips) => {
        for (let i = 0; i < no_of_skips; i++) {
            queuedSongs.shift();
        }
        updateQueueList();
    });

    socket.on('disconnect', () => {
        console.log('Disconnected from server');
    });

    socket.on('add_to_queue', (data) => {
        console.log('Adding song to queue');
        console.log(data);
        for (let song of data) {
            queuedSongs.push(song);
        }
        updateQueueList();
    });

    socket.on('shuffle_queue', (data) => {
        console.log('Shuffling queue');
        console.log(data);
        queuedSongs = data;
        updateQueueList();
    });

    socket.on('add_users_list', (data) => {
        console.log('Adding users to list');
        console.log(data);
        for (let user of data) {
            ConnectedUsers.push(user);
        }
        updateUsersList();
    });

    socket.on('remove_users_list', (data) => {
        console.log('Removing user from list');
        console.log(data);
        for (let i = 0; i < ConnectedUsers.length; i++) {
            if (ConnectedUsers[i][0] === data) {
                ConnectedUsers.splice(i, 1);
                break;
            }
        }
        updateUsersList();
    });


    socket.on('pause_song', () => {
        isPaused = true
        player.pause();
    });

    socket.on('resume_song', () => {
        isPaused = false
        player.play();
    });

    socket.on('force_exit', () => {
        window.Telegram.WebApp.close();
    });


    socket.on('seek_song', (data) => {
        const time_spent_on_response = new Date().getTime() - data['response_time']; // in milliseconds
        player.currentTime = data['time_elapsed'] + time_spent_on_response / 1000;
    });


}
