import UrlPuller
import os

puller_file = os.path.join(os.getcwd(), 'URLs', 'list.txt')
puller = UrlPuller.UrlPuller(puller_file)

for i in range(puller.get_size()):
    print(puller.get_url())
    puller.next_url()

