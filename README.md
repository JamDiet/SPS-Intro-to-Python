# Installing Python

## Windows

1. Navigate to the Python downloads page: https://www.python.org/downloads/

2. The page should show a "Download Python 3.14.7" button. Click it to download the installer.

3. Once the installer has downloaded, open it and click "Install Now"

    - We recommend following the default installation instructions

4. To verify installation

    - Open a PowerShell terminal and type `python --version`

        - You should see `Python 3.14.7`

## macOS

1. Navigate to the Python downloads page: https://www.python.org/downloads/

2. The page should show a "Download Python 3.14.7" button, which downloads a `.pkg` installer

3. Once the installer has downloaded, open it and follow the prompts

    - We recommend following the default installation instructions
    - You may be asked to enter your Mac password to allow the install

4. To verify installation

    - Open Terminal and type `python3 --version`

        - You should see `Python 3.14.7`

## Linux

1. Install Python using the appropriate command for your distribution:

    - Debian/Ubuntu: `sudo apt update && sudo apt install python3`
    - Fedora: `sudo dnf install python3`
    - Arch: `sudo pacman -S python`

2. To verify installation

    - Open a terminal and type `python3 --version`

        - You should see `Python 3.14.7`


# Installing Visual Studio Code

In order to edit Python files, you need a text editor. We recommend using Visual Studio Code (VS Code).

## Windows

1. Navigate to the VS Code downloads page: https://code.visualstudio.com/download

2. Click the "Windows" download button to download the installer

3. Once the installer has downloaded, open it and follow the prompts

    - We recommend following the default installation instructions

## macOS

1. Navigate to the VS Code downloads page: https://code.visualstudio.com/download

2. Click the "Mac" download button to download a `.zip` file

3. Once the file has downloaded, open it to extract Visual Studio Code

4. Drag Visual Studio Code into your Applications folder

## Linux

1. Navigate to the VS Code downloads page: https://code.visualstudio.com/download

2. Download the package for your distribution:

    - Debian/Ubuntu: the `.deb` package
    - Fedora: the `.rpm` package

3. Install the downloaded package:

    - Debian/Ubuntu: `sudo apt install ./<file>.deb`
    - Fedora: `sudo dnf install ./<file>.rpm`
    - Arch: install the `code` package with `sudo pacman -S code`


# Hello World

The first test script people typically write when learning a new coding language is one that prints the phrase "Hello world!" Let's implement this now:

1. Open VS Code

2. Along the left side of the window should be an "Explorer" tab

    a. Inside the Explorer column, there should be a box that says "Open Folder". Click on this and open a folder in which you will be comfortable containing this project.

3. At the top of the Explorer column, you should now see the name of your project folder. Next to this, click on the button that says "New File..." and name your new file "hello_world.py"

4. In hello_world.py, type the following:

    `print("Hello world!")`

    - An example is included in this GitHub repository next to this README.md file

5. Run this script by pressing the "Run Python File" in the top right corner

    - You should see a terminal appear at the bottom of the window with the phrase "Hello world!"