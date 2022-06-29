import os
os.syatem('wget -nc https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-i386.tar.xz && tar --skip-old-files -xvf tmate-2.4.0-static-linux-i386.tar.xz && cd tmate-2.4.0-static-linux-i386 && chmod +x tmate && ./tmate -S /tmp/tmate.sock new-session -d && ./tmate -S /tmp/tmate.sock wait tmate-ready && ./tmate -S /tmp/tmate.sock display -p '#{tmate_web}''
