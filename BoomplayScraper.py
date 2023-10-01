import os
import requests
from bs4 import BeautifulSoup

class BoomplayScraper:
    def get_images(self, url: str):    

        request = requests.get(url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")

        song_container = soup.find("ul", class_="morePart_albums")

        images = []
        image_urls = song_container.find_all("div", class_="img hasToPlay_icon lazyImg")
        
        for image_url in image_urls:
            images.append(image_url['data-bgurl'])
            print(image_url['data-bgurl'])

        print("\n")
        return images
    
    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        return [image['src'] for image in content.findAll('img')]
    
    def download(self, url):
        response = requests.get(url)
        filename = url.split('/')[-1]
        
        if not os.path.exists("images/"):
            os.mkdir("images/")

        print('Downloading image %s from URL %s' % (filename, url))
        
        if response.status_code == 200:
            with open('./images/' + filename, 'wb') as image:
                for chunk in response.iter_content(chunk_size=128):
                    image.write(chunk)
    

    def run(self, artist_url: str):

        images = self.get_images(artist_url)
        
        for image in images:
            self.download(image)



if __name__ == "__main__":

    print("==================================================================================================================================================")
    print("$$$$$$$\\                                              $$\\                      $$$$$$\\                                                              ")
    print("$$  __$$\\                                             $$ |                    $$  __$$\\                                                            ")
    print("$$ |  $$ | $$$$$$\\   $$$$$$\\  $$$$$$\\$$$$\\   $$$$$$\\  $$ | $$$$$$\\  $$\\   $$\\ $$ /  \\__| $$$$$$$\\  $$$$$$\\  $$$$$$\\   $$$$$$\\   $$$$$$\\   $$$$$$\\  ")
    print("$$$$$$$\ |$$  __$$\\ $$  __$$\\ $$  _$$  _$$\\ $$  __$$\\ $$ | \\____$$\\ $$ |  $$ |\\$$$$$$\\  $$  _____|$$  __$$\\ \\____$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ ")
    print("$$  __$$\\ $$ /  $$ |$$ /  $$ |$$ / $$ / $$ |$$ /  $$ |$$ | $$$$$$$ |$$ |  $$ | \\____$$\\ $$ /      $$ |  \\__|$$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \\__|")
    print("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$\\   $$ |$$ |      $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |      ")
    print("$$$$$$$  |\\$$$$$$  |\\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |$$ |\\$$$$$$$ |\\$$$$$$$ |\\$$$$$$  |\\$$$$$$$\\ $$ |     \\$$$$$$$ |$$$$$$$  |\\$$$$$$\\ $$ |      ")
    print("\\_______/  \\______/  \\______/ \\__| \\__| \\__|$$  ____/ \\__| \\_______| \\____$$ | \\______/  \\_______|\\__|      \\_______|$$  ____/  \\_______|\\__|      ")
    print("                                            $$ |                    $$\\   $$ |                                       $$ |                          ")
    print("                                            $$ |                    \\$$$$$$  |                                       $$ |                          ")
    print("                                            \\__|                     \\______/                                        \\__|                          ")
    print("==================================================================================================================================================")


    url = input("Please enter artists url: ")
    scraper = BoomplayScraper()
    scraper.run(url)

    print ("\nSuccesfully downloaded all images.")
    print("=======================================================================================================================================================================")