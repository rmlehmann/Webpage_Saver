import urllib.request, datetime

def main():
    url = input('\nInsert the url of the page you want to download:\n')
    fileName = input('\nWhat is the name you want this page to be saved as?\n')
    write_html_file(urlPage(url),fileName)
    print('\nDone :)')

def urlPage(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    content = str(resp.read())
    return content

def write_html_file(content,filename):
    file = open(filename+'.html','w')
    file.write(content)
    file.close


if __name__ == '__main__':
    try:
        main()
        
    except Exception as e:
        errorlog = open('error_log.txt','a')
        errorlog.write(str(datetime.datetime.now())+' : '+str(e)+'\n')
        errorlog.close()
        print('\nOops, something went wrong :(\nIf you want to know more see the error log')

    input('\nPress enter to exit\n')
