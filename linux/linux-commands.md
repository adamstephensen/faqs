## To open a file 

If you wish to open files in graphical applications from the command line, such as within gnome-terminal or xterm then simply run:

``` bash
xdg-open $file
```

And it will open $file in an appropriate application for that file. The argument can also be a URL, so ``` xdg-open http://askubuntu.com/ ``` will open this site in your browser, and: ``` xdg-open mailto:someone@somewhere.com ``` should open your default mail program's composer, with someone@somewhere.com in the To: field.  
  
If what you want to view videos on a virtual terminal, without Xorg, you can use mplayer with the directfb, fbdev, fbdev2, sdl (with the frame buffer back-end), or svga as the video output, by running  

``` bash
mplayer -vo fbdev2 file.mpg
```

For example. For still images, you can install the fbi package, and use it to display images on a framebuffer.


## To open a video from terminal

First install vlc player by running the below commands on terminal

``` bash
sudo add-apt-repository ppa:videolan/stable-daily
sudo apt-get update
sudo apt-get install vlc
```

Then go into the directory which contains videos you want to play,

``` bash
cd /path/to/the/directory/which/contains/videos
```

Play the video from terminal using vlc player,

``` bash
vlc "videofilename.fileformat"
```

## To open a picture from terminal,

Install shotwell to open a picture via terminal,

``` bash
sudo add-apt-repository ppa:yorba/ppa
sudo apt-get update
sudo apt-get install shotwell
```

Then go into the directory which contain picture you want to open,

 ``` bash
cd /path/to/the/directory/which/contains/picture
```

Open the picture via terminal using shotwell,

```
shotwell "picturefilename.fileformat"
```

## Shutdown

for shut down ```sudo shutdown ```  
for restart ```sudo shutdown -r```  

## Text editors 
gedit
geany 


Running the Live Camera Recognition Demo
$ ./imagenet-camera googlenet           # to run using googlenet
$ ./imagenet-camera alexnet             # to run using alexnet

live camera detection demo
$ ./detectnet-camera facenet        # run using facial recognition network
$ ./detectnet-camera multiped       # run using multi-class pedestrian/luggage detector
$ ./detectnet-camera pednet         # run using original single-class pedestrian detector
$ ./detectnet-camera coco-bottle    # detect bottles/soda cans in the camera
$ ./detectnet-camera coco-dog       # detect dogs in the camera
$ ./detectnet-camera                # by default, program will run using multiped



# Building the Repo from Source

Provided along with this repo are TensorRT-enabled deep learning primitives for running Googlenet/Alexnet on live camera feed for image recognition, pedestrian detection networks with localization capabilities (i.e. that provide bounding boxes), and segmentation.  This repo is intended to be built & run on the Jetson and to accept the network models from the host PC trained on the DIGITS server.

The latest source can be obtained from [GitHub](http://github.com/dusty-nv/jetson-inference) and compiled onboard Jetson AGX Xavier and Jetson TX1/TX2.
      
#### Cloning the Repo
To obtain the repository, navigate to a folder of your choosing on the Jetson.  First, make sure git and cmake are installed locally:

``` bash
$ sudo apt-get install git cmake
```

Then clone the jetson-inference repo:
``` bash
$ git clone https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ git submodule update --init
```

#### Configuring with CMake

When cmake is run, a special pre-installation script (CMakePreBuild.sh) is run and will automatically install any dependencies.

``` bash
$ mkdir build
$ cd build
$ cmake ../
```

> **note**: the cmake command will launch the CMakePrebuild.sh script which asks for sudo while making sure prerequisite packages have been installed on the Jetson. The script also downloads the network model snapshots from web services.

#### Compiling the Project

Make sure you are still in the jetson-inference/build directory, created above in step #2.

``` bash
$ cd jetson-inference/build			# omit if pwd is already /build from above
$ make
$ sudo make install
```




## To list all video devices picked up by the kernel

```
ls -ltrh /dev/video*

```

## list all devices attached to USB 

```
lsusb 
```

## list all devices attached to PCI use 

```
lspci
```


dog walking video
https://www.youtube.com/watch?v=pCrpb_N6YG8


## Summary

``` bash
$ mkdir build
$ cd build
$ cmake ../

$ cd jetson-inference/build			# omit if pwd is already /build from above
$ make
$ sudo make install
cd aarch64/bin
detectnet multiped

```
