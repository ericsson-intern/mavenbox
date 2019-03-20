import subprocess
import pipes,os
import shutil


class GitAdaptor:
    
    def __init__(self,repo_folder=None,url=None):
    

        self.BRANCH = 'master'
        
        self.REPO_DIR = repo_folder
        self.REMOTE_URL = url
    


        print('asdfasdfasdfasdfasdfasdfasdf====')

        if os.path.isdir(self.REPO_DIR):
            shutil.rmtree(self.REPO_DIR)
        os.mkdir(self.REPO_DIR)
        


        include_string='pom.xml'
        
        subprocess.call(['git' ,'init'],cwd=self.REPO_DIR)
        # subprocess.call(['cd',self.REPO_DIR])
        # subprocess.call('cd',shell=True)
        # self.resetcwd()
        subprocess.call('cd',shell=True,cwd=self.REPO_DIR)
        subprocess.call("git remote add origin " + self.REMOTE_URL,shell=True,cwd=self.REPO_DIR)
        subprocess.call('git config core.sparsecheckout true',shell=True,cwd=self.REPO_DIR)


        f=open(os.path.join(self.REPO_DIR,'.git/info/sparse-checkout'), 'w+')
        f.write(include_string)
        f.close()
        
        
        subprocess.call('git pull --depth=1 origin ' + self.BRANCH ,shell=True,cwd=self.REPO_DIR)



    def resetcwd(self):
        os.chdir(self.REPO_DIR)
        subprocess.call('cd',shell=True)

    def push(self):
        subprocess.call('git checkout ',shell=True)
        subprocess.call('git push origin ' + self.BRANCH,shell=True)

    def commit(self):
        subprocess.call('git add -A ',shell=True)
        subprocess.call('git commit -m "edited dependency version"',shell=True)






# a=GitAdaptor()
# a.push()
# a.commit()