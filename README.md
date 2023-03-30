# cli-web-browser
CLI Browser
CLI Browser is a simple command-line interface for browsing the web. It allows you to fetch and view web pages, follow links, search for content, and save bookmarks.

CLI Browser Screenshot

Installation
To use CLI Browser, you need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can download the CLI Browser code from this repository.

Usage
To start the CLI Browser, run the 
client.py
 file in your terminal:

python client.py
This will start the CLI Browser and display a welcome message. You can then enter a URL to fetch, or use one of the available commands to navigate the web:

Enter a link number to follow
'b' to go back
'f' to go forward
'v' to view source code
's' to search
'h' to view history
'm' to add a bookmark
'l' to view bookmarks
'q' to quit
Following Links
When you enter a URL to fetch, CLI Browser will display the headers and content of the page, as well as a list of links found in the page. You can follow a link by entering its number, or go back or forward in your browsing history using the 'b' and 'f' commands.

Searching
You can search for content on Wikipedia using the 's' command. Enter a search query and CLI Browser will display a list of search results. You can then follow a link to view the corresponding Wikipedia page.

Bookmarks
You can save bookmarks using the 'm' command. Enter a name for the bookmark and CLI Browser will save the current URL with the specified name. You can view your bookmarks using the 'l' command.

HTTP Server
CLI Browser requires an HTTP server to fetch web pages. The server code is included in this repository as 
server.py
. To start the server, run the following command in your terminal:

python server.py
This will start the server and make it available at http://localhost:8000/. The server serves files from the local directory and returns a list of links found in the requested file.

License
CLI Browser is released under the MIT License. See LICENSE file for details.

