## run ffmpeg to create images to train a cog services model


```
ffmpeg -i ./video/croc-train.mp4 -filter:v fps=fps=1/1 ./train/croc-train-001_%000d.jpg
```
