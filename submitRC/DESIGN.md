# _General Start_
**`1: the beginning`**
```
We start by importing the libraries that we need and then some internalisation work, then we jump to check the version
of the used python if it's 2.7 or higher.
```
**`2: creating helper classes`**
```
We create an Error class to handle thrown exceptions, and in it, are 2 classes: one for Unix and one for Windows. Each
one initializes itself by importing more required libraries. We also have other methods in case it is linux. Then we
initialize one object from this class, in order to get characters from standard input.
```
**`3: doing the work`**
```
Now we define the main, and in it we start by listening to the ctrl-c, in case the user wants to cancel submission. Then
we get and parse the command line args and we put it all in a args object by using the argparse.ArgumentParser(). We
check to see if the user wants more detailes about the submision process by checking the verbose in args if it existes.
Now we sumbit the slug and exit with exit code 0.
```
# _Submission process_
**`1: checking connection and git version (414->434)`**
```
Check to see if git is installed, is a working version, then throw error if not to quit. Now we show the user that we
connecting to git, by calling the progress("Connecting"). Here we comunicate with the git api and we gete the headers.
We also set the current time and format it, then save it as a string.
```
**`2: get list of files to handel and ensure that the branch is valid (434->447)`**
```
We ensure that the slug exists in the branch from the submit50 repo, and if yes, then we get the list of files to upload
, and the list of files to exclude. If the slug is invalid, then we throw an exeption, and catch it in the catch section
, to tell the user to chech the slug, if s/he mistyped.
```
**`3: check for missing files and authenticating the connection with github (447->494)`**
```
We check if somthing is missing from the list that we recived from before, and if something is missing, we alert the
user by printing the name of the missing files names, and throw an error to end the submmision process.
If all is good, we start authenticating the user to the github repo to uploead the requiered files. The authentication
process can be via SSH, and if this failes, we use HTTPS, then we tell the user that we are preparing to upload the files.
```
**`4: clone repo, update and cache credentials, and check files (494->590)`**
```
We clone the repository, and if that fails, we tell the user why, and then we throw and exeption and stop the submmision.
We update the user's credentials that are stored in the config file localy. Get the list of files that we want to submit
and the list of files to ignore, then we unescape them and also hide the .gitattributes file from output. We also check
for large files to exclude from submmision. If any file is too huge to be submited, we raise an error and quit. If we
encounter large files, we install ilf from git and re-add the files to submission by force.
```
**`5: confirmation and uploading process (590->630)`**
```
Display files that will/will not be submitted, then ask the user to cinfirm submisstion. If yes, we display uploading to
him/her and commit to the branch, then we push. In the end we say successful submission, and we stop all.
```