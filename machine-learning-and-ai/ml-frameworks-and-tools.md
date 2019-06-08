##compare frameworks (tensorflow vs tensorrt)

https://www.eriksmistad.no/deep-learning-inference-engines/

## What is onnx 

> The Open Neural Network Exchange Format (ONNYX) is a new standard for exchanging deep learning models. It promises to make deep learning models portable thus preventing vendor lock in. Let’s look at why that matter for the modern ML/AI developer.
>  
> https://blog.paperspace.com/what-every-ml-ai-developer-should-know-about-onnx/


## What is Yolo ? 


> Why use YOLO instead of another deep learning algorithm for object detection such as Fast R-CNN? The reason: Because YOLO is even faster.
Instead of applying the model to an image at multiple locations and scales, like conventional approaches, YOLO applies a single neural network to the full image for both classification and localization.
> YOLOv3 uses a custom variant of the Darknet architecture, darknet-53, which has a 53 layer network trained on ImageNet, a large-scale database of images labeled with Mechanical Turk (which is what we used for labeling our images in Step 2!). For object detection, 53 more layers are stacked on top, giving us a 106 fully convolution architecture as the basis for YOLOv3. YOLOv3 attempts prediction at three scales, downsampling the size of the input image by 32, 16, and 8.
> https://towardsdatascience.com/tutorial-build-an-object-detection-system-using-yolo-9a930513643a

# Darknet
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.
https://github.com/pjreddie/darknet


## tensor flow sample
https://www.edureka.co/blog/tensorflow-object-detection-tutorial/#tutorial-1

installation on jetson https://docs.nvidia.com/deeplearning/frameworks/install-tf-xavier/index.html

## python 

sudo apt-get update
sudo apt-get install python3.7
python3 --version

docs.python-guide.org/starting/install3/linux

## Deepstream

https://www.forbes.com/sites/janakirammsv/2019/03/23/microsoft-and-nvidia-deliver-intelligent-video-analytics-at-the-edge/#6519cbfa7623