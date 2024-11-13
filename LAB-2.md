# Version Control with Git: Practice basic Git operations such as repository creation, file addition, committing changes, and pushing to a remote repository.
### Creating Repository
##### 1. Login to https://www.github.com/
##### 2. Click on the `+` icon on top right aside of search bar.
##### 3. Click on New Repository. This will open a page as below.
![image](https://github.com/user-attachments/assets/506235b4-2037-4d28-a0de-a6801a641cb7) ![image](https://github.com/user-attachments/assets/83179e28-b937-4d4f-a229-76660cc4dd45)
##### 4. Write a concise and compact repo name without spaces. You can use `-` or `_` for seperating words. Write a short description about your repository. Choose whether to keep it public or private and click on Add a README.md file. Also select the default gitignore template with the primary language of your project. Click on Create Repository. You will see a new repository created with the short description you provided written in the README.md file.
### File Addition, Committing Changes and Pushing to remote reposiotry
###### We can either add files commit and push them from the browser or from our command terminal. If we have to add simple files like markdown files we can do it from browser easily or else for code files that we need to test should be added and pushed from local syatem to remote repository.
##### 1. open command terminal of your system and ensure that git is installed on your device by clicking the following command to get the below output.
```bash
git -v
```
![image](https://github.com/user-attachments/assets/30a9337c-fd4e-42d8-8ce5-58b9f5ad8c74)
##### 2. Clone the repository by writing `git clone repo-url` to clone the newly created repository in your device. For example.
```bash
git clone https://www.github.com/Ritik-912/SOFTWARE-ENGINEERING-LABORATORY
```
##### 3. You can create a file using command terminal or from the File System depending on the OS which is more easy. For demo in windows we can create a file as follows from Command Terminal. But for complex task it is advisable to create file in the git folder from File Explorer and edit it using favoured text editor.
![image](https://github.com/user-attachments/assets/a0cee64b-54be-42a1-92a4-6512b1fe3496)
##### 4. Add the file to version control system i.e., git by using the following command. We used here . to add all newly created files. To just add a specific file we can write name of file in place of dot.
```bash
git add .
```
##### 5. Commiting the changes for pushing to remote repository with a message to remind what was the change about by reading the commit message.
```bash
git commit -m "Adding a new Demo File"
```
##### 6. Pushing the commit to remote repository by following command, It will ask for authentication if not authorized or else it will show a successful pushed message. Here origin is the name of local repository whose changes are being pushed to main branch of remote repository.
```bash
git push origin main
```
