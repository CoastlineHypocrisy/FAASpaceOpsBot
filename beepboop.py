import os
import requests
from bs4 import BeautifulSoup

import post_to_twitter

# download the target page
faa_site = requests.get('https://www.fly.faa.gov/adv/adv_spt.jsp')

# parse the HTML content of the page
soup = BeautifulSoup(faa_site.content, 'html.parser')
find_text = soup.find('pre').get_text()

space_operation = find_text.find('SPACE OPERATION(S):') + 20
flight_check = find_text.find('FLIGHT CHECK:') - 5

with open('scratch.txt', 'w') as file:
    x = space_operation
    while space_operation <= x <= flight_check:
        file.write(find_text[x])
        x += 1

with open('scratch.txt', 'r') as file:
    with open('scratchier.txt', 'w') as new_file:
        for line in file.readlines():
            format_primary = 'PRIMARY:'
            format_backup1 = 'BACKUP(S):'
            format_backup2 = 'BACKUP:'
            remove_tab = line.replace('\t', '   ')
            if line.startswith(format_primary):
                new_file.write(remove_tab.replace(format_primary, '== PRIMARY ==\n   '))
            elif line.startswith(format_backup1):
                new_file.write((remove_tab.replace(format_backup1, '== BACKUP(S) ==\n   ')))
            elif line.startswith(format_backup2):
                new_file.write((remove_tab.replace(format_backup2, '== BACKUP(S) ==\n')))
            else:
                new_file.write(remove_tab)

os.remove('scratch.txt')

post_to_twitter.run()

os.remove('scratchier.txt')
