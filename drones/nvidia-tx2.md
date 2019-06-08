## Overviews
- great tx2 overview https://hackaday.com/2017/03/14/hands-on-nvidia-jetson-tx2-fast-processing-for-embedded-devices/
- programming languages for the jetson https://www.jetsonhacks.com/2016/08/18/thoughts-on-programming-languages-and-environments-part-iv-jetson-dev-kits/

## Tips for working with the tx2
- You need to run Linux on bare metal. 
- [Never use ```sudo``` to run jetpack](https://devtalk.nvidia.com/default/topic/1027939/inquire-about-jetpack-3-2/)
- [How to setup Ubuntu remote desktop](https://www.lifewire.com/setup-ubuntu-remote-desktop-4129666) (you can't connect from Windows)
- [Installing OpenCV on a tx2](https://jkjung-avt.github.io/opencv3-on-tx2/)
- [Python code to access OpenCV](https://gist.github.com/jkjung-avt/86b60a7723b97da19f7bfa3cb7d2690e)
- [IF the samples aren't installed download 'L4T Multimedia API Reerence from http://developer.nvidia.com/embedded/downloads](https://www.jetsonhacks.com/2017/03/21/jetpack-3-0-nvidia-jetson-tx2-development-kit/)
- if you get 'return code: 1' see https://devtalk.nvidia.com/default/topic/1027939/inquire-about-jetpack-3-2/

```
mkdir /home/me/jetpack
chmod 7777 /home/me/jetpack
mv <install.run file> /home/me/jetpack
cd /home/me/jetpack
./<install.run file>
```

## Getting started with the tx2

This article is awesome and is the source for many of the links on this page
https://medium.com/@surmenok/getting-started-with-nvidia-jetson-tx2-5952a2d8d7ae

JetPack 3.0 – NVIDIA Jetson TX2 Development Kit
https://www.jetsonhacks.com/2017/03/21/jetpack-3-0-nvidia-jetson-tx2-development-kit/

## Tutorials
- Hello world AI https://github.com/dusty-nv/jetson-inference

- [tensor flow on tx2](https://jkjung-avt.github.io/tf-trt-models/)
- [tensor flow models on tx2](https://jkjung-avt.github.io/tf-trt-models/) **this is the one for me to run on **

## doco
 - [Nvidia - tensorrt with phyton](https://docs.nvidia.com/deeplearning/sdk/tensorrt-developer-guide/index.html#python_topics)
 - [tensor rt containers](https://ngc.nvidia.com/catalog/containers/nvidia:tensorrt)
 - [tensorrt overview](https://devblogs.nvidia.com/speed-up-inference-tensorrt/)

- [Deep Vision tutorial for Tx2 / Nano](https://github.com/dusty-nv/jetson-inference)


## Compiling vs code on tx2 **todo**
https://devtalk.nvidia.com/default/topic/1035752/how-to-install-quot-visual-studio-code-quot-/


## Cog services
-  https://www.microsoft.com/developerblog/2017/05/12/food-classification-custom-vision-service/
- computer vision in real time https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/vision-api-how-to-topics/howtoanalyzevideo_vision
- custom vision docs https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/home


## Cog services and UWP
 - running an Onnx model in UWP https://github.com/Azure-Samples/cognitive-services-onnx12-customvision-sample/
 - uwp and custom vision https://www.henkboelman.com/running-win-ml-on-the-raspberry-pi/


## Jetson Nano
- [Basic setup](https://jkjung-avt.github.io/setting-up-nano/)




## Jetson TX2
- [Jetson Tx2 Home Page](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems-dev-kits-modules/)
- [NVidia blog - NVIDIA Jetson TX2 Delivers Twice the Intelligence to the Edge](https://devblogs.nvidia.com/jetson-tx2-delivers-twice-intelligence-edge/)
- [Jetson TX2 Official Specs](https://developer.nvidia.com/embedded/buy/jetson-tx2-devkit)
- [NVidia drone page](https://www.nvidia.com/en-us/autonomous-machines/uavs-drones-technology/)
-	[M600 with TX2 for shark spotting](https://www.youtube.com/watch?v=GF_M4XB--UQ)
-	[Unboxing tx2](https://www.youtube.com/watch?v=kl2rMlHde4k )
- [Jetpack 3.0 and TX2](https://www.youtube.com/watch?v=D7lkth34rgM)
- [VentureBeat - Nvidia’s Jetson platform can power drones with good artificial intelligence](https://venturebeat.com/2017/03/07/nvidias-jetson-platform-can-power-drones-with-good-artificial-intelligence/)
- [drone pilotted by dnn](https://www.youtube.com/watch?v=voVxIGyeqgo)

## Jetson AGX Xavier (TX2s big brother)
- [Official Specs](https://developer.nvidia.com/embedded/buy/jetson-xavier-devkit)

## DJI Drone support for onboard video
https://github.com/dji-sdk/Onboard-SDK/issues/280

##DJI Ros 
https://github.com/ethz-asl/mav_dji_ros_interface/wiki/Introduction

## Intel and Microsoft on the edge
https://newsroom.intel.com/news/intel-microsoft-enable-ai-inference-edge-intel-movidius-vision-processing-units-windows-ml/

## AI - unsorted
- https://github.com/vjrantal/iot-edge-darknet-module
- https://gist.github.com/seank-com/9d9bf1ffcbd0acb5129246c8e32de687
- https://devblogs.microsoft.com/iotdev/a-workaround-to-run-azure-iot-edge-on-arm64-devices/
- https://www.quantumobile.com/object-detection-on-nvidia-jetson-tx2/

- how to load tensor flow models with open cv
- https://jeanvitor.com/tensorflow-object-detecion-opencv/
- https://github.com/Azure/iotedge/issues/104
- https://github.com/ethz-asl/mav_dji_ros_interface/wiki/Introduction
- autonomous drone navigation video https://www.youtube.com/watch?v=voVxIGyeqgo
- https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-model-python
- https://github.com/Microsoft/Cognitive-Samples-VideoFrameAnalysis/
- https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/Vision-API-How-to-Topics/HowtoAnalyzeVideo_Vision
- https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-core-3-0
- https://gist.github.com/richlander/467813274cea8abc624553ee72b28213
 



## Jetson TX2
- [Jetson Tx2 Home Page](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems-dev-kits-modules/)
- [NVidia blog - NVIDIA Jetson TX2 Delivers Twice the Intelligence to the Edge](https://devblogs.nvidia.com/jetson-tx2-delivers-twice-intelligence-edge/)
- [Jetson TX2 Official Specs](https://developer.nvidia.com/embedded/buy/jetson-tx2-devkit)
- [NVidia drone page](https://www.nvidia.com/en-us/autonomous-machines/uavs-drones-technology/)
-	[M600 with TX2 for shark spotting](https://www.youtube.com/watch?v=GF_M4XB--UQ)
-	[Unboxing tx2](https://www.youtube.com/watch?v=kl2rMlHde4k )
- [Jetpack 3.0 and TX2](https://www.youtube.com/watch?v=D7lkth34rgM)
- [VentureBeat - Nvidia’s Jetson platform can power drones with good artificial intelligence](https://venturebeat.com/2017/03/07/nvidias-jetson-platform-can-power-drones-with-good-artificial-intelligence/)
- [drone pilotted by dnn](https://www.youtube.com/watch?v=voVxIGyeqgo)

## Jetson AGX Xavier (TX2s big brother)
- [Official Specs](https://developer.nvidia.com/embedded/buy/jetson-xavier-devkit)

## DJI Drone support for onboard video
https://github.com/dji-sdk/Onboard-SDK/issues/280

##DJI Ros 
https://github.com/ethz-asl/mav_dji_ros_interface/wiki/Introduction

## Intel and Microsoft on the edge
https://newsroom.intel.com/news/intel-microsoft-enable-ai-inference-edge-intel-movidius-vision-processing-units-windows-ml/

## AI - unsorted
- https://github.com/vjrantal/iot-edge-darknet-module
- https://gist.github.com/seank-com/9d9bf1ffcbd0acb5129246c8e32de687
- https://devblogs.microsoft.com/iotdev/a-workaround-to-run-azure-iot-edge-on-arm64-devices/
- https://www.quantumobile.com/object-detection-on-nvidia-jetson-tx2/

- how to load tensor flow models with open cv
- https://jeanvitor.com/tensorflow-object-detecion-opencv/
- https://github.com/Azure/iotedge/issues/104
- https://github.com/ethz-asl/mav_dji_ros_interface/wiki/Introduction
- autonomous drone navigation video https://www.youtube.com/watch?v=voVxIGyeqgo
- https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-model-python
- https://github.com/Microsoft/Cognitive-Samples-VideoFrameAnalysis/
- https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/Vision-API-How-to-Topics/HowtoAnalyzeVideo_Vision
- https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-core-3-0
- https://gist.github.com/richlander/467813274cea8abc624553ee72b28213
