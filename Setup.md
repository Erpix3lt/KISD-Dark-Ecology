## Basic Setup
ssh max@crawler.local

<Enter PW>

sudo apt upgrade

sudo apt update

<Add new ssh passkey to github>

Clone Project

## Get Light Detection Running
First connect the camera to its dedicated port. If you are running on the latest raspberry pi os, there should be no additional configuration needed.

### Install CV2
https://askubuntu.com/questions/1330968/how-can-i-install-python-opencv-package-in-ubuntu-20-04
https://raspberrypi-guide.github.io/programming/install-opencv
sudo apt-get update

sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

sudo apt-get install python3-opencv

### Install PiCamera2
https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
sudo apt install -y python3-picamera2

### Install GPIOZERO
sudo apt install python3-gpiozero

### Run the main.py

## Get Servo Running
Connect Servo to GPIO 26 the left one to GPIO 13 and Ground, Power to 10V

### Servo Notes
Going Backward Everything under <7 6 being the fastest 1 is not moving
Going Forward Everything above >7 11 being the fastest 7.5 the slowest

## Get the crawler running
For a bit of context:
`cd` -> Change Directory
`ssh`-> Connect over the wireless lan
`python` -> executes the python code

Hit enter after each command!

1. Rename your I phone to `Raspi-Hotspot`, this is so the raspberry can connect to it. Then change your Iphones Hotspot password to Barcelona84 <br> https://support.apple.com/en-bn/guide/iphone/iphf256af64f/ios
3. Open the app Powershell on windows, alternativly open CMD on windows
4. Your computer must also be connected to the same hotspot as the raspberry
5. In either powershell or CMD type in the command: `ssh max@crawler.local`
6. You are then prompted to enter the password, type in `crawler`, you might not see that you are typing in text, hit enter regardless when you are finished typing in.
7. YOU ARE NOW ON THE RASPBERRY PI!! :)
8.  Navigate to the correct folder, you can hit TAB for autocompletion: `cd KISD-Dark-Ecology/code/crawler`
9.  In order to execute the servo_service_test script run: `python servo_service_test.py`
10.  If you want to stop it type: Control C









