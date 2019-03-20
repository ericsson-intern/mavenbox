from POM.pom import PomEditor
from GitManager.util import GitAdaptor
import csv
import os


def git_ignore(dirs):
    if('.git' in dirs):
        dirs.remove('.git')


def tsv_util(file):
    list_tsv=[]
    with open('sample.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
    for row in reader:
        list_tsv.append(row)
    return list_tsv


def change_dependency(dir_path,artifact):

    if len(artifact) != 2:
        print('please provide valid artifact tuple as (\'name\'):(\'version\')')
        return

    DIR_NAME = dir_path
    os.chdir(DIR_NAME)

    for root, dirs, files in os.walk(DIR_NAME,topdown=True):
        git_ignore(dirs)
        for file in files:
            if file.endswith('pom.xml'):
                a=PomEditor(os.path.abspath(os.path.join(root, file)))
                a.update_dependency(artifact[0],artifact[1])
                a.commit_local()


def url_dir_name(url):
    link = 'https://github.com/msirrele/dc-metro-proxy'
    link = url
    l_strings = link.split('/')
    return l_strings[-1]+'.git'





# //////////////////////// DRIVER CODE /////////////////////////////


TEMP_DIR= os.path.abspath(os.path.join(os.path.dirname(__name__),'temp'))
TSV_FILE = os.path.abspath(os.path.join(os.path.dirname(__name__),'sample.tsv'))
URLS = []


artifacts = tsv_util(TSV_FILE)

for url in URLS:
    
    repo_dir_name = url_dir_name(url)
    repo_dir = os.path.join(TEMP_DIR,repo_dir_name)
    os.makedirs(repo_dir)

    adaptor = GitAdaptor()
    adaptor.init(repo_dir,url)
    
    for artifact in artifacts:
        change_dependency(repo_dir,(artifact['name'],artifact['version']))
        adaptor.push()

adaptor.commit()


# //////////////////////// DRIVER CODE /////////////////////////////



