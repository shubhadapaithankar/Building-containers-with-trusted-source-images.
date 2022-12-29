# Building containers with trusted source images.

Use Python scripts to automate the creation of a Dockerfile that specifies a trusted base image and any additional dependencies needed by your application.

Build and push the Docker image to a container registry using the docker build and docker push commands.

Deploy the container to a Kubernetes cluster using the kubectl command-line tool or a configuration file written in YAML.

By following these steps, you can build and deploy containers using trusted source images in Kubernetes, using Python scripts to automate the process.
### Important Libraries:

1. git : GitPython is a python library used to interact with git repositories. It is a module in python used to access our git repositories. It provides abstractions of git objects for easy access of repository data, and additionally allows you to access the git repository more directly using pure python implementation.

2. os: The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

3. json: JSON module that will help converting the datastructures to JSON strings. Use the import function to import the JSON module. The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.

4. urllib.request: The urllib. request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols.

### The Script is located at location: 
https://github.com/shubhadapaithankar/SRE-Challenge/blob/main/script.py
### Source File located at(input url): 

https://gist.githubusercontent.com/jmelis/c60e61a893248244dc4fa12b946585c4/raw/25d39f67f2405330a6314cad64fac423a171162c/sources.txt

To Run a Script perform the following steps:
1. run the scrip using : python3 script.py
2. Give the source file path as mention above(input url).
3. Output: (json response)


<img width="1131" alt="Screen Shot 2022-10-28 at 2 02 28 PM" src="https://user-images.githubusercontent.com/99461999/198731998-3f3ac7fb-5e73-42de-af6d-58a56ef12e47.png">



## Bonus work
I have installed minikube on Ubuntu AWS EC2 VM.
### Installation 

<img width="1305" alt="Screen Shot 2022-10-27 at 12 40 26 PM" src="https://user-images.githubusercontent.com/99461999/198384135-4cf42c0c-5407-47d7-aa0f-39a763bcfb1b.png">

### Interact with your cluster
<img width="665" alt="Screen Shot 2022-10-27 at 12 41 59 PM" src="https://user-images.githubusercontent.com/99461999/198384138-1b50855f-bdda-41e1-80de-72d8c1cb0b52.png">

### Deploy applications:
1. Test the sample application to test the Env.
<img width="731" alt="Screen Shot 2022-10-27 at 1 00 15 PM" src="https://user-images.githubusercontent.com/99461999/198386779-b2632923-1f88-40bf-9128-8a82189475fa.png">
