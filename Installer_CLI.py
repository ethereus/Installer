##
## Installer.py
## Package Installer
##
## Created by Wz on 17/09/20
## Copyright © 2020 Wz. All rights reserved.
##

#declaring globals

global repoStatus
global fileName
global url
global downloadType
global identifier
global version
global filePath
global packageName
global updateList
global choice
global name
global activeRepo
global updateInstall


# -----------------------------------------------------------------------
# ----------------------- REPOSITORY MANAGEMENT -------------------------
# -----------------------------------------------------------------------


#import os for editing file path to variable

import os

#import tqdm for download progress 

from tqdm import tqdm

#import urllib for reading a file from the web without saving a local copy

import urllib.request, requests

#import json for working with repo files

import json 

#import libraries for database management

import sqlite3, os

print(' ')
print('--------------------------------------------------------------------------')

#if there is no package directory then creates one as it is needed for this program to function

if not os.path.isdir('Packages'):

        os.mkdir('Packages')
        
        print('CONSOLE: the Packages directory was missing and has been replaced')

#if there is no local package database then creates one as it is needed for this program to function

if not os.path.isfile('Packages/Packages.db'):
    
        db = sqlite3.connect('Packages/Packages.db')
        c = db.cursor()

        #creates the table PackageInfo to hold useful data about packages for the user to be able to view
    
        c.execute('''CREATE TABLE PackageInfo
        (identifier TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        version TEXT NOT NULL,
        url TEXT NOT NULL)
        ''')

        #creates the table Installed to hold data about packages that is needed for management

        c.execute('''CREATE TABLE Installed
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT NOT NULL,
        packageID TEXT NOT NULL,
        FOREIGN KEY(packageID) REFERENCES PackageInfo(identifier))
        ''')
    
        db.commit()
        db.close()

        print('CONSOLE: the installed packages database was missing and has been replaced')

#if there is no package directory then creates one as it is needed for this program to function

if not os.path.isdir('Sources'):

        os.mkdir('Sources')

        print('CONSOLE: the Sources directory was missing and has been replaced')

#if there is no local sources file then creates one as it is needed for this program to function

if not os.path.isfile('Sources/Sources.txt'):
    
        open('Sources/Sources.txt', 'a').close()

        print('CONSOLE: Sources file was missing and has been replaced')

#adds the default repo to the sources file unless it is already present

default = 'http://f4d3z.space/Installer'

file = open('Sources/Sources.txt', 'r')

if default in file.read():
        
        file.close()

else:

        file.close()

        file = open('Sources/Sources.txt', 'a')

        file.write(default)
        file.write('\n')

        file.close()

#function for adding a repository

def addRepo():

        url = input('repo: ')

        file = open('Sources/Sources.txt', 'r')

        #if repo already added then skips

        if url in file.read():
            print('INSTALLER:', url, 'already added')
            file.close()

        #adds the repo url to the sources list

        else:

            file.close()
            file = open('Sources/Sources.txt', 'a')
            file.write(url)
            file.write('\n')
            file.close()

            print('INSTALLER:', url, 'added to sources')

#function for removing a repository

def removeRepo():

        #reads the sources file and outputs the sources in a user friendly format

        file = open('Sources/Sources.txt', 'r')

        sources = file.readlines()
        
        length = len(sources)

        if length == 0:

                print('no sources to remove')
                menu()

        else:

                print('Repos:' + '\n')
                print(' ')

                for i in range(0, length):

                        print(sources[i].strip())

                file.close()

                url = input('enter repo url to remove: ')

                print('--------------------------------------------------------------------------')
                print('\n')

                #read all the data from the file
                
                with open("Sources/Sources.txt", "r") as file: 
              
                    data = file.readlines()
                    file.close()
              
                #write all the data back to the file except the repo to be removed
                
                with open("Sources/Sources.txt", "w") as file: 
              
                    for line in data : 
                  
                        if line.strip("\n") != url :  
                            file.write(line)
                            file.close()

                print('INSTALLER:', url, 'removed from sources')

#function for adding a downloaded package into the local database

