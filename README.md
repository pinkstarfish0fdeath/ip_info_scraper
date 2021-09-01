UPDATE

ipinfo.io now requires an API token to retrieve data.  Also they're actively blocking all robot scans.  Good luck guys and gals!

# ip_info_scraper
Small program that takes any AS number from ipinfo.io and lists all associated IPv4 ranges via stdout.

***This script is a quick way to generate masscan lists using the ranges found on ipinfo.io.*** 

USAGE: python3 ip_info_scraper.py | when prompted input the AS number of your target and press enter.

If you desire to make a quick and easy text file point the output to a new file with python3 ip_info_scraper.py > targets.text

Could this be achieved with the ipinfo.io API? Yes.

Could this be achieved with JSON? Yes.  That version will come next.  

But, this script achieves the purpose it was designed for, even though parsing HTML is a pain in the ass. 

