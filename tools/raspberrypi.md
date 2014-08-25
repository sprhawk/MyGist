Raspberry Pi
===========

1. streaming camera module:

    1. method RTP

    ```shell
    raspivid -o - -t 0 -n -w 320 -h 200 -fps 24 | avconv  -i - -f rtp rtp://192.168.1.122:855
    ```

    > v=0
    > o=- 0 0 IN IP4 127.0.0.1
    > S=No Name
    > c=IN IP4 192.168.1.122
    > t=0 0
    > a=tool:libavformat 53.21.1
    > m=video 8558 RTP/AVP 96
    > b=AS:200
    > a=rtpmap:96 MP4V-ES/90000
    > a=fmtp:96 profile-level-id=1

    ```shell
    ffplay -i test.sdp
    ```

    2. method VLC
    ```shell
    raspivid -o - -t 0 -n -w 320 -h 200 -fps 24 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
    ```

    ```shell
    ffplay http://raspberrypi.local:8090
    ```
