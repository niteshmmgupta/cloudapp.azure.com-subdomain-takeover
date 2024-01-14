import os

# Updates libraries & install apache webserver
def webserver_installer():
    print("Updating Libraries : \n")
    os.system("sudo apt-get update")
    print("Libraries Updated!!\n")
    print("Installing Apache2 Webserver!!\n")
    os.system("sudo apt-get install apache2 -y")
    print("Webserver Installed\n")

# Creating POC webpage 
def create_webpage():
    os.system("sudo mv /var/www/html/index.html /var/www/html/index.html.bak")
    print("Copying POC webpage to webserver directory\n")
    os.system("sudo cp ./index.html /var/www/html/index.html")
    print("Starting Apache2 Service\n")
    os.system("sudo service apache2 start")
    print("You're All Set Enjoy ;)\n")

webserver_installer()
create_webpage()
