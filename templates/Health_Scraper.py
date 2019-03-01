from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('/Users/jamescheung/chromedriver')
import datetime
now = datetime.datetime.now()
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from nltk.stem import WordNetLemmatizer
import heapq  
from textblob import TextBlob

def Summarizer(article_text):
    if article_text == "":
        return ""
    else:
        # Removing Square Brackets and Extra Spaces
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
        article_text = re.sub(r'\s+', ' ', article_text)

        # Removing special characters and digits
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text) 
        
        lemma = WordNetLemmatizer()
        formatted_article_text = lemma.lemmatize(formatted_article_text)
        
        clean_list = []
        sentence_list = TextBlob(article_text).sentences
        for sent in sentence_list:
            clean_list.append(str(sent))
            
        stopwords = nltk.corpus.stopwords.words('english')

        word_frequencies = {}  
        for word in word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word.lower()] = 1
                else:
                    word_frequencies[word.lower()] += 1

        maximum_frequency = max(word_frequencies.values())
        max_keys = [k for k, v in word_frequencies.items() if v == maximum_frequency]

        for word in word_frequencies.keys():  
            word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

        sentence_scores = {}  
        for sent in clean_list:  
            for word in TextBlob(formatted_article_text).words:
                if word in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
        
        summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
        if len(' '.join(summary_sentences)) > 1000:
            summary_sentences = heapq.nlargest(4, sentence_scores, key=sentence_scores.get)
        max_keys = heapq.nlargest(10, word_frequencies, key=word_frequencies.get)
        for x in max_keys:
            if x.isalpha():
                Max = x
                break
        summary = ' '.join(summary_sentences)
        return(summary,Max) 


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

def Get_Text_Politico(Link_List):
    Link_Catalyst = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_Catalyst:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('p')
        for p in all_ps[1:-3]:
            article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

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

def Get_Text_Catalyst(Link_List):
    Link_Catalyst = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_Catalyst:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('section[class=article__content] p')
        for p in all_ps:
            article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

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
        Link.append('https://www.modernhealthcare.com'+link['href'])
        Title.append(link.get_text())
    return(Title,Link,url)

def Get_Text_Modern(Link_List):
    driver.get('https://home.modernhealthcare.com/clickshare/forceLogin.do?CSAuthReq=1&CSTargetURL=https%3A//www.modernhealthcare.com/home-0')
    driver.find_element_by_id('username').send_keys('research@hmacademy.com')
    driver.find_element_by_id('password').send_keys('Academy1')
    driver.find_element_by_id('login-submit').click()
    Link_Modern = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_Modern:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('p')
        for p in all_ps:
            article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

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

def Get_Text_Fierce(Link_List):
    Link_Catalyst = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_Catalyst:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('p')
        for p in all_ps:
            article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

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

def Get_Text_Biospace(Link_List):
    Link_Biospace = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_Biospace:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('p')
        for p in all_ps[2:]:
            article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

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

def Get_Text_Fox(Link_List):
    Link_Fox = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_Fox:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('div[class=article-body] p')
        for p in all_ps[1:]:
            if p.get_text().isupper():
                Strong.append(p)
            else:
                article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

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

def Get_Text_MSNBC(Link_List):
    Link_MSNBC = Link_List[1]
    Articles = []
    Strong = []
    for article in Link_MSNBC:
        driver.get(article)
        driver.implicitly_wait(30)
        html1 = driver.page_source
        soup1 = BeautifulSoup(html1, 'lxml')
        article_text = ""
        all_ps = soup1.select('p')
        for p in all_ps[:-1]:
            article_text += p.get_text() + ' '
        Articles.append(article_text)
    return(Articles)

def Scrape_CNN():
    url = 'https://www.cnn.com/'
    driver.get(url)
    html = driver.page_source
    Link = []
    Title = []
    soup = BeautifulSoup(html, 'lxml')
    
    for link in soup.select('h3[class=cd__headline] > a'):
        Link.append('https://www.cnn.com'+link['href'])
        Title.append(link.get_text())
        Spliced_Title = Title[8:15]
        Spliced_Link = Link[8:15]
    return(Spliced_Title,Spliced_Link,url)

def HTML_Writer(Text,Name,id):
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
    padding-left: 25%;
    padding-right: 25%;
    
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

h3 {
    text-align: center;
}

a {
  color: black;
  text-decoration: none;
}


.link:hover {
  color: blue;
}
/* Navbar container */
.navbar {
  overflow: hidden;
  background-color: #333;
  font-family: Arial;
}

/* Links inside the navbar */
.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* The dropdown container */
.dropdown {
  float: left;
  overflow: hidden;
}

/* Dropdown button */
.dropdown .dropbtn {
  font-size: 16px; 
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit; /* Important for vertical align on mobile phones */
  margin: 0; /* Important for vertical align on mobile phones */
}

/* Add a red background color to navbar links on hover */
.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

