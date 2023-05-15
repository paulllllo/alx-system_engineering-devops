# Postmortem
After completing the ALX/holberton task 0x04 'Airbnb clone - Web frmework', approximately 00:07 West African Time (WAT), an outage occurred on an isolated Ubuntu 20.00 container running an Nginx web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file displaying a simple web site.

# Debugging Process
A very smart software engineer (me :)) encountered the issue upon opening the project and being, well, instructed to address it, roughly 01:09 WAT. He promptly proceeded to undergo solving the problem.

Checked running processes using ps aux. Two nginx processes - root and www-data - were properly running.

Looked in the sites-available folder of the /etc/nginx/ directory. Determined that the web server was serving content located in /var/www/html/ and other configured routes.

In one terminal, ran strace on the PID of the root nginx process. In another, curled the server. Expected great things... only to be disappointed. strace gave no useful information.

Repeated step 3, except on the PID of the www-data process. Kept expectations lower this time... but was rewarded! strace revelead an -1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/index.html.

Looked through files in the /var/www/html/ directory one-by-one, also checking their contents. I found that the index.html file was named incorrectly. I went throught the last few scripts i ran on the web server and found that i misspelt the file name and replaced the existing file... oops ;).

Corrected the script but didn't run it again because it might break configurations made after. I also corrected the filename by moving the content into the correct filename and removing the first file.

Tested another curl on the server. 200 A-ok!

Wrote a Puppet manifest to automate fixing of the error and other similar error-types.

# Summation
In short, a typo. Gotta love'em. In full, the app was encountering problems when trying to access a 'index.html' file which is the default file set in the configuration but could not find a file with that filename.

Patch involved a simple fix on the typo, comparing the filename to the expected filename and correcting where necessary.

# Prevention
This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.

Test! Test test test. Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

Status monitoring. Enable some uptime-monitoring service such as UptimeRobot to alert instantly upon outage of the website.

Note that in response to this error, I wrote a Puppet manifest 0-strace_is_your_friend.pp to automate fixing of any such identitical errors should they occur in the future. The manifest compares some filenames with the expected filename and replaces the closest fitting filenames with the correct ones(only where the expected filename doesn't exist in that directory.

But of course, this situation won't repeat itself because we are smart programmers, and we never make errorse. right?
