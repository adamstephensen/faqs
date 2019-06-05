## Unsorted


code for uwp camera work https://blogs.msdn.microsoft.com/appconsult/2018/11/15/23535/
custom vision onyx uwp 
 - article https://elbruno.com/2019/01/22/onnx-object-recognition-with-customvision-and-onnx-in-windows-applications-using-windows-ml-2/
 - - code https://github.com/elbruno/events/tree/master/2019%2001%2010%20CodeMash%20CustomVision/CSharp 

uwp object detection
- https://github.com/microsoft/Windows-Machine-Learning/blob/master/Samples/SqueezeNetObjectDetection/UWP/cs/MainPage.xaml.cs
- https://github.com/mtaulty/WindowsMLExperiment





## Object Classification

#### UWP Object Classifier

- [Tutorial: Use an ONNX model from Custom Vision with Windows ML (preview)](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/custom-vision-onnx-windows-ml)

        - Source Code https://github.com/Azure-Samples/cognitive-services-onnx12-customvision-sample/

Other

- https://mtaulty.com/2018/03/11/first-experiment-with-image-classification-on-windows-ml-from-uwp/
        - has commnets about size and rgba

## Object Detection (With boxes)
- [Quickstart: Create an object detection project with the Custom Vision .NET SDK](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/csharp-tutorial-od)
        - shows how to call object detection api (cloud endpoint)
        - 
        - 
- How to do object detection from camera
    - https://elbruno.com/2018/06/28/winml-how-to-create-a-windows10-app-using-yolo-for-object-detection/
    - [code](https://github.com/elbruno/Blog/tree/master/20180704%20UwpMLNet%20TinyYoloV2)


- [Mr and Azure 310: Object detection](https://docs.microsoft.com/en-us/windows/mixed-reality/mr-azure-310)
        - This is a Hololens app but shows how to work with bounding boxes

- [Image classification with winml and uwp](https://blog.pieeatingninjas.be/2018/05/15/image-classification-with-winml-and-uwp/)
        - [update ](https://blog.pieeatingninjas.be/2019/04/22/image-classification-with-winml-and-uwp-update/)
        - [code](https://github.com/PieEatingNinjas/WinMLDemo)
        - uses static images, but runs onnx locallyh 
        - 
        - 

https://github.com/elbruno/events/tree/master/2019%2001%2010%20CodeMash%20CustomVision/CSharp/CustomVisionMarvel01
    - looks amazing
    - uwp, detection
    - 
https://github.com/microsoft/uwp-experiences/tree/master/apps/social
- good demo of camera app
         
        
## how to get a model file

```

            var uriSTring = $"ms-appx:///model.onnx";

            var modelFile = await StorageFile.GetFileFromApplicationUriAsync(new Uri(uriSTring));
```