/* Dropdown content (hidden by default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}
        </style>
        <title>HEALTH SUMMARIES</title>
        </head>
        <body>
   <div class="navbar">
   <div class="navbar">
    <div class="dropdown">
    <button class="dropbtn"><a href="/">Home
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
        </div>
  </div> 

  <div class="dropdown">
    <button class="dropbtn"><a href="/news">General News 
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
      <a href ="/news#Fox">Fox</a>
      <a href="/news#MSNBC">MSNBC</a>
      <a href="/news#CNN">CNN</a>
    </div>
  </div> 
  
  <div class="dropdown">
    <button class="dropbtn"><a href='/health'>Health Care News
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
      <a href ="/health#NEJM">NEJM Catalyst</a>
      <a href="/health#MHealthcare">Modern Healthcare</a>
      <a href="/health#Politico">Politico</a>
      <a href="/health#Vox">Vox</a>
      <a href="/health#HAffairs">Health Affairs</a>
      <a href="/health#Beckers">Becker's Hospital Review</a>
      <a href="/health#HDive">Healthcare Dive</a>
      <a href="/health#Kaiser">Kaiser Health News</a>
      <a href="/health#JAMA">JAMA Forum</a>
    </div>
  </div> 

  <div class="dropdown">
    <button class="dropbtn"><a href="/pharma">Pharma News 
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
      <a href ="/pharma#Fierce">Fierce Biotech</a>
      <a href="/pharma#BioSpace">BioSpace</a>

    </div>
  </div> 
</div>
        </div>

        </div>
        <div class='all'>"""
    name = """<h1 id="""+str(id)+"""><a href='"""+str(url)+"""'>""" +str(Name)+ """</a></h1>"""
    date = "<h4>"+now.strftime("%Y-%m-%d %H:%M")+"</h4>"
    tail = """</div></body>
        </html>"""
    return(head,name,date,body_html,tail)

def Summary_Writer(Text,Name,Article_List,id):
    Title = Text[0]
    Link = Text[1]
    url = Text[2]
    Articles = Article_List

    article_list = []
    for i in range(len(Articles)):
        article_list.append('article'+str([i+1]))
    article_dict = dict(zip(article_list,Articles))

    article_html = []
    for i in range(len(Articles)):
        article_html.append("<p>"+str(Summarizer(article_dict[article_list[i]])[0]+"</p>"))

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
        body_html += title_html[i] + article_html[i] + "<br>"       
    head = """
    <!DOCTYPE html>
        <html>
        <head>
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <style>




@media only screen and (min-width:601px){
  .all {
    padding-left: 25%;
    padding-right: 25%;
    
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

h3 {
    text-align: center;
}

a {
  color: black;
  text-decoration: none;
}


.link:hover {
  color: blue;
}
/* Navbar container */
.navbar {
  overflow: hidden;
  background-color: #333;
  font-family: Arial;
}

/* Links inside the navbar */
.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* The dropdown container */
.dropdown {
  float: left;
  overflow: hidden;
}

/* Dropdown button */
.dropdown .dropbtn {
  font-size: 16px; 
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit; /* Important for vertical align on mobile phones */
  margin: 0; /* Important for vertical align on mobile phones */
}

/* Add a red background color to navbar links on hover */
.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

