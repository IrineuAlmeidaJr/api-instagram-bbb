from bs4 import BeautifulSoup

import requests

from controllers import user_controller

#
# print(len(imgs))
#
# # #
# for img in imgs:
#     src = img.get("src")
#     if src:
#         # resolve any relative urls to absolute urls using base URL
#         src = requests.compat.urljoin(url, src)
#         print(">>", src)

user_controller.get_follower_history_brother("Rodriguinho")
