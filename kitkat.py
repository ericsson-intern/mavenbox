import subprocess
import pipes,os
import shutil


class GitAdaptor:
    
    def __init__(self):
        self.REMOTE_URL='https://github.com/ericsson-intern/maven-simple.git'
        self.DIR_NAME = os.path.join(os.path.dirname(__name__),'temp')

    def init(self,temp_folder,url):
        self.DIR_NAME = temp_folder

        if os.path.isdir(self.DIR_NAME):
            shutil.rmtree(self.DIR_NAME)
        os.mkdir(self.DIR_NAME)

        repo= '../temp_repo'
        self.REMOTE_URL= url
        glob='pom.xml'

        subprocess.call(['git' ,'init','temp'])
        subprocess.call('cd temp',shell=True)
        subprocess.call('cd',shell=True)
        self.resetcwd()
        subprocess.call("git remote add origin " + self.REMOTE_URL,shell=True)
        subprocess.call('git config core.sparsecheckout true',shell=True)


        f=open('./.git/info/sparse-checkout', 'w+')
        f.write(glob)
        f.close()
        
        
        subprocess.call('git pull --depth=1 origin hello ',shell=True)



    def resetcwd(self):
        os.chdir(self.DIR_NAME)
        subprocess.call('cd',shell=True)

    def push(self):
        self.resetcwd()
        subprocess.call('git checkout ',shell=True)
        subprocess.call('git push origin hello ',shell=True)

    def commit(self):
        self.resetcwd()
        subprocess.call('git add -A ',shell=True)
        subprocess.call('git commit -m "edited dependency version"',shell=True)





# init(self.DIR_NAME,self.REMOTE_URL)


a=GitAdaptor()
a.push()
a.commit()