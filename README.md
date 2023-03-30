
# Command-line Web Browser

CLI Browser is a Python-based command-line interface that allows users to browse the web using HTTP requests and responses. The program uses the 
socket
 module to establish a connection with an HTTP server and send requests for web pages. The program also includes a simple HTTP server that serves files from the local directory and returns a list of links found in the requested file.

The program uses the 
urllib
 module to read the content of web pages and the 
re
 module to extract links from the HTML response body. The program also includes functionality for searching Wikipedia and saving bookmarks.

CLI Browser is designed to be simple and lightweight, with a minimal user interface that allows users to navigate the web using a set of intuitive commands. The program is intended for use by developers and other technical users who prefer to work with command-line interfaces rather than graphical user interfaces.


## Tech used

 CLI Browser is a Python-based command-line interface that uses several technologies to enable web browsing functionality. Here are the main technologies used in CLI Browser:

#### Python:
 CLI Browser is written in Python, a high-level programming language that is widely used for web development, data analysis, and scientific computing.

#### Socket Programming:
 CLI Browser uses the 
socket
 module in Python to establish a connection with an HTTP server and send requests for web pages.

#### HTTP Protocol:
 CLI Browser uses the HTTP protocol to communicate with web servers and fetch web pages. The program sends HTTP requests to web servers and receives HTTP responses containing the content of web pages.

#### HTML Parsing:
 CLI Browser uses the 
urllib
 module in Python to read the content of web pages and the 
re
 module to extract links from the HTML response body.

#### Wikipedia API:
 CLI Browser uses the Wikipedia API to search for content on Wikipedia and retrieve search results.

#### JSON Parsing:
 CLI Browser uses the 
json
 module in Python to parse JSON data returned by the Wikipedia API.

#### File I/O:
 CLI Browser uses file I/O operations to save and load bookmarks. The program stores bookmarks in a JSON file and reads the file when bookmarks are requested.

Overall, CLI Browser is a simple and lightweight program that uses a combination of Python modules and web technologies to provide a command-line interface for web browsing.
## Installation



```bash
  git clone https://github.com/pannagkumaar/cli-web-browser
  cd cli-web-browser

```

## Start the server and client codes 
```bash
  python3 client.py
```
This should start the CLI Browser and display a welcome message
```bash
  python3 server.py
```
This will start the server and make it available at http://localhost:8000/. The server serves files from the local directory and returns a list of links found in the requested file.


    
## About

You can then enter a URL to fetch, or use one of the available commands to navigate the web(make sure to use the address in the form of http://xxxxxx.com )

HTTP Server CLI Browser requires an HTTP server to fetch web pages. 

The options available are  
 Enter a link number to follow  
'b' to go back  
'f' to go forward  
'v' to view source code  
's' to search   
'h' to view history  
'm' to add a bookmark  
'l' to view bookmarks  
'q' to quit

#### Searching :
Searching You can search for content on Wikipedia using the 's' command. Enter a search query and CLI Browser will display a list of search results. You can then follow a link to view the corresponding Wikipedia page.

#### Bookmarking :
Bookmarks You can save bookmarks using the 'm' command. Enter a name for the bookmark and CLI Browser will save the current URL with the specified name. You can view your bookmarks using the 'l' command.

