let telegram

function ContinueTelegram() {
    const user_id = telegram.initDataUnsafe.user.id
    const group_id = telegram.initDataUnsafe.start_param

    if (group_id === undefined) {
        telegram.showAlert('Use the /join command to join Group Music.', callback = () => {
            telegram.close()
        })
        return
    }

    telegram.enableClosingConfirmation()
    InitWebsite(user_id, group_id)
}

document.addEventListener('DOMContentLoaded', () => {
    telegram = window.Telegram.WebApp

    document.getElementById('join-btn').addEventListener('click', () => {
        document.getElementById('join-div').style.display = 'none';
        document.getElementById('loader').style.display = 'flex';

        telegram.ready()
        telegram.expand()
        telegram.setHeaderColor('#000813')
        telegram.setBackgroundColor('#000813')


        if (!telegram.isVersionAtLeast('7.6')) {
            telegram.showPopup(
                {
                    'title': 'Update Required',
                    'message': `Please update your Telegram app to continue using TechZMusic. Your current version is ${telegram.version}, but TechZMusic requires version 7.6 or higher to function properly.`,
                    'buttons': [
                        {
                            'id': 'Close',
                            'text': 'Close'
                        },

                    ]
                }
            )

            telegram.onEvent('popupClosed', function (data) {
                telegram.close()
            })
        }
        else {
            ContinueTelegram()
        }
    })
})
