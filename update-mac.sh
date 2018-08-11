#!/bin/sh

brew update
brew outdated
brew upgrade
brew cleanup
npm update -g
npm install -g npm
sudo port -v selfupdate
sudo port selfupdate
sudo port upgrade outdated
sudo port uninstall inactive
sudo composer self-update
pip install -U pip
flutter upgrade
rustup update stable
pip3 install --upgrade pip

