## linux commands
- [apt commmand guide](https://itsfoss.com/apt-command-guide/)

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
  

## What's the difference between apt and apt-get

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
