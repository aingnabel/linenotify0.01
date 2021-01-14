
import requests
class linenotify:


    def __init__(self, tokenin):
        self.tokenin = token

    def lineconfig(self, command):
        url = 'https://notify-api.line.me/api/notify'
        token = self.tokenin
        header = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
        return requests.post(url, headers=header, data=command)

    def linems(self, message):
        # send plain text to line
        command = {'message': message}
        return self.lineconfig(command)

    def linest(self, stid, paid, message=' '):
        command = {'message': message, 'stickerPackageId': paid, 'stickerId': stid}
        return self.lineconfig(command)

    ''' def sendimage(self, url):
        command = {'message': " ", 'imageThumbnail': url, 'imageFullsize': url}
        return self.Lineconfig(command)
    '''


if __name__ == '__main__':
    token = 't7JZpU9RyierqkIF03tumN38ofZ8JaYokEKIsjdyhgX'
    messenger = linenotify(token)

    # send message
    messenger.linems('Hello world')

    # send sticker
    messenger.linest(1, 1)

