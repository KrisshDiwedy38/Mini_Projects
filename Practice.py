#Project 3: URL Shortener Develop a simple URL shortener that takes a long URL as input and generates a shorter version. The program should also be able to redirect the short URL to the original long URL.

def shortening_url(url):
   url_parts = url.split("/")
   for i in url_parts:
      

# def url_storing(og_url,short_url):
#    urls = {}
#    urls[short_url] = og_url
#    return urls

def main(og_url):
   short_url = shortening_url(og_url)
   # urls = url_storing(og_url, short_url)
   print(short_url)

if __name__ == "__main__":
   original_url = input("Enter the url: ")
   main(original_url)