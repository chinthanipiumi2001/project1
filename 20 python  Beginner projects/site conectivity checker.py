import urllib.request as urllib

def main (url):
    print("checking connectivity ")

    response = urllib.urlopen(url)
    print("connected to ",url, "successfully")
    print("The responce code was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)
