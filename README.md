# baby-timed-radio

An open source, containerised app that simple plays music for a defined period of time on the client.  [Sean](https://seanland.ca) created this to play bedtime music for his newborn baby.  

```
# build it
docker build -t baby-timed-radio .

# run it
docker run -p 5000:5000 -v /your/local/Music:/music baby-timed-radio
```

## Created By: 
[Sean Clarke](https://seanland.ca)

## How To Support
Feel free to contribute!  Enchance it, document it! Great first time for new git, python and docker users. 

[Donate if you like my work!](https://ko-fi.com/seanland)