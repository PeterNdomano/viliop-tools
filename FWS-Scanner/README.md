## FWS Scanner
This tool fingerprints webserver that powers a target web app.

### Algorithm Summary
First it uses `BANNER GRABBING` by sending a request to the target url and checking if there is a Server Field on the headers. If server field is not found it tries to send `MALFORMED REQUESTS` and filter the response text to see if there is server name and version leaked. Refer to the flowchart for more
