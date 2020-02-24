import os


def get_uploaded_images():
    rootdir = os.getcwd()
    print(rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            print(os.path.join(subdir, file))
