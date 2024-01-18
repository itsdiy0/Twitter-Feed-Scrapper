from libs.tweet_puller import puller

def main():
    #enter the duration you want 
    duration = 60
    #enter desired username
    username = ""
    #enter password
    password = ""
    #enter the address of your proxy list file
    proxy_list_file_address = ""
    puller(duration=duration,username=username,password=password)

if __name__ == "__main__":
    main()
