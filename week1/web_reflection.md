 # Web Architecture Reflection
Stage 1 — DNS (Domain Name System): Your browser doesn't know where netflix.com lives. It first checks its own cache, then asks your operating system, then asks a DNS resolver (usually your ISP's). The DNS resolver eventually finds the authoritative name server for netflix.com and returns an IP address like 52.94.237.74. Think of DNS as a phone book — you look up a name to get the actual number.

Stage 2 — Firewall: Before your request even reaches Netflix's servers, it passes through a firewall. The firewall checks whether the request looks legitimate — is it coming from a suspicious IP? Is it a known attack pattern? If it looks fine, it's allowed through. If not, it's dropped

Stage 3 — Load Balancer: Netflix has thousands of servers, not one. A load balancer sits in front of them and decides which specific server should handle your request. It spreads traffic evenly so no single server gets overwhelmed. It's like a traffic controller at a busy intersection

Stage 4 — Web Server: The request arrives at a web server (like Nginx or Apache). The web server's job is to handle the HTTP protocol and serve static files — HTML, CSS, JavaScript, images. If you're requesting a simple static page, the web server can handle it entirely on its own.

Stage 5 — Application Server: For dynamic content (like your Netflix homepage showing your recommendations), the web server forwards the request to an application server. The application server runs the business logic — it knows who you are, what you've watched, and which shows to suggest. Think of it as the brain.

Stage 6 — Database: The application server needs your data — your watch history, your profile, your preferences. It queries a database, which returns the relevant records. The application server then assembles a response and sends it back up the chain to your browser.




When you load spotify.com, the web server serves you the static webpage — the HTML shell, the CSS styling, the JavaScript files. But when you press play on a song, the application server kicks in — it checks your subscription tier, applies geographic licensing rules, generates a streaming token, and tells the player which audio file to stream. One handles the delivery of files, the other handles the intelligence and logic.




Security. If your browser could talk directly to a database, any malicious user could craft database queries and steal or destroy data. The application server acts as a gatekeeper — it validates input, checks permissions, and only exposes what it's supposed to.



