from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('/Users/jamescheung/chromedriver')
import datetime
now = datetime.datetime.now()


def Scrape_Health_Affairs():
    url = 'https://www.healthaffairs.org/blog'
    driver.maximize_window()
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')
    
    for link in soup.select('h4[class=featuredCard__title] > a'):
        Link.append('https://www.healthaffairs.org'+link['href'])
        Title.append(link.get_text())

    return(Title,Link,url)

def Scrape_Healthcare_Dive():
    url = 'https://www.healthcaredive.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('section[class=top-stories] a'):
        Link.append('https://www.healthcaredive.com'+link['href'])
        Title.append(link.get_text().strip('\n                                                    '))
    return(Title,Link,url)

def Scrape_Politico():
    url = 'https://www.politico.com/health-care'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('div[class=summary] > header > h3 > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
    Spliced_Link = Link[1:6]
    Spliced_Title = Title[1:6]
    return(Spliced_Title, Spliced_Link,url)

def Scrape_Vox():
    url = 'https://www.vox.com/health-care'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('h2[class=c-entry-box--compact__title] > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
    Spliced_Link = Link[2:7]
    Spliced_Title = Title[2:7]
    return(Spliced_Title,Spliced_Link,url)

def Scrape_NEJM_Catalyst():
    url = 'https://catalyst.nejm.org/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.find_all('a', class_='txt__link post__h-link'):
        Link.append(link['href'])
        Title.append(link.get_text())
    Spliced_Title = Title[1:6]
    Spliced_Link = Link[1:6]
    return(Spliced_Title, Spliced_Link,url)

def Scrape_Beckers():
    url = 'https://www.beckershospitalreview.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('h2[class=article-title] > a'):
        Link.append('https://www.beckershospitalreview.com'+link['href'])
        Title.append(link.get_text())

    Spliced_Link = Link[:10:2]
    Spliced_Title = Title[:10:2]
    return(Spliced_Title, Spliced_Link,url)

def Scrape_Modern():
    url = 'https://www.modernhealthcare.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('article > h2 > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
    return(Title,Link,url)

def Scrape_KHN():
    url = 'https://khn.org/stories/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('p[class=headline] > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
    Spliced_Title = Title[0:5]
    Spliced_Link = Link[0:5]
    return(Spliced_Title, Spliced_Link,url)

def Scrape_JAMA():
    url = 'https://newsatjama.jama.com/category/the-jama-forum/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('h2[class=posttitle] > a[class=dark]'):
        Link.append(link['href'])
        Title.append(link.get_text())
    Spliced_Link = Link[0:5]
    Spliced_Title = Title[0:5]
    return(Spliced_Title, Spliced_Link,url)

def Scrape_Fierce():
    url = 'https://www.fiercebiotech.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('h3[class=list-title] > a'):
        Link.append('https://www.fiercebiotech.com'+link['href'])
        Title.append(link.get_text())
    return(Title,Link,url)

def Scrape_Biospace():
    url = 'https://www.biospace.com/news/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')

    for link in soup.select('h3[class=lister__header] > a'):
        Link.append('https://www.biospace.com'+link['href'])
        Title.append(link.get_text())
        Spliced_Link = Link[0:5]
        Spliced_Title = Title[0:5]
    return(Spliced_Title, Spliced_Link, url)

def Scrape_Fox():
    url = 'https://www.foxnews.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')
    
    for link in soup.select('main[class=main-content] h2[class=title] > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
        Spliced_Link= Link[0:5]
        Spliced_Title = Title[0:5]
    return(Spliced_Title, Spliced_Link,url)

def Scrape_MSNBC():
    url ='https://www.nbcnews.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')
    
    for link in soup.select('h2[class=title___2T5qK] > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
        Spliced_Title = Title[0:8]
        Spliced_Link = Link[0:8]
    return(Spliced_Title,Spliced_Link,url)

def Scrape_CNN():
    url = 'https://www.cnn.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')
    
    for link in soup.select('h3[class=cd__headline] > a'):
        Link.append(link['href'])
        Title.append(link.get_text())
        Spliced_Title = Title[8:15]
        Spliced_Link = Link[8:15]
    return(Spliced_Title,Spliced_Link,url)

