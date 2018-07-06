API_KEY = "blah-blah-but-actually-not-secret" # pragma: whitelist secret

def main():
    print('hello world')
    print(API_KEY)

main()