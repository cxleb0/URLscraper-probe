NOTE: INITIAL IDEA FOR THIS SCRIPT CAME FROM RYAN JOHNS YOUTUBE COURSE ON PYTHON FOR HACKERS BUT THE MODIFICATIONS THAT WERE MADE WERE MY OWN IDEAS.
This Python script is designed to scrape URLs containing a specified keyword from a webpage and validate these URLs by sending a HEAD request to each URL. Only the validated URLs are then saved to a text file.

Libraries Used:

requests: For sending HTTP requests to URLs.
BeautifulSoup: For parsing HTML content.
urljoin: For constructing complete URLs.
Global Variables:

visited_urls: A set to store visited URLs to avoid revisiting them.
count: A counter to keep track of the number of URLs found.
Function: spider_urls(url, keyword, max_urls)

Input:
url: The URL of the webpage to scrape.
keyword: The keyword to search for in the URLs.
max_urls: The maximum number of URLs to scrape.
Output: A list of tuples containing the found URLs and a boolean indicating if they have been validated (initially set to False).
Description:
Sends a GET request to the specified URL.
Parses the HTML content using BeautifulSoup to extract all 'a' tags.
Iterates over the extracted URLs:
Marks each URL as visited.
Constructs the complete URL using urljoin.
Checks if the keyword is present in the URL and adds it to the list of found URLs.
Recursively calls the function for the found URL if the maximum number of URLs has not been reached.
Returns the list of found URLs.
Function: main()

Description:
Prompts the user to input the URL, keyword, and maximum number of URLs.
Calls the spider_urls function to scrape URLs containing the keyword.
Validates the found URLs by sending a HEAD request and filters out the valid URLs.
Saves the validated URLs to a text file.
Prints a confirmation message.
Execution:

Checks if the script is being run directly (__name__ == "__main__") and calls the main() function.
Example Usage:

Enter the URL you want to scrape: https://example.com
Enter the keyword you want to search for: example
Enter the maximum amount of URLs you want from the scrape: 10
The script will scrape the specified webpage for URLs containing the keyword example, validate them, and save the validated URLs to a text file filtered_urls.txt.
