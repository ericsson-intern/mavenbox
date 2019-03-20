#this script(module) updates a pom.xml file with a specific artifactid/groupid/version/type/classifier dependency  
#if the dependency is already there, the version is checked and updated if needed  
#the comparison of dependencies is based on artifactid/groupid/type (and optionally classifier). other fields are ignored  
#the pom file should be in UTF-8  


import os  
import xml.etree.ElementTree as ET  
import xml.dom.minidom as minidom  
import sys,re  
import argparse  
   
class PomEditor:

    def __init__(self,param_pomlocation):
        
        self.pom_et=()
        self.pomlocation = param_pomlocation
        self.pom_ns=()
        self.artifactfound=False  
        self.pom_et_changed=False  
        self.pom_ns = dict(pom='http://maven.apache.org/POM/4.0.0') 
        
        #set the default namespace of the pom.xml file 
        ET.register_namespace('',self.pom_ns.get('pom')) 
        self._debug()

    def _debug(self):
        print('\n\n\n\n/////////////////// PomEditor Instance //////////////////////\n')    
        
    def __del__(self):
        # print('PomEditor class instance destroyed')
        pass

    #read a file and return a ElementTree  
    def get_tree_from_xmlfile(self,filename):  
        if os.path.isfile(filename):  
            tree = ET.parse(filename)  
            return tree  
        else:  
            raise Exception('Error opening POM: '+filename)  


    #obtain a specific element from an ElementTree based on an xpath  
    def get_xpath_element_from_tree(self,tree,xpath,namespaces):  
        return tree.find(xpath, namespaces)  


    #returns the content of an element as a string  
    def element_to_str(self,element):  
        return ET.tostring(element, encoding='utf8', method='xml')  


    #returns an ElementTree as a pretty printed string  
    def elementtree_to_str(self,et):  
        root=et.getroot()  
        ugly_xml = ET.tostring(root, encoding='utf8', method='xml')  
        dom=minidom.parseString(ugly_xml)  
        prettyXML=dom.toprettyxml('\t','\n','utf8')  
        trails=re.compile(r'\s+\n')  
        prettyXML=re.sub(trails,"\n",prettyXML)  
        return prettyXML  
    

    #update the version of a dependency in the pom ElementTree if it is already present.
    #returns the updated ElementTree and a boolean indicating if the pom ElementTree has been updated  
    def update_dependency(self,param_artifactid,param_version):  
        print('======================= updating dependency========================')
        self.pom_et= self.get_tree_from_xmlfile(self.pomlocation)
        print('file parsed as in-memory POM tree')
        for dependency_element in self.pom_et.findall('pom:dependencies/pom:dependency',self.pom_ns):  
            checkartifactid = self.get_xpath_element_from_tree(dependency_element,'pom:artifactId',self.pom_ns).text  
            print('recursing through all dependencies')
            if (checkartifactid == param_artifactid ):  
                self.artifactfound=True  
                print('Artifact found in ' + self.pomlocation)  
                pomversion=dependency_element.find('pom:version',self.pom_ns).text  

                if pomversion != param_version:  
                    print("Artifact has different version in "+ self.pomlocation + ". Updating")  
                    dependency_element.find('pom:version',self.pom_ns).text=param_version  
                    self.pom_et_changed=True  
                    print("changed_version: "+ pomversion+ " to "+ param_version)

                else:  
                    print "Artifact already in "+self.pomlocation+" with specified version. Update aborted"  
        return


    def commit_local(self):
        print('\nlocally commiting ... ')
        #overwrite the pomlocation if it has been changed  
        if self.pom_et_changed:  
            print('wrote')
            print "Overwriting "+self.pomlocation+" with changes"  
            target = open(self.pomlocation, 'w')  
            target.truncate()  
            target.write(self.elementtree_to_str(self.pom_et))  
            print('wrote')
            target.close()  
        else:  
            print self.pomlocation+" does not require file modifications"  

        print('done. ')







# ////////////////////////////////////////////////////////////////////////////////////////////////////////

def git_ignore(dirs):
    if('.git' in dirs):
        dirs.remove('.git')


import os


DIR_NAME = os.path.abspath(os.path.join(os.path.dirname(__name__),'temp'))
os.chdir(DIR_NAME)

for root, dirs, files in os.walk(DIR_NAME,topdown=True):
    git_ignore(dirs)
    for file in files:
        if file.endswith('pom.xml'):
            a=PomEditor(os.path.abspath(os.path.join(root, file)))
            a.update_dependency('junit','4.13')
            a.commit_local()
