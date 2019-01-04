## linux commands
- [apt commmand guide](https://itsfoss.com/apt-command-guide/)
- [debian apt user manual](https://www.debian.org/doc/user-manuals#apt-howto)
- [ubuntu aptget manual](https://help.ubuntu.com/community/AptGet/Howto)

apt command | description
------------| -----------
apt list --installed | list all packages installed
apt list --all-versions | list all packages available
sudo apt update | Updating the package database so you know what needs upgrading
apt list --upgradable | see upgradable packages
sudo apt upgrade | upgrade the installed packages (shows proposed changes and requests confirmation)
sudo apt full-upgrade | full-upgrade works the same as upgrade except that if system upgrade needs the removal of a package already installed on the system, it will do that
sudo apt update && sudo apt upgrade -y | update database & upgrade with y to confirmation
sudo apt autoremove | remove unnecessary  packages after upgrade
sudo apt install <package_1> <package_2> <package_3> | install a package(s) (and upgrade it if I already have it)
sudo apt install <package_name> --no-upgrade | install package, but don't upgrade it 
sudo apt install <package_name> --only-upgrade | don't install, just upgrade
sudo apt install <package_name>=<version_number> | install a specific version
sudo apt remove <package_name> | removes the binaries of a package. It leaves residue configuration files.
sudo apt purge <package_name> | removes everything related to a package including the configuration files.
apt search <search term>  | search for a package
apt show <package_name> | see the details of a package
  sudo apt autoremove | This command removes libs and packages that were installed automatically to satisfy the dependencies of an installed package. 
  

## What's the difference between apt and apt-get and dpkg

- [dpkg](https://help.ubuntu.com/lts/serverguide/dpkg.html.en) is a low level package manager. it can't download packages
- [apt vs apt-get](https://itsfoss.com/apt-vs-apt-get-difference/)
includes a list of apt and apt-get comands

apt command | apt-get command | description
------------| --------------- | -----------
apt install | apt-get install	 | Installs a package
apt remove  | apt-get remove	 | Removes a package
apt purge   | apt-get purge	 | Removes package with configuration
apt update  | apt-get update	 | Refreshes repository index
apt upgrade | apt-get upgrade | 	Upgrades all upgradable packages
apt autoremove| apt-get autoremove	 | Removes unwanted packages
apt full-upgrade| 	apt-get dist-upgrade | 	Upgrades packages with auto-handling of dependencies
apt search	| apt-cache search | Searches for the program
apt show	| apt-cache show	| Shows package details
apt list | (none) |	Lists packages with criteria (installed, upgradable etc)
apt edit-sources | (none) |	Edits sources list
??? | sudo apt-get install -f | apt-get fix broken packages


## What's the go with ```curl```

You use ```curl``` to download stuff.
- [project page](https://github.com/curl/curl)
- [manual](https://curl.haxx.se/docs/manual.html)


command | usage
--- | ---
 curl http://www.netscape.com/ | download a page
 curl -o thatpage.html http://www.netscape.com/ | download a page and store in thatpage.html
 curl -O http://www.netscape.com/index.html | get a remote file, and store it with it's own name
   curl -O www.haxx.se/index.html -O curl.haxx.se/download.html | download two files
 curl -L https://aka.ms/moby-engine-armhf-latest -o moby_engine.deb | -L, --location If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response code), this option will make curl redo the request on the new place.   


```
