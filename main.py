import subprocess

def update_libraries():
    print("Updating Libraries:\n")
    subprocess.run(["sudo", "apt-get", "update"])
    print("Libraries Updated!\n")

def install_apache_webserver():
    print("Installing Apache2 Webserver:\n")
    subprocess.run(["sudo", "apt-get", "install", "apache2", "-y"])
    print("Webserver Installed!\n")

def backup_and_replace_index_html():
    print("Backing up existing index.html file:")
    subprocess.run(["sudo", "mv", "/var/www/html/index.html", "/var/www/html/index.html.bak"])
    print("Copying Subdomain Takeover POC webpage to webserver directory:")
    subprocess.run(["sudo", "cp", "./index.html", "/var/www/html/index.html"])

def start_apache_service():
    print("Starting Apache2 Service:\n")
    subprocess.run(["sudo", "service", "apache2", "start"])
    print("You're All Set! Enjoy ;)\n")

def main():
    try:
        update_libraries()
        install_apache_webserver()
        backup_and_replace_index_html()
        start_apache_service()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()