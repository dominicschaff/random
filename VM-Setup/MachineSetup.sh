apt-get update
apt-get upgrade
apt-get dist-upgrade
apt-get install vim
echo "alias update=\"sudo apt-get update; sudo apt-get upgrade; sudo apt-get dist-upgrade\"" >> .bashrc
echo "alias cleanup=\"sudo apt-get autoclean && sudo apt-get autoremove && sudo apt-get clean && sudo apt-get purge\"" >> .bashrc
echo "PS1='\[\e[31m\]\h \[\e[36m\]\t\[\e[37m\] \[\e[35m\]\W \[\e[34m\]\$>\[\e[00m\] '" >> .bashrc
echo "alias cd..=\"cd ..\"" >> .bashrc
touch .hushlogin
echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

#Dev:
apt-get install htop npm openjdk-8-jdk git libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1 ruby
npm config set registry 'http://registry.npmjs.org/'
npm install npm -g
npm update npm -g
npm install -g n
n stablenpm
echo 'export ANDROID_HOME=$HOME/android-sdk-linux' >> .bashrc
echo 'export PATH=$PATH:$ANDROID_HOME/tools' >> .bashrc
echo 'export PATH=$PATH:$ANDROID_HOME/platform-tools' >> .bashrc
echo "After reboot run again but using dev2"
sleep 5
reboot

npm install -g yo cordova ionic grunt-cli bower grunt
/var/lib/dpkg/info/ca-certificates-java.postinst configure
#Documentation
apt-get install pandoc texlive-full
reboot

# network1:
cat - >> /etc/network/interfaces <<EOF

# Host-Only interface
auto eth1
iface eth1 inet static
    address    192.168.56.20
    netmask    255.255.255.0
    network    192.168.56.0
    broadcast  192.168.56.255
EOF

# network2:
cat - >> /etc/network/interfaces <<EOF

# Host-Only interface
auto eth1
iface eth1 inet static
    address    192.168.56.21
    netmask    255.255.255.0
    network    192.168.56.0
    broadcast  192.168.56.255
EOF
