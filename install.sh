echo "Downloading homebrew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

echo "Installing python3"
brew install python3

echo "Installing pyautogui..."
pip3 install pyautogui