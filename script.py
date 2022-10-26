import git
import os
import json
import requests
import urllib.request
def getResp(input_test,dict_repos):
    git_link = input_test.split(" ")[0]
    commit_id = input_test.split(" ")[1]
    repoDir = "./" + "route" #local directory name where clone repo reside.
    path = "./route"
    if not os.path.exists(path):
    	os.system("mkdir route")
    #cloning the repo to local directory
    git.Git(repoDir).clone(git_link)
    for (root,dirs,files) in os.walk(repoDir, topdown=True):
        if 'Dockerfile' in files:
            file = open(root+"/Dockerfile","r")
            ls = []
            for each_line in file:
                if "FROM" in each_line and "#" not in each_line:
                    ls.append(each_line.split(" ")[1])
            path = root.split("\\")[-1] + "\\" + "Dockerfile"
            temp_dict1 = {path : ls}
            temp_dict2 = {commit_id : temp_dict1}
    dict_repos[git_link] = temp_dict2
    return dict_repos  

if __name__ == '__main__':
    url = input("Enter source file path : ")
    address = urllib.request.urlopen(url)
    data = str(address.read()).split("\\n")
    dict_repos = dict()
    dict_json = "Data"
    for each_line in data:
        if 'b' in each_line[0]:
            each_line = each_line.replace("b'","")
        if 'http' in each_line and not '#' in each_line:
            input_test = each_line
            dict_repos = getResp(input_test,dict_repos)
    dict_json = {"Data" : dict_repos}
    json_data = json.dumps(dict_json)
    print(json.dumps(dict_json, indent = 3))
    os.system("rm -rf route")