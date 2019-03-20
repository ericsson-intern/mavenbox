import subprocess
import pipes,os
import shutil


class GitAdaptor:
    
    def __init__(self):
        self.REMOTE_URL='https://github.com/ericsson-intern/maven-simple'
        self.REPO_DIR = os.path.join(os.path.dirname(__name__),'temp_repo')

    def init(self,repo_folder=None,url=None):
        if not repo_folder:
            self.REPO_DIR = repo_folder
        if not url:
            self.REMOTE_URL= url



        if os.path.isdir(self.REPO_DIR):
            shutil.rmtree(self.REPO_DIR)
        os.mkdir(self.REPO_DIR)
        


        include_string='pom.xml'

        subprocess.call(['git' ,'init',self.REPO_DIR])
        subprocess.call('cd temp',shell=True)
        subprocess.call('cd',shell=True)
        self.resetcwd()
        subprocess.call("git remote add origin " + self.REMOTE_URL,shell=True)
        subprocess.call('git config core.sparsecheckout true',shell=True)


        f=open('./.git/info/sparse-checkout', 'w+')
        f.write(include_string)
        f.close()
        
        
        subprocess.call('git pull --depth=1 origin hello ',shell=True)



    def resetcwd(self):
        os.chdir(self.REPO_DIR)
        subprocess.call('cd',shell=True)

    def push(self):
        subprocess.call('git checkout ',shell=True)
        subprocess.call('git push origin hello ',shell=True)

    def commit(self):
        subprocess.call('git add -A ',shell=True)
        subprocess.call('git commit -m "edited dependency version"',shell=True)





# # init(self.REPO_DIR,self.REMOTE_URL)


# a=GitAdaptor()
# a.push()
# a.commit()