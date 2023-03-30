
import urllib.parse
import urllib.request
import zlib
import html.parser
from colorama import Fore, Style
import json

ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.BLUE
SUCCESS_COLOR = Fore.GREEN
RESET_COLOR = Style.RESET_ALL

history = []

def print_error(message):
    print(ERROR_COLOR + message + RESET_COLOR)

def print_info(message):
    print(INFO_COLOR +  message + RESET_COLOR)

def print_success(message):
    print(SUCCESS_COLOR + message + RESET_COLOR)

class LinkParser(html.parser.HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    url = urllib.parse.urljoin(self.base_url, attr[1])
                    self.links.append(url)
def add_bookmark(url, name):
    with open('bookmarks.txt', 'a') as f:
        f.write(f"{url},{name}\n")
        
def get_response(url):
    """
    Sends a GET request to the specified URL and returns the headers, content, and links found in the content.
    """
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as res:
            headers = res.headers
            content = res.read()
            # Decompress the content using gzip compression, if applicable
            if headers.get('Content-Encoding') == 'gzip':
                content = zlib.decompress(content, 16+zlib.MAX_WBITS)
            content = content.decode(errors='ignore')
            # Extract links from the content
            parser = LinkParser(url)
            parser.feed(content)
            links = parser.links
            return headers, content, links
    except Exception as e:
        print(f"\nAn error occurred while trying to fetch {url}: {e}")
        return None, None, []

def print_links(links):
    """
    Prints the list of links with their respective indices.
    """
    if links:
        print_success(Fore.BLUE + "Links found:\n" + Style.RESET_ALL)
        for i, link in enumerate(links):
            print(Fore.GREEN + f"{i}. " + Style.RESET_ALL +Fore.BLUE+ link+Style.RESET_ALL)
    else:
        print_info("\nNo links found in the page.")

def format_search_result(result):
    """
    Formats a search result into a string for display.
    """
    output = f"\nSearch results for '{result['query']}':\n"
    if result['results']:
        for i, r in enumerate(result['results']):
            output += f"\n{i+1}. {r['title']}\n{r['link']}\n"
    else:
        output += f"\nNo results found for '{result['query']}'.\n"
    return output
def get_bookmarks():
    with open('bookmarks.txt', 'r') as f:
        bookmarks = f.readlines()
    return [tuple(bookmark.strip().split(',')) for bookmark in bookmarks]

def search(query):
    """
    Searches for the specified query on the Wikipedia API and returns a list of page titles and links.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={query}"
    headers, content, _ = get_response(url)
    if not headers or not content:
        print_error(f"\nUnable to fetch search results for {query}. Please try again.")
        return None
    results = json.loads(content)
    titles = results[1]
    links = results[3]
    if not titles:
        print_info(f"\nNo search results found for {query}.")
        return None
    # Format the search results into a dictionary
    output = {
        'query': query,
        'results': [{'title': title, 'link': link} for title, link in zip(titles, links)]
    }
    return output

# def main():
#     print("Welcome to the CLI Browser!")
#     all_links = []  # Initialize the list of all links
#     history = []  # Initialize the history list
#     current_pos = -1  # Initialize the current position in the history list
#     while True:
#         url = input("\nEnter the URL to fetch (or 'q' to quit): ")
#         if url.lower() == 'q':
#             return
#         headers, content, links = get_response(url)
#         if not headers or not content:
#             print_error(f"\nUnable to fetch {url}. Please check the URL and try again.")
#             continue

#         # Add the links to the list of all links
#         all_links.append(links)

#         print(f"\nHeaders for {url}:\n")
#         print(headers)

#         print(f"\nContent for {url}:\n")
#         print(content[:500])

#         print_links(links)

#         # Add the links for the current page to the history list
#         history.append(links)
#         # Update the current position in the history list
#         current_pos += 1

#         while True:
#             choice = input("\nEnter link number to follow, 'b' to go back, 'f' to go forward, 'v' to view source code, 's' to search, 'h' to view history, or 'q' to quit: ")
#             if choice == 'q':
#                 return
#             elif choice == 'b':
#                 if current_pos > 0:
#                     # Decrement the current position in the history list
#                     current_pos -= 1
#                     # Get the links from the previous page
#                     links = history[current_pos]
#                     print_links(links)
#                 else:
#                     print_info("\nYou are already at the first page.")
#             elif choice == 'f':
#                 if current_pos < len(history) - 1:
#                     # Increment the current position in the history list
#                     current_pos += 1
#                     # Get the links from the next page
#                     links = history[current_pos]
#                     print_links(links)
#                 else:
#                     print_info("\nYou are already at the last page.")
#             elif choice == 'v':
#                 print(f"\nSource code for {url}:\n")
#                 print(content)
#             elif choice == 's':
#                 query = input("\nEnter the search query: ")
#                 result = search(query)
#                 if result:
#                     print(format_search_result(result))
#             elif choice == 'm':
#                 name = input("\nEnter a name for the bookmark: ")
#                 add_bookmark(url, name)
#                 print_success(f"\nBookmark '{name}' added for {url}")        
#             elif choice == 'h':
#                 if history:
#                     print_success(Fore.BLUE + "History:\n" + Style.RESET_ALL)
#                     for i, url in enumerate(history):
#                         print(Fore.GREEN + f"{i}. " + Style.RESET_ALL +Fore.BLUE+ url[0]+Style.RESET_ALL)
#                 else:
#                     print_info("\nNo history yet.")
#             else:
#                 try:
#                     choice = int(choice)
#                     url = links[choice]
#                     print_success(f"\nFollowing link {choice}: {url}")
#                     headers, content, links = get_response(url)
#                     print_links(links)
#                     # Add the links for the current page to the history list
#                     history.append(links)
#                     # Update the current position in the history list
#                     current_pos += 1
#                     # Add the links to the list of all links
#                     all_links.append(links)
#                 except (ValueError, IndexError):
#                     print_error("\nInvalid choice. Please try again.")
def main():
    print("Welcome to the CLI Browser!")
    all_links = []  # Initialize the list of all links
    history = []  # Initialize the history list
    current_pos = -1  # Initialize the current position in the history list
    while True:
        url = input("\nEnter the URL to fetch (or 'q' to quit): ")
        if url.lower() == 'q':
            return
        headers, content, links = get_response(url)
        if not headers or not content:
            print_error(f"\nUnable to fetch {url}. Please check the URL and try again.")
            continue

        # Add the links to the list of all links
        all_links.append(links)

        print(f"\nHeaders for {url}:\n")
        print(headers)

        print(f"\nContent for {url}:\n")
        print(content[:500])

        print_links(links)

        # Add the links for the current page to the history list
        history.append(links)
        # Update the current position in the history list
        current_pos += 1

        while True:
            choice = input("\nEnter link number to follow, 'b' to go back, 'f' to go forward, 'v' to view source code, 's' to search, 'h' to view history,'m' to add a bookmark,'l' to view bookmarks or 'q' to quit: ")
            if choice == 'q':
                return
            elif choice == 'b':
                if current_pos > 0:
                    # Decrement the current position in the history list
                    current_pos -= 1
                    # Get the links from the previous page
                    links = history[current_pos]
                    print_links(links)
                else:
                    print_info("\nYou are already at the first page.")
            elif choice == 'f':
                if current_pos < len(history) - 1:
                    # Increment the current position in the history list
                    current_pos += 1
                    # Get the links from the next page
                    links = history[current_pos]
                    print_links(links)
                else:
                    print_info("\nYou are already at the last page.")
            elif choice == 'v':
                print(f"\nSource code for {url}:\n")
                print(content)
            elif choice == 's':
                query = input("\nEnter the search query: ")
                result = search(query)
                if result:
                    print(format_search_result(result))
            elif choice == 'm':
                name = input("\nEnter a name for the bookmark: ")
                add_bookmark(url, name)
                print_success(f"\nBookmark '{name}' added for {url}")        
            elif choice == 'h':
                if history:
                    print_success(Fore.BLUE + "History:\n" + Style.RESET_ALL)
                    for i, url in enumerate(history):
                        print(Fore.GREEN + f"{i}. " + Style.RESET_ALL +Fore.BLUE+ url[0]+Style.RESET_ALL)
                else:
                    print_info("\nNo history yet.")
            elif choice == 'l':
                bookmarks = get_bookmarks()
                if bookmarks:
                    print_success(Fore.BLUE + "Bookmarks:\n" + Style.RESET_ALL)
                    for i, bookmark in enumerate(bookmarks):
                        print(Fore.GREEN + f"{i+1}. " + Style.RESET_ALL +Fore.BLUE+ f"{bookmark[1]}: {bookmark[0]}"+Style.RESET_ALL)
                else:
                    print_info("\nNo bookmarks yet.")
            else:
                try:
                    choice = int(choice)
                    url = links[choice]
                    print_success(f"\nFollowing link {choice}: {url}")
                    headers, content, links = get_response(url)
                    print_links(links)
                    # Add the links for the current page to the history list
                    history.append(links)
                    # Update the current position in the history list
                    current_pos += 1
                    # Add the links to the list of all links
                    all_links.append(links)
                except (ValueError, IndexError):
                    print_error("\nInvalid choice. Please try again.")                    
if __name__ == '__main__':
        main()