from fs.sshfs import SSHFS

path = '/media/pidrive/pidata/share/Videos/neil.txt'
dest = '/Users/guillaumethomas/tmp/test_backup/'
dest2 = '/media/pidrive/pidata/share/Videos/neil2.txt'

class NasClient:
    def __init__(self):
        self.client = SSHFS("raspberrypi", "pi", "Pi314981")

    def change_dir(self, direct):
        self.client.opendir(direct)

    def list_dir(self, direct):
        self.client.listdir(self, direct)

    def copy(self, file):
        self.client.copy(path, dest2)

    def getfile(self):
        pass


if __name__ == "__main__":
    a = NasClient()
    a.copy("tt")
    a.client.close()
    print(a.client.isclosed())