def addPackage():

        global identifier
        global fileName
        global downloadType
        global version
        global filePath
        global activeRepo

        db = sqlite3.connect('Packages/Packages.db')
        c = db.cursor()

        #check if package is already in the database

        check = c.execute('''SELECT identifier FROM PackageInfo WHERE identifier = (?);''', [identifier])

        if check != identifier:               

                #insert the data of the downloaded package into the local database
                
                c.execute('''INSERT INTO PackageInfo VALUES (?, ?, ?, ?, ?)''', (identifier, fileName, downloadType, version, activeRepo))
                c.execute('''INSERT INTO Installed VALUES (NULL, ?, ?)''', (filePath, identifier))

                db.commit()
                db.close()

        else:

                #close the database since we are not inserting any data

                print('CONSOLE: package entry already exists, if the package file is missing it will be replaced now')

                db.close()

#functions for removing a installed package from the database

def choosePackageRemove():
        
        global identifier
        global name

        packages = []

        db = sqlite3.connect('Packages/Packages.db')
        c = db.cursor()

        #select all installed packages from local database

        c.execute('''SELECT name FROM PackageInfo''')

        data = c.fetchall()

        db.close()

        end = len(data)

        i = 0
        
        while i < end:

                packages.append(data[i][0])

                print(packages[i])

                i = i +1

        end = len(packages)

        if end == 0:

                print('no packages are currently installed')

                menu()

        else:

                print('\n')
                choice = input('enter name of package to remove: ')

                end = len(choice)

                if end == 0:

                        print('no package entered')

                        menu()

                else:

                        name = choice

                        db = sqlite3.connect('Packages/Packages.db')
                        
                        c = db.cursor()

                        c.execute('''SELECT identifier FROM PackageInfo WHERE name = ?''', (choice,))

                        data = c.fetchall()

                        identifier = data

                        db.close()
               

def removePackage():
        
        global identifier

        db = sqlite3.connect('Packages/Packages.db')
        c = db.cursor()
        
        c.execute('''SELECT path FROM Installed WHERE packageID = (?)''', (identifier[0]))

        path = c.fetchall()

        db.close()

        filePath = path[0][0]

        print(path)

        print(filePath)

        print('INSTALLER: removing package')

        db = sqlite3.connect('Packages/Packages.db')
        c = db.cursor()

        #remove package from the local database

        c.execute('''DELETE FROM Installed WHERE packageID = (?)''', (identifier[0]))
        c.execute('''DELETE FROM PackageInfo WHERE identifier = (?)''', (identifier[0]))

        db.commit()
        db.close()

        os.remove(filePath)

        print('INSTALLER: package has been removed')

#function for loading repo information

def chooseRepo():
        
        global choice

        print('Repos:')
        print('\n')

        name = []
        packagesFile = []
        author = []

        file = open('Sources/Sources.txt', 'r')

        sources = file.readlines()
        
        length = len(sources)
        

        for i in range(0, length):

                url = sources[i].strip()

                url = os.path.join(url, 'Repo.json')

                data = urllib.request.urlopen(url).read()

                contents = json.loads(data)

                end = len(contents)

                for x in range(0, end):

                        info = contents['Installer'][0]
                
                        name.append(info['repo_name'])
                        packagesFile.append(info['packages_file'])
                        author.append(info['author_name'])

                print('\n')
                print(name[i])
                print('author: ', author[i])
                print('\n')

                url = sources[i].strip()
                
        file.close()

        repo = input('enter the name of chosen repo: ')
        print('--------------------------------------------------------------------------')

        if not repo in name:

                while not repo in name:

                        print('the repo you have entered does not exist')
                        repo = input('enter the name of chosen repo: ')
                        print('--------------------------------------------------------------------------')

        i = name.index(repo)
        choice = packagesFile[i]


#function for listing packages on repo

def choosePackageAdd():
        
        global choice
        global identifier
        global activeRepo

        name = []
        idList = []

        #sets the json file location in the repository as a variable

        print('\n')
        print('Packages in repo: ')
        print('\n')

        repoFile = choice

        activeRepo = choice[:-13]

        data = urllib.request.urlopen(repoFile).read()

        contents = json.loads(data)
        
        end = len(contents['Installer']['Packages'])

        for i in range(0, end):
        
                for x in contents['Installer'].items():

                        data = contents['Installer']['Packages'][i]

                        name.append(data['name'])
                        idList.append(data['identifier'])

        for i in range(0, end):

                print(name[i])

                        
        print('\n')
        selection = input('enter the name of chosen package: ')
        print('--------------------------------------------------------------------------')

        if not selection in name:

                while not selection in name:

                        print('the package you have entered does not exist')
                        selection = input('enter the name of chosen package: ')
                        print('--------------------------------------------------------------------------')

        pos = name.index(selection)

        identifier = idList[pos]

#function for checking if updates are available for installed packages

def checkUpdates():

        print('CONSOLE: checking for package updates')

        #create a list to hold the installed repos
        #create a list for to hold identifier of packages with updates

        repos = []
        update = []

        with open("Sources/Sources.txt", "r") as file: 
              
                    data = file.readlines()
                    file.close()

        end = len(data)

        for i in range(0, end):

                repos.append(data[i].rstrip())

        #for how many installed repos there are:

        end = len(repos)

        for i in range(0, end):

                #save the current repo url to a variable

                url = repos[i]

                url = url + '/'
        
                #create a list for holding all the installed package identifiers
                #create a second list for holding all the installed package versions

                installedPackages = []
                installedVersions = []

                #store the names of installed packages in the list
                #store the versions of installed packages in the list

                db = sqlite3.connect('Packages/Packages.db')
                c = db.cursor()
                
                c.execute('''SELECT identifier FROM PackageInfo WHERE url = (?)''', (url,))

                identifiers = c.fetchall()
                
                c.execute('''SELECT version FROM PackageInfo WHERE url = (?)''', (url,))

                versions = c.fetchall()

                end = len(identifiers)

                #for how many packages there are installed from the repo:

                for i in range(0, end):

                        #add the data to the lists

                        installedPackages.append(identifiers[i])
                        installedVersions.append(versions[i])

                db.close()

                #load the repos packages file

                repoFile = url + 'Packages.json'

                data = urllib.request.urlopen(repoFile).read()

                contents = json.loads(data)

                end = len(contents['Installer']['Packages'])

                check = 'temp'

                #for how many packages there are on the repo:

                for z in range(0, end):

                        y = 0

                        #save the identifier to a variable

                        data = contents['Installer']['Packages'][z]

                        check = data['identifier']

                        #for how many packages are installed:

                        for i in range(0, len(identifiers)):

                                #check the saved identifier to the one that needs updating

                                #if they are the same then that is the position of the package

                                if check == identifiers[i][0]:

                                    #find version for check from json file

                                    #create a temp variable to hold the repo package version
                                    #store the version of the package to a temp variable

                                    temp = 'temp'

                                    info = contents['Installer']['Packages'][z]

                                    temp = info['version']

                                    current = installedVersions[i][0]

                                    #use the temp variable to check against the versions list

                                    if temp > current:

                                            update.append(installedPackages[i][0])

        check = len(update)

        if check == 0:

                print('no package updates available')
                menu()

        else:

                print('\n')
                print('CONSOLE: the following packages require updating:', update)

                #start the download of the new packages and update the version numbers in the local database

                print('--------------------------------------------------------------------------')
                updatePackages(update)

def updatePackages(update):

        global url
        global identifier
        global updateIdentifier
        global updateFileName
        global updateDownloadType
        global updateVersion
        global updateFilePath

        print('CONSOLE: the updates will now be downloaded and installed')
        print('\n')

        end = len(update)
        
        #for the number of packages that need updating:

        for i in range(0, end):

                #set identifier variable to the identifier in the update list

                identifier = update[i]

                #use the identifier to find the repo url from local database

                db = sqlite3.connect('Packages/Packages.db')
                c = db.cursor()
                
                c.execute('''SELECT url FROM PackageInfo WHERE identifier = (?)''', (identifier,))

                data = c.fetchall()

                #set the url variable to the repo url we just found

                url = data[0][0]

                #use the identifier to find the package type from local database

                c.execute('''SELECT type FROM PackageInfo WHERE identifier = (?)''', (identifier,))

                data = c.fetchall()

                #set the downloadType variable to the repo url we just found

                downloadType = data[0][0]

                #use the identifier to find the new package version from the repo

                repoFile = os.path.join(url, 'Packages.json')

                data = urllib.request.urlopen(repoFile).read()

                contents = json.loads(data)

                end = len(contents)

                x = 0

                for i in range(0, end):

                        check = contents['Installer']['Packages'][x]

                        check = check['identifier']

                        if check == identifier:

                                x = i

                        else:

                                i = i +1

                packages = contents['Installer']['Packages'][x]

                #set the version variable to the latest package version

                version = packages['version']

                name = packages['name']

                #update local database and remove outdated package from system
                
                c.execute('''UPDATE PackageInfo SET version = ? WHERE identifier = ?''',(version, identifier))

                db.commit()

                #remove the outdated package from the system

                c.execute('''SELECT path FROM Installed WHERE packageID = (?)''', (identifier,))

                path = c.fetchall()

                filePath = path[0][0]

                os.remove(filePath)

                db.close()

                #start download process

                updateIdentifier = identifier
                updateFileName = name
                updateDownloadType = downloadType
                updateVersion = version
                updateFilePath = filePath

                downloadPrep()


# -----------------------------------------------------------------------
# ----------------------- DOWNLOADING A TWEAK/APP -----------------------
# -----------------------------------------------------------------------


#function to start the download process after the package information is gathered

def startDownload():
       
        print('INSTALLER: preparing download')
        checkStatus()

#function to check if the url is/is still a repository
        
def checkStatus():

        global url
        global choice
        global identifier
        global repoStatus

        url = choice[:-13]

        print(url)

        repoStatus = False

        #loads data from the Repo file located on the server

        data = urllib.request.urlopen(url + 'Repo.json').read()

        contents = json.loads(data)

        #check to see if the repo is still valid before downloads begin
        #check to see if we can load data from the repo by checking if 'Installer' exists in the repo file

        #if the repo is valid then we move on to the download prep

        if 'Installer' in contents:

                repoStatus = True
                print('INSTALLER:', url, 'loaded successfully')
                downloadPrep()

        else:

                print('INSTALLER:', url, 'has failed to load')

#function to store all of the necessary information from the repository json file for downloading the package as variables
                
def downloadPrep():
        
        global identifier
        global url
        global fileName
        global downloadType
        global version

        #if the Applications directory is missing then replaces it as it is needed for this program to function

        if not os.path.isdir('Applications'):

                os.mkdir('Applications')

                print('CONSOLE: the Applications directory was missing and has been replaced')

        #if the Tweaks directory is missing then replaces it as it is needed for this program to function

        if not os.path.isdir('Tweaks'):

                os.mkdir('Tweaks')

                print('CONSOLE: the Tweaks directory was missing and has been replaced')

        print('INSTALLER: locating package information')

        #sets the json file location in the repository as a variable

        repoFile = os.path.join(url, 'Packages.json')

        #reads data from the file located on the server

        data = urllib.request.urlopen(repoFile).read()

        contents = json.loads(data)

        #stores the package information locally as variables

        end = len(contents['Installer']['Packages'])

        x = 0

        pos = 0

        for i in range(0, end):

                check = 'temp'

                data = contents['Installer']['Packages'][x]

                check = data['identifier']

                if check == identifier:
                
                        pos = x

                else:

                        x = x +1

        packages = contents['Installer']['Packages'][pos]

        fileName = packages['name']
        location = packages['url']
        downloadType = packages['type']
        version = packages['version']

        print('INSTALLER: package information found')
                

        #once the information needed is collected then start downloading tweak/app

        if downloadType == 'App':
            appDownload(location)
            
        if downloadType == 'Tweak':
            tweakDownload(location)
    
#function for downloading an app from the repository

def appDownload(location):

        global updateInstall

        if updateInstall == False:

                global identifier
                global fileName
                global downloadType
                global version
                global filePath

        elif updateInstall == True:

                global updateIdentifier
                global updateFileName
                global updateDownloadType
                global updateVersion
                global updateFilePath

        print('INSTALLER: installing package')

        #downloads the file in parts and writes the data to the specified location
        #keeps the file name the same by taking the file name from the server and appending it to the local path
        
        #using tqdm gives more control over the file download and also allows the download information to be displayed to the user

        buffer = 1024
        pull = requests.get(location, timeout=5)
        fileSize = int(pull.headers.get('Content-Length', 0))
        packageName = location.split('/')[-1]
        filePath = os.path.join('Applications', packageName)

        if updateInstall == False:
        
                if not os.path.exists(filePath):
                        
                    addPackage()
                    
                    progress = tqdm(pull.iter_content(buffer), f'Downloading {packageName}', total=fileSize, unit='B', unit_scale=True, unit_divisor=1024)
                    
                    with open(os.path.join('Applications', packageName), 'wb') as file:
                            
                            for data in progress:
                                    file.write(data)
                                    progress.update(len(data))

                    print(' ')
                    print('INSTALLER: finished installation')
                    print('--------------------------------------------------------------------------')
                    
                else:
                        
                    print('INSTALLER:', 'Application already installed')
                    print('--------------------------------------------------------------------------')

        else:
                    
            progress = tqdm(pull.iter_content(buffer), f'Downloading {packageName}', total=fileSize, unit='B', unit_scale=True, unit_divisor=1024)
            
            with open(os.path.join('Applications', packageName), 'wb') as file:
                    
                    for data in progress:
                            file.write(data)
                            progress.update(len(data))

            print(' ')
            print('INSTALLER: finished installation')
            print('--------------------------------------------------------------------------')

#function for downloading a tweak from the repository

def tweakDownload(location):

        global updateInstall

        if updateInstall == False:

                global identifier
                global fileName
                global downloadType
                global version
                global filePath

        elif updateInstall == True:

                global updateIdentifier
                global updateFileName
                global updateDownloadType
                global updateVersion
                global updateFilePath

        print('INSTALLER: installing package')

        #downloads the file in parts and writes the data to the specified location
        #keeps the file name the same by taking the file name from the server and appending it to the local path
        
        #using tqdm gives more control over the file download and also allows the download information to be displayed to the user

        buffer = 1024
        pull = requests.get(location, timeout=5)
        fileSize = int(pull.headers.get('Content-Length', 0))
        packageName = location.split('/')[-1]
        filePath = os.path.join('Tweaks', packageName)

        if updateInstall == False:
        
                if not os.path.exists(filePath):
                        
                    addPackage()
                    progress = tqdm(pull.iter_content(buffer), f'Downloading {packageName}', total=fileSize, unit='B', unit_scale=True, unit_divisor=1024)
                    
                    with open(os.path.join('Tweaks', packageName), 'wb') as file:
                            
                            for data in progress:
                                    file.write(data)
                                    progress.update(len(data))

                    print(' ')
                    print('INSTALLER: finished installation')
                    print('--------------------------------------------------------------------------')

                else:
                        
                    print('INSTALLER:', 'Tweak already installed')
                    print('--------------------------------------------------------------------------')

        else:
                        
            progress = tqdm(pull.iter_content(buffer), f'Downloading {packageName}', total=fileSize, unit='B', unit_scale=True, unit_divisor=1024)
            
            with open(os.path.join('Tweaks', packageName), 'wb') as file:
                    
                    for data in progress:
                            file.write(data)
                            progress.update(len(data))

            print(' ')
            print('INSTALLER: finished installation')
            print('--------------------------------------------------------------------------')


# -----------------------------------------------------------------------
# --------------------------- TEMPORARY MENU ----------------------------
# -----------------------------------------------------------------------


#temporary menu used to make testing quicker and easier
#will be replaced by a proper GUI in the future

def menu():

        global url
        global identifier
        global updateInstall

        #shows a user friendly menu interface for testing purposes

        print('')
        print('--------------------------------------------------------------------------')
        print('1. Download Package')
        print('2. Remove Package')
        print('3. Add Repo')
        print('4. Remove Repo')
        print('5. Update Packages')
        print('6. Exit')
        print(' ')

        option = input('choose an option >> ')

        print('--------------------------------------------------------------------------')

        #if the user wants to download a package

        if option == '1':

                updateInstall = False

                chooseRepo()

                choosePackageAdd()

                startDownload()

                menu()

        if option == '2':

                choosePackageRemove()

                removePackage()

                menu()

        if option == '3':

                addRepo()

                menu()

        if option == '4':

                removeRepo()

                menu()

        if option == '5':

                updateInstall = True

                checkUpdates()

        if option == '6':

                exit()


        else:

                print('invalid input, returning to menu..')
                menu()


# -----------------------------------------------------------------------
# ---------------------------- Testing Zone -----------------------------
# -----------------------------------------------------------------------


#this is where functions are called for testing

menu()
