## Interesting case studies

#### Farm Beats
- https://news.microsoft.com/transform/farmings-most-important-crop-may-be-the-knowledge-harvested-by-drones-and-the-intelligent-edge/
- https://news.microsoft.com/2018/05/07/dji-and-microsoft-partner-to-bring-advanced-drone-technology-to-the-enterprise/

#### Teaching drones to aid surf and rescue operations with Cognitive Serviecs
https://blogs.technet.microsoft.com/canitpro/2017/05/10/teaching-drones-to-aid-search-and-rescue-efforts-via-cognitive-services/ 


#### DJI Partnership
- Announcement: https://news.microsoft.com/2018/05/07/dji-and-microsoft-partner-to-bring-advanced-drone-technology-to-the-enterprise/ 
- Demonstration: https://www.youtube.com/watch?v=EruH-4Fvecc

#### Project Brainwave (using FPGAs to accelerate DNNs ie. Fast hardware to do AI faster ;-)
- https://www.forbes.com/sites/patrickmoorhead/2018/05/07/microsoft-shows-iot-momentum-with-new-support-from-qualcomm-nxp-and-dji/#21cfa9f0556c 
- https://www.microsoft.com/en-us/research/project/project-brainwave/ 

#### Airsim (training machine learning models using simulations)
- https://www.techrepublic.com/article/microsofts-ai-system-for-training-autonomous-cars-and-drones-goes-open-source/

#### Fish Detection in Darwin (not an actual drone case study but we use this ML from drones)
- https://news.microsoft.com/en-au/features/fishy-business-putting-ai-to-work-in-australias-darwin-harbour/

#### Powerline fault detection 
- https://blogs.technet.microsoft.com/machinelearning/2016/11/02/connected-drones-3-powerful-lessons-we-can-all-take-away/ 

#### Project Premonition – detecting pathogens before they cause outbreaks
- https://www.microsoft.com/en-us/research/project/project-premonition/ 

#### Airmap
- https://www.airmap.com/microsoft-azure-cloud-ethical-drone-skyguide/
- https://azure.microsoft.com/en-au/blog/building-an-ecosystem-for-responsible-drone-use-and-development-on-microsoft-azure/

#### Zerotech 
Zerotech smart pocket drone solution architecture
https://microsoft.github.io/techcasestudies/iot/2017/04/10/Zerotech.html


## What are some related open source projects ? 

- [The official DJI SDK](https://github.com/dji-sdk/Mobile-UXSDK-Android)
- [Demo - Dragon Drone](https://github.com/dwcares/DragonDrone) 
- [Demo - Mavic with Cognitive Services](https://github.com/Li-Yanzhi/DJI-CognitiveService)

## What are interesting articles out coding with drones ? 

- [Drone Girls - Announcing DJI Microsoft SDK](http://thedronegirl.com/2018/05/07/dji-microsoft-sdk/)
- [Hacking the Tello](https://gobot.io/blog/2018/04/20/hello-tello-hacking-drones-with-go/)
- [Drone Garage - Channel 9 videos](https://channel9.msdn.com/Shows/Drones-Garage)

## How can I start to understand drone mapping ?
This is a great article on drone mapping. https://www.dronepilotgroundschool.com/drone-mapping-software/

## What cool things are people doing with drones ? 
There are lots of awesome things people are doing with drones.
- [Using drones to track koalas](https://www.brisbanetimes.com.au/environment/conservation/heat-seeking-drones-find-brisbane-s-hiding-koalas-20181003-p507km.html)
- [Shark-detecting drones take to the skies in Australia](https://www.theverge.com/2017/8/28/16213416/drones-australia-shark-attack-ai-little-ripper)
- [Project Wing](https://x.company/projects/wing/)
- [Project wing is delivering GMG in SA](https://blog.x.company/testing-in-the-australian-skies-5a71db1ed6fe)
- [FAA Releases 2016 to 2036 Aerospace Forecast](https://www.faa.gov/news/updates/?newsId=85227&cid=TW414)
- [DJI AirWorks - Limitless Possibilities With Onboard SDK 3.2](https://binged.it/2zsHDfF)
- [Drones used by police forces](https://bc.ctvnews.ca/video?clipId=1536701)

#### Drones to spot sharks
- [The Verge - Shark-detecting drones take to the skies in Australia](https://www.theverge.com/2017/8/28/16213416/drones-australia-shark-attack-ai-little-ripper)
- [Nine - High-tech shark-spotting drones could soon patrol Aussie beaches](https://pickle.nine.com.au/2018/07/13/16/06/shark-attack-drone-patrolling-australian-beaches)
- [Northern Star - Technology keeps eye on sharks](https://www.northernstar.com.au/news/technology-keeps-eye-on-sharks/3168053/)
- [Ripper International - Shark Ppotter](https://www.ripperacademy.com/news-and-events/sharkspotter-algorithm-development)

# Development



## How does my drone interact with Azure AI Services ? 
```
With this SDK, we now have three methods to enable Azure AI services to interact with drone imagery and video in real-time:

Drone imagery can be sent directly to Azure for processing by an AI workload.
Drone imagery can be processed on Windows running Azure IoT Edge with an AI workload.
Drone imagery can be processed directly onboard drones running Azure IoT Edge with an AI workload.
```
https://azure.microsoft.com/en-au/blog/building-an-ecosystem-for-responsible-drone-use-and-development-on-microsoft-azure/

## Dronecode
airframe reference https://docs.px4.io/en/airframes/airframe_reference.html

"The library can run on a vehicle-based companion computer or on a ground-based GCS or mobile device " ... https://sdk.dronecode.org/en/


# Drones

#### DJI Mavic Pro
Is the Mavic Pro getting the Windows SDK ? 
Aparently yes ...https://stackoverflow.com/questions/50323037/mavic-pro-microsoft-build-2018-windows-sdk


#### DJI Mavic 2 Enterprise
https://www.dji.com/mavic-2-enterprise?utm_source=Twitter&utm_medium=Social&utm_campaign=M2E

#### Intel Ready to fly 
https://docs.px4.io/en/flight_controller/intel_aero.html
https://www.intel.com.au/content/www/au/en/products/drones/aero-ready-to-fly.html


#### DJI Matrice 200
Review https://bestdroneforthejob.com/drone-reviews/dji-matrice-200-review/


## Live streaming from drones

https://briandunnington.github.io/dronecast.html *todo*


## CPU vs GPU vs FPGA
https://ai4e.azurewebsites.net/fpga
