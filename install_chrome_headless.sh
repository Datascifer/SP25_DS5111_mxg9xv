# Update package lists
sudo apt update

# Install dependencies
sudo apt install -y wget gnupg2

# Add Google's signing key
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

# Add Chrome's repository
echo "deb [arch=$(dpkg --print-architecture)] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list

# Update package lists again and install Google Chrome
sudo apt update
sudo apt install -y google-chrome-stable

# Verify install
google-chrome --version
