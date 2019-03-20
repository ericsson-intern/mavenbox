import git, os, shutil


#============================
#    os.environment['GIT_ASKPASS']= <full path to your script>
#    os.environment['GIT_USERNAME'] = <committer username>
#    os.environment['GIT_PASSWORD'] = <the password>
#============================

DIR_NAME = os.path.join(os.path.join(os.path.dirname(__name__), '..'),'temp')
REMOTE_URL = "https://github.com/kevinsawicki/github-maven-example.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)

print "---- DONE ----"




