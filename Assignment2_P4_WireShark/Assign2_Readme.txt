The following would be the readme instructions on how to run 
a. Basic files
b. Star files

a. Basic files:
   go to this directory by using cd command
   clean and run the directory which would lead us into a mininet
   now use the xterm commands to get into the respected terminals
   
   commands for the above:
   
   cd /home.p4/tutorials/exercises/basic
   make clean
   make run
   
   (in mininet)
   xterm h1 h2

   (in h2)
   bash h2-arp.sh
   python server.py

   (in h1)
   bash h1-arp.sh
   python client.py

   Now we are inside this 2 person (server<->client) link


b. Star files:
   go to this directory by using cd command
   clean and run the directory which would lead us into a mininet
   now use the xterm commands to get into the respected terminals
   
   commands for the above:
   
   cd /home.p4/tutorials/exercises/star
   make clean
   make run
   
   (in mininet)
   xterm h1 h2 h3

   (in h3)
   bash h3-arp.sh
   python server.py

   (in h2)
   bash h2-arp.sh
   python cache.py

   (in h1)
   bash h1-arp.sh
   python client.py

   Now we are inside this 3 person (server<->cache<->client) link
