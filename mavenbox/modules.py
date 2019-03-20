from POM.pom import PomEditor
from GitManager.util import GitAdaptor
import csv
import os


def git_ignore(dirs):
    if('.git' in dirs):
        dirs.remove('.git')


def tsv_util(file):
    list_tsv=[]
    with open(file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            list_tsv.append(row)
    return list_tsv


def update_dependency_aux(dir_path,artifact):

    if len(artifact) != 2:
        print('please provide valid artifact tuple as (\'name\'):(\'version\')')
        return

    repo_dir = dir_path
    os.chdir(repo_dir)

    for root, dirs, files in os.walk(repo_dir,topdown=True):
        git_ignore(dirs)
        for file in files:
            if file.endswith('pom.xml'):
                a=PomEditor(os.path.abspath(os.path.join(root, file)))
                a.update_dependency_tree(artifact[0],artifact[1])
                a.commit_local()


def url_dir_extract_name(url):
    link = 'https://github.com/msirrele/dc-metro-proxy'
    link = url
    l_strings = link.split('/')
    return l_strings[-1]+'.git'





# //////////////////////// DRIVER CODE /////////////////////////////

def update_dependency(COLLECTION_ROOT=None,TSV_FILE=None,URLS=None):

    if not COLLECTION_ROOT:
        COLLECTION_ROOT= os.path.abspath(os.path.join(os.path.dirname(__name__),'temp'))
    if not TSV_FILE:
        TSV_FILE = os.path.abspath(os.path.join(os.path.dirname(__name__),'artifacts.tsv'))
    if not URLS:
        URLS = ['https://github.com/ericsson-intern/maven-simple']


    artifacts = tsv_util(TSV_FILE)

    for url in URLS:
        
        # trim url and make individual local repos out of name
        repo_dir_name = url_dir_extract_name(url)
        repo_dir_abspath = os.path.join(COLLECTION_ROOT,repo_dir_name)
        os.makedirs(repo_dir_abspath)

        adaptor = GitAdaptor()
        print(repo_dir_abspath)
        adaptor.init(repo_dir_abspath, url )
        
        for artifact in artifacts:
            update_dependency_aux(repo_dir_abspath,(artifact['name'],artifact['version']))
            adaptor.push()

    # finally publish changes to remote repository
    adaptor.commit()


# //////////////////////// DRIVER CODE /////////////////////////////

# update_dependency()

