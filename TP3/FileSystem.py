import os
import sys
import stat
import errno
import random
import signal
import pwd
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from fuse import FUSE, FuseOSError, Operations

usertimeOut = 300


def handler(signum, frame):
        print("acabou o tempo para o utilizador")
        Passthrough.authenticadedUser = "none"

def checkUsr():
    username = pwd.getpwuid (os.getuid()).pw_name
    valido = False

    usrAutenticado = Passthrough.authenticadedUser

    print("recebi um pedido - " + usrAutenticado)
    if usrAutenticado == username:
        return True
    else:
        valido = validaUsr(username)

    if valido :
        Passthrough.authenticadedUser = username
        signal.alarm(usertimeOut)
        return True
    else:
        Passthrough.authenticadedUser = "none"
        return False





def validaUsr(username):
    
    codeSended = False
    
    with open('users.txt', 'r') as utilizadores:

        for linha in utilizadores:
            usr = linha.split('/')

            if(usr[0] == username): 
                # envia o email
                token = str(random.randint(10000000, 99999999))
                codeSended = sendCode(usr[1].strip(), token)
        
     
    if not codeSended:
        print("Erro - Utilizador invalido")
        return False

    svSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    svSocket.connect((socket.gethostname(), 12345))

    svSocket.settimeout(30)

    try:
        bytes = svSocket.recv(8)

        print("codigo recebido")

        msg = bytes.decode("utf-8")

    except socket.timeout:
        print("Erro: Expiraram os 30 segundos")
        msg = "   "
    finally:
        svSocket.close()
                  

    if msg == token:
        return True
    else:
        return False



def sendCode(email, code):

    msg = MIMEMultipart()

    msg['From'] = "ssitp32021@gmail.com"
    msg['To'] = email
    msg['Subject'] = "File System Code"

    msg.attach(MIMEText(code, 'html'))

    try:
    
        server = smtplib.SMTP("smtp.gmail.com", 587)
    
        server.starttls()
       
        server.login(msg['From'], "fmfcpzavetqviqio")
        
        server.sendmail(msg['From'], email, msg.as_string())
        
        server.close()
        print("Email enviado com sucesso")
        return True
    except:
        print ("Erro: envio do email falhou")
        return False

class Passthrough(Operations):

    authenticadedUser = "none"

    def __init__(self, root):
        self.root = root

    # Helpers
    # =======

    def _full_path(self, partial):
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    # Filesystem Methods
    # ==================

    def access(self, path, mode):
        full_path = self._full_path(path)            
        if not os.access(full_path, mode):
            raise FuseOSError(errno.EACCES)


    def chmod(self, path, mode):
        full_path = self._full_path(path)
        return os.chmod(full_path, mode)


    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))

    def readdir(self, path, fh):
        full_path = self._full_path(path)
        dirents = ['.', '..']
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        for r in dirents:
            yield r

    def readlink(self, path):
        pathname = os.readlink(self._full_path(path))
        if pathname.startswith("/"):
            return os.path.relpath(pathname, self.root)
        else:
            return pathname

    def mknod(self, path, mode, dev):
        return os.mknod(self._full_path(path), mode, dev)

    def rmdir(self, path):
        full_path = self._full_path(path)
        return os.rmdir(full_path)

    def mkdir(self, path, mode):
        return os.mkdir(self._full_path(path), mode)

    def statfs(self, path):
        full_path = self._full_path(path)
        stv = os.statvfs(full_path)
        return dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
            'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files', 'f_flag',
            'f_frsize', 'f_namemax'))

    def unlink(self, path):
        return os.unlink(self._full_path(path))

    def symlink(self, name, target):
        return os.symlink(target, self._full_path(name))

    def rename(self, old, new):
        return os.rename(self._full_path(old), self._full_path(new))

    def link(self, target, name):
        return os.link(self._full_path(name), self._full_path(target))

    def utimens(self, path, times=None):
        return os.utime(self._full_path(path), times)


    def create(self, path, mode, fi=None):
        full_path = self._full_path(path)
        return os.open(full_path, os.O_WRONLY | os.O_CREAT, mode)
    
    def open(self, path, flags):
        print("Pedido para Abrir ficheiro recebido")
        valido = checkUsr()
        if valido:
            full_path = self._full_path(path)
            return os.open(full_path, flags)
        else:
            raise FuseOSError(errno.EACCES)

    def read(self, path, length, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    def truncate(self, path, length, fh=None):
        full_path = self._full_path(path)
        with open(full_path, 'r+') as f:
            f.truncate(length)

    def flush(self, path, fh):
        return os.fsync(fh)

    def release(self, path, fh):
        return os.close(fh)

    def fsync(self, path, fdatasync, fh):
        return self.flush(path, fh)


def main(mountpoint, root):
    print("Sistema de ficheiros iniciado")
    signal.signal(signal.SIGALRM,handler)
    os.chmod("users.txt", 400)
    FUSE(Passthrough(root), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    main(sys.argv[2], sys.argv[1])