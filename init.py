import git, os, shutil


#============================
#    os.environment['GIT_ASKPASS']= <full path to your script>
#    os.environment['GIT_USERNAME'] = <committer username>
#    os.environment['GIT_PASSWORD'] = <the password>
#============================

DIR_NAME = "../temp"
REMOTE_URL = "https://github.com/hasinhayder/LightBulb.git"
 
if os.path.isdir(DIR_NAME):
    shutil.rmtree(DIR_NAME, ignore_errors=True)
 
os.mkdir(DIR_NAME)
 
repo = git.Repo.init(DIR_NAME)
origin = repo.create_remote('origin',REMOTE_URL)
origin.fetch()
origin.pull(origin.refs[0].remote_head)
git.ex
print "---- DONE ----"