/* Dropdown content (hidden by default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}
                </style>
        <title>HEALTH SUMMARIES</title>
        </head>
        <body>
   <div class="navbar">
<div class="navbar">
    <div class="dropdown">
    <button class="dropbtn"><a href="/">Home
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
        </div>
  </div> 
  
  <div class="dropdown">
    <button class="dropbtn"><a href="/news">General News
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
      <a href ="/news#Fox">Fox</a>
      <a href="/news#MSNBC">MSNBC</a>
      <a href="/news#CNN">CNN</a>
    </div>
  </div> 

  <div class="dropdown">
    <button class="dropbtn"><a href='/health'>Health Care News 
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
      <a href ="/health#NEJM">NEJM Catalyst</a>
      <a href="/health#MHealthcare">Modern Healthcare</a>
      <a href="/health#Politico">Politico</a>
      <a href="/health#Vox">Vox</a>
      <a href="/health#HAffairs">Health Affairs</a>
      <a href="/health#Beckers">Becker's Hospital Review</a>
      <a href="/health#HDive">Healthcare Dive</a>
      <a href="/health#Kaiser">Kaiser Health News</a>
      <a href="/health#JAMA">JAMA Forum</a>
    </div>
  </div> 

  <div class="dropdown">
    <button class="dropbtn"><a href="/pharma">Pharma News
      <i class="fa fa-caret-down"></i>
    </a></button>
    <div class="dropdown-content">
      <a href ="/pharma#Fierce">Fierce Biotech</a>
      <a href="/pharma#BioSpace">BioSpace</a>

    </div>
  </div> 
</div>
        </div>

        </div>
        <div class='all'>"""
    name = """<h1 id="""+str(id)+"""><a href='"""+str(url)+"""'>""" +str(Name)+ """</a></h1>"""
    date = "<h4>"+now.strftime("%Y-%m-%d %H:%M")+"</h4>"
    tail = """</div></body>
        </html>"""
    return(head,name,date,body_html,tail)

Health_Affairs = Scrape_Health_Affairs()
Healthcare_Dive = Scrape_Healthcare_Dive()
Politico = Scrape_Politico()
Politico_Articles = Get_Text_Politico(Politico)
Vox = Scrape_Vox()
NEJM_Catalyst = Scrape_NEJM_Catalyst()
NEJM_Catalyst_Articles = Get_Text_Catalyst(NEJM_Catalyst)
Beckers = Scrape_Beckers()
Modern = Scrape_Modern()
Modern_Articles = Get_Text_Modern(Modern)
KHN = Scrape_KHN()
JAMA = Scrape_JAMA()
Fierce = Scrape_Fierce()
Fierce_Articles = Get_Text_Fierce(Fierce)
Biospace = Scrape_Biospace()
Biospace_Articles = Get_Text_Biospace(Biospace)
Fox = Scrape_Fox()
Fox_Articles = Get_Text_Fox(Fox)
MSNBC = Scrape_MSNBC()
MSNBC_Articles = Get_Text_MSNBC(MSNBC)
CNN = Scrape_CNN()



def Health_Combinator():
    Page_Catalyst = Summary_Writer(NEJM_Catalyst, "NEJM Catalyst", NEJM_Catalyst_Articles,'NEJM')
    Page_Health_Affairs = HTML_Writer(Health_Affairs,'Health Affairs','HAffairs')
    Page_Healthcare_Dive = HTML_Writer(Healthcare_Dive,'Healthcare Dive','HDive') 
    Page_Politico = Summary_Writer(Politico, 'Politico',Politico_Articles, 'Politico')
    Page_Vox = HTML_Writer(Vox, 'Vox','Vox')
    
    Page_Beckers = HTML_Writer(Beckers, "Becker's Hospital Review","Beckers")
    Page_Modern = Summary_Writer(Modern, "Modern Healthcare", Modern_Articles,'MHealthcare')
    Page_KHN = HTML_Writer(KHN, 'Kaiser Health News','Kaiser')
    Page_JAMA = HTML_Writer(JAMA, 'JAMA Forum',"JAMA")
    Page = Page_Catalyst[0] + Page_Catalyst[2]+Page_Catalyst[1] + Page_Catalyst[3]+"<br>"+Page_Modern[1]+Page_Modern[3]+"<br>"+Page_Politico[1]+Page_Politico[3]+"<br>"+Page_Vox[1]+Page_Vox[3]+"<br>"+Page_Health_Affairs[1]+Page_Health_Affairs[3]+"<br>"+Page_Beckers[1]+Page_Beckers[3]+"<br>"+Page_Healthcare_Dive[1]+Page_Healthcare_Dive[3]+"<br>"+Page_KHN[1]+Page_KHN[3]+"<br>"+Page_JAMA[1]+Page_JAMA[3]+Page_JAMA[4]
    return(Page)

def Pharma_Combinator():
    Page_Fierce = Summary_Writer(Fierce, 'Fierce Biotech',Fierce_Articles,'Fierce')
    Page_Biospace = Summary_Writer(Biospace, 'BioSpace', Biospace_Articles, 'BioSpace')
    Page = Page_Fierce[0]+Page_Fierce[2]+Page_Fierce[1]+Page_Fierce[3]+'<br>'+Page_Biospace[1]+Page_Biospace[3]+Page_Biospace[4]
    return(Page)

def News_Combinator():
    Page_Fox = Summary_Writer(Fox, "Fox News", Fox_Articles, 'Fox')
    Page_MSNBC = Summary_Writer(MSNBC, 'MSNBC', MSNBC_Articles, 'MSNBC')
    Page_CNN = HTML_Writer(CNN, 'CNN','CNN')
    Page = Page_Fox[0]+Page_Fox[2]+Page_Fox[1]+Page_Fox[3]+'<br>'+Page_MSNBC[1]+Page_MSNBC[3]+'<br>'+Page_CNN[1]+Page_CNN[3]+Page_CNN[4]
    return(Page)

def HTML_Saver(Page,Name):
    File_Name = 'NewsSummaries_'+str(Name)+'.html'
    HTML = open(File_Name, 'wb')
    HTML.write(Page.encode('utf-8'))
    HTML.close()


Page_Health = Health_Combinator()
HTML_Saver(Page_Health,'Health') 
Page_Pharma = Pharma_Combinator()
HTML_Saver(Page_Pharma,'Pharma')
Page_News = News_Combinator()
HTML_Saver(Page_News,'News')
driver.quit()



