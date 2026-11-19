from tools import check_url_blocklist

url=input("Enter the url: ")

result = check_url_blocklist(url)

print(result)