def HTML_Writer(Text,Name):
    Title = Text[0]
    Link = Text[1]
    url = Text[2]

    title_list = []
    for i in range(len(Title)):
        title_list.append('title'+str([i+1]))
    title_dict = dict(zip(title_list, Title))
    
    link_list = []
    for i in range(len(Link)):
        link_list.append('link'+str([i+1]))
    link_dict = dict(zip(link_list,Link))
    
    title_html = []
    for i in range(len(Title)):
        title_html.append("""<h3><a class='link' href='"""+str(link_dict[link_list[i]])+"""'>"""+str(title_dict[title_list[i]]+"</a></h3>"))

    body_html = ""
    for i in range(len(Title)):
        body_html += title_html[i]        
    head = """
    <!DOCTYPE html>
        <html>
        <head>
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <style>
            @media only screen and (min-width:601px){
                .all {
                padding-left: 30%;
                padding-right: 30%;
                }
            }

            @media only screen and (max-width: 600px) {
                .all {
                padding-left: 5%;
                padding-right: 5%;
                }
            }

            body {
            margin-bottom:20%;
            
            }
            h1 {
            text-align: center;
   
            }
            a {
            color: black;
            text-decoration: none;
            }

            .topnav {
              background-color: #333;
              overflow: hidden;
            }

            .topnav a {
              float: left;
              color: #f2f2f2;
              text-align: center;
              padding: 14px 16px;
              text-decoration: none;
              font-size: 17px;
            }

            .topnav a:hover {
              background-color: #ddd;
              color: black;
            }

            .link:hover {
            color: blue;

            }

        </style>
        <title>HEALTH SUMMARIES</title>
        </head>
        <body>
        <div class = 'topnav'>
        <a class='active' href='/'> Front Page</a>
        <a href="/news">News</a>
        <a href="/health">Health</a>
        <a href="/pharma">Pharma</a>
        </div>
        <div class='all'>"""
    name = """<h1><a href='"""+str(url)+"""'>""" +str(Name)+ """</a></h1>"""
    date = "<h4>"+now.strftime("%Y-%m-%d %H:%M")+"</h4>"
    tail = """</div></body>
        </html>"""
    return(head,name,date,body_html,tail)

Health_Affairs = Scrape_Health_Affairs()
Healthcare_Dive = Scrape_Healthcare_Dive()
Politico = Scrape_Politico()
Vox = Scrape_Vox()
NEJM_Catalyst = Scrape_NEJM_Catalyst()
Beckers = Scrape_Beckers()
Modern = Scrape_Modern()
KHN = Scrape_KHN()
JAMA = Scrape_JAMA()
Fierce = Scrape_Fierce()
Biospace = Scrape_Biospace()
Fox = Scrape_Fox()
MSNBC = Scrape_MSNBC()
CNN = Scrape_CNN()



def Health_Combinator():
    Page_Health_Affairs = HTML_Writer(Health_Affairs,'Health Affairs')
    Page_Healthcare_Dive = HTML_Writer(Healthcare_Dive,'Healthcare Dive') 
    Page_Politico = HTML_Writer(Politico, 'Politico')
    Page_Vox = HTML_Writer(Vox, 'Vox')
    Page_Catalyst = HTML_Writer(NEJM_Catalyst, "NEJM Catalyst")
    Page_Beckers = HTML_Writer(Beckers, "Becker's Hospital Review")
    Page_Modern = HTML_Writer(Modern, "Modern Healthcare")
    Page_KHN = HTML_Writer(KHN, 'Kaiser Health News')
    Page_JAMA = HTML_Writer(JAMA, 'JAMA Forum')
    Page = Page_Health_Affairs[0] + Page_Health_Affairs[2]+Page_Health_Affairs[1] + Page_Health_Affairs[3]+"<br>"+Page_Healthcare_Dive[1]+Page_Healthcare_Dive[3]+"<br>"+Page_Politico[1]+Page_Politico[3]+"<br>"+Page_Vox[1]+Page_Vox[3]+"<br>"+Page_Catalyst[1]+Page_Catalyst[3]+"<br>"+Page_Beckers[1]+Page_Beckers[3]+"<br>"+Page_Modern[1]+Page_Modern[3]+"<br>"+Page_KHN[1]+Page_KHN[3]+"<br>"+Page_JAMA[1]+Page_JAMA[3]+Page_JAMA[4]
    return(Page)

def Pharma_Combinator():
    Page_Fierce = HTML_Writer(Fierce, 'Fierce Biotech')
    Page_Biospace = HTML_Writer(Biospace, 'BioSpace')
    Page = Page_Fierce[0]+Page_Fierce[2]+Page_Fierce[1]+Page_Fierce[3]+'<br>'+Page_Biospace[1]+Page_Biospace[3]+Page_Biospace[4]
    return(Page)

def News_Combinator():
    Page_Fox = HTML_Writer(Fox, "Fox News")
    Page_MSNBC = HTML_Writer(MSNBC, 'MSNBC')
    Page_CNN = HTML_Writer(CNN, 'CNN')
    Page = Page_Fox[0]+Page_Fox[2]+Page_Fox[1]+Page_Fox[3]+'<br>'+Page_MSNBC[1]+Page_MSNBC[3]+'<br>'+Page_CNN[1]+Page_CNN[3]+Page_CNN[4]
    return(Page)

def HTML_Saver(Page,Name):
    File_Name = 'NewsSummaries_'+str(Name)+'.html'
    HTML = open(File_Name, 'wb')
    HTML.write(Page.encode('utf-8'))
    HTML.close()
    # driver.get('file:///Users/jamescheung/'+File_Name)

Page_Health = Health_Combinator()
HTML_Saver(Page_Health,'Health') 
Page_Pharma = Pharma_Combinator()
HTML_Saver(Page_Pharma,'Pharma')
Page_News = News_Combinator()
HTML_Saver(Page_News,'News')



