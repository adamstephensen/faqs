# Front Door Demo Script
(Thanks Bec Lyons)


Hit the web site

```
 for i in {1..50}; do echo -n "Run # $i : :  "; curl -w 'Return Code: %{http_code}; Bytes received: %{size_download}; Response Time: %{time_total}\n' https://<yourwebsite>.azurewebsites.net/content/site.css -m 2 -o /dev/nul -s; done|tee /dev/tty|awk '{ sum += $NF; n++ } END { if (n>0) print "Average Resp time =",sum/n}'
```
 
With Front Door

```
FRONT DOOR:

for i in {1..50}; do echo -n "Run # $i : :  "; curl -w 'Return Code: %{http_code}; Bytes received: %{size_download}; Response Time: %{time_total}\n' <yourfrontdoor>.azurefd.net/Content/site.css   -m 2 -o /dev/nul -s; done|tee /dev/tty|awk '{ sum += $NF; n++ } END { if (n>0) print "Average Resp time =",sum/n}'
```
 
 
