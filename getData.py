import config, Repository, csv
import pyodbc, pysftp, paramiko
import hashlib as hl

class FingerprintKey:
    def __init__(self, fingerprint):
        self.fingerprint = fingerprint
    def compare(self, other):
        if callable(getattr(other, "get_fingerprint", None)):
            return other.get_fingerprint() == self.fingerprint
        elif other == self.get_fingerprint():
            return True
        elif hl.md5(other).hexdigest() == self.fingerprint:
            return True
        else:
            return False
    def __cmp__(self, other):
        return self.compare(other)
    def __contains__(self, other):
        return self.compare(other)
    def __eq__(self, other):
        return self.compare(other)
    def __ne__(self, other):
        return not self.compare(other)
    def get_fingerprint(self):
        return self.fingerprint
    def get_name(self):
        return u'ssh-rsa'
        #u'ssh-ed25519'
        #u'ssh-dss', etc
    def asbytes(self):
        return self


repo = repository.Repository()
config = config.Config()


# get data from database and create a csv file 
data = repo.get_data()
with open(config.path + 'filename.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(repo.columns)
    for item in data:
        writer.writerow(item)

# set up sftp connection
cnopts = pysftp.CnOpts()
cnopts.hostkeys.add(config.sftp_host, u'ssh-rsa 2048', FingerprintKey("1234566789key-without-:"))
with pysftp.Connection(config.sftp_host, username=config.sftp_user, private_key=config.sftp_pkPath, cnopts=cnopts) as sftp:
    
    with sftp.cd('/file/location/'):

        # drop file 
        try:
            sftp.put(config.path + 'filename.csv')
        except ValueError:
            print("put didn't work")

        # get file
        try:
            sftp.get('filename to get', 'C:\\path\\to\\save\\file\\file.txt')
            sftp.remove('/file/location/remove-this-file-from-sftp-site.txt')
        except ValueError:
            print("get didn't work")

