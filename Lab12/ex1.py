#open a url and print some content from it fromt te omstamces of tje title tag
import urllib.request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
encoding = 'utf-8'
#Open the webpage

print(f"Opening {url}...")
webpage = urllib.request.urlopen(url)

#itterate through each line in the webpage and search for <title> tag
for line in webpage:
    line = line.decode(encoding)
    if '<label>' in line:
        print(line)


