import git
import getopt
import sys
repo = git.Repo(r'D:\myFiles\git_repository\picture_bed')
urlbase ='https://raw.githubusercontent.com/copbint/picture_bed/main/2021/'
imageNames = sys.argv
git = repo.git
print('Upload Success:')
for i in range(1,len(imageNames)):
    imageName = imageNames[i].split("\\")
    imageName = imageName[len(imageName)-1]
    git.add('2021/'+imageName)
    try:
        git.commit('-m', 'Add image: 2021/'+imageName)
    except:
        1+1
    finally:
        git.push("origin")
        print(urlbase + imageName)

