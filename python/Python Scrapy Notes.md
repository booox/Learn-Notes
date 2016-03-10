
# Install Scrapy
    `$ pip install scrapy`
    
# Scrapy Tutorial
## Creating a project
    `$ scrapy startproject tutorial`
    
        ```
        tutorial/
            scrapy.cfg            # deploy configuration file

            tutorial/             # project's Python module, you'll import your code from here
                __init__.py

                items.py          # project items file

                pipelines.py      # project pipelines file

                settings.py       # project settings file

                spiders/          # a directory where you'll later put your spiders
                    __init__.py
                    ...

        ```   
## Defining our Item

* *Items* are containers that will be loaded with the scraped data
* they work like simple Python dicts.
* They are declared by creating a *scrapy.Item* class and defining its attributes as *scrapy.Field* objects
* Edit *tutorial/items.py*  
    ```
    import scrapy

    class DmozItem(scrapy.Item):
        title = scrapy.Field()
        link = scrapy.Field()
        desc = scrapy.Field()
    
    ```
## Our first Spider

* Spiders are classes that you define and Scrapy uses to scrape information from a domain(or group of domains).
* They define an initial list of URLs to download, how to follow links, and how to parse the contents of pages to extract items.
* To create a Spider, you must subclass *scrapy.Spider* and define some attributes:
    * *name* : identifies the Spider. It must be unique.
    * *start_urls* : a list of URLs where the spider will begin to crawl from.
    * *parse()* : a method of the spider, which will be called with the downloaded *Response* object of each start URL.
        * The response is passed to the method as the first and only argument.
* Edit *tutorial/spiders/dmoz_spider.py* 
    ```
    import scrapy

    class DmozSpider(scrapy.Spider):
        name = "dmoz"
        allowed_domains = ["dmoz.org"]
        start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]

        def parse(self, response):
            filename = response.url.split("/")[-2] + '.html'
            with open(filename, 'wb') as f:
                f.write(response.body)    
        
    ```
    
### Crawling

* To put our spider to work, go to the project’s top level directory and run
    * `$ scrapy crawl dmoz`
    * `$ scrapy crawl dmoz -o items.json -t json`
* You should notice two new files have been created
    * *Books.html*
    * *Resources.html* 


### Extracting Items
#### Introduction to Selectors

* There are several ways to extract data from web pages. 
* Scrapy uses a mechanism based on [XPath](http://www.w3.org/TR/xpath) or [CSS](http://www.w3.org/TR/selectors) expressions called *Scrapy Selectors* .  
* XPath expressions examples
    * */html/head/title* : selects the <title> element
    * */html/head/title/text()* : selects the text inside <title> element.
    * *//td* : selects all the <td> elements
    * *//div[@class="mine"]* : selects all *div* elements which contain an attribute *class="mine"* 
    
* some tutorial to learn XPath
    * [ XPath 1.0 Tutorial](http://zvon.org/comp/r/tut-XPath_1.html)
    * [Concise XPath](http://plasmasturm.org/log/xpath101/)
    
* Selectors have four basic methods
    * *xpath()* : return a list of selectors, each of which represents the nodes selected by the xpath expressions given as argument.
    * *css()* :  return a list of selectors, each of which represents the nodes selected by the CSS expression given as argument.
    * *extract()* : returns a unicode string with the selected data. 
    * *re()* : returns a list of unicode strings extracted by applying the regular expression given as argument.

#### Trying Selectors in the Shell
* To illustrate the use of Selectors we're going to use the built-in *Scrapy shell* , which also requires [IPython](http://ipython.org/).
* To start a shell, you must go to the project's top level directory and run:
    * `scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"`
    
    
#### Extracting the data
* Edit *tutorial/spiders/dmoz_spider.py*     
    ```
    import scrapy

    class DmozSpider(scrapy.Spider):
        name = "dmoz"
        allowed_domains = ["dmoz.org"]
        start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]

        def parse(self, response):
            for sel in response.xpath('//ul/li'):
                title = sel.xpath('a/text()').extract()
                link = sel.xpath('a/@href').extract()
                desc = sel.xpath('text()').extract()
                print title, link, desc


    ```
* Run `$ scrapy crawl dmoz`
    * You'll see sites being printed in your output.

### Using our item
* *Item* objects are custom Python dicts
* You can access the values of their fields using the standard dict syntax like:
    ```
    >>> item = DmozItem()
    >>> item['title'] = 'Example title'
    >>> item['title']
    'Example title'
    
    ```
* Edit *tutorial/spiders/dmoz_spider.py*     
    ```
    # -*- coding: utf-8 -*-

    import scrapy

    from tutorial.items import DmozItem

    class DmozSpider(scrapy.Spider):
        name = "dmoz"
        allowed_domains = ["dmoz.org"]
        start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]
        
        def parse(self, response):
            # filename = response.url.split("/")[-2] + '.html'
            # with open(filename, 'wb') as f:
                # f.write(response.body)
            
            tag_wrap = response.xpath('//ul[@class="directory-url"]/li')
            for tag in tag_wrap:
                item = DmozItem()
                item['title'] = tag.xpath('a/text()').extract()
                item['link'] = tag.xpath('a/@href').extract()
                item['desc'] = tag.xpath('text()').extract()
                yield item
            
                
    ```

## Following links

* Now that you know how to extract data from a pages.
* Why not extract the links for the pages you are interested, follow them and then extract the data you want for all of them?

### Here is a modification to our spider that does just that:


    ```
    # -*- coding: utf-8 -*-

    import scrapy

    from tutorial.items import DmozItem

    class DmozSpider(scrapy.Spider):
        name = "dmoz"
        allowed_domains = ["dmoz.org"]
        start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        ]
        
        def parse(self, response):
        
            for href in response.css("ul.directory.dir-col > li > a:attr('href')"):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback = self.parse_dir_contents)
                
        def parse_dir_contents(self, response):        
            
            tag_wrap = response.xpath('//ul[@class="directory-url"]/li')
            for tag in tag_wrap:
                item = DmozItem()
                item['title'] = tag.xpath('a/text()').extract()
                item['link'] = tag.xpath('a/@href').extract()
                item['desc'] = tag.xpath('text()').extract()
                yield item
            
    
    ```

### callback method 
* A common pattern is a callback method that extracts some items, looks for a link to follow to the next page and then yields a Request with the same callback for it:

    ```
    def parse_articles_follow_next_page(self, response):
        for article in response.xpath("//article"):
            item = ArticleItem()

            ... extract article data here

            yield item

        next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_articles_follow_next_page)    
    ```
* This creates a sort of loop, following all the links to the next page until it doesn't find one
    * handy for crawling blogs, forums and other sites with pagination
    
### pass additional data to the callbacks

* Another common pattern is to build an item with data from more than one page, using a trick to pass additional data to the callbacks.


## Storing the scraped data

### using Feed exports

* The simplest way to store the scraped data is by using [Feed exports]() with the following command:
    * `$ scrapy crawl dmoz -o items.json`
    
    
    
# Request usage examples

## Using FormRequest to send data via HTTP POST

* If you want to simulate a HTML Form POST in your spider and send a couple of key-value fields
* you can return a *FormRequest* object (from your spider) like this:
* 
    ```
    
    return [FormRequest(url="http://www.example.com/post/action",
                    formdata={'name': 'John Doe', 'age': '27'},
                    callback=self.after_post)]
    ```
    
## Using FormRequest.from_response() to simulate a user login

* You can use the *FormRequest.from_response()* method for this job
* Here’s an example spider which uses it:
    ```
    import scrapy

    class LoginSpider(scrapy.Spider):
        name = 'example.com'
        start_urls = ['http://www.example.com/users/login.php']

        def parse(self, response):
            return scrapy.FormRequest.from_response(
                response,
                formdata={'username': 'john', 'password': 'secret'},
                callback=self.after_login
            )

        def after_login(self, response):
            # check login succeed before going on
            if "authentication failed" in response.body:
                self.logger.error("Login failed")
                return

            # continue scraping with authenticated session...
    
    
    ```
    
### From Stackoverflow
* Ref [Crawling with an authenticated session in Scrapy](http://stackoverflow.com/a/5857202)
    * [init.py](https://github.com/scrapy/scrapy/blob/master/scrapy/spiders/init.py)

```
    from scrapy.contrib.spiders.init import InitSpider
    from scrapy.http import Request, FormRequest
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.contrib.spiders import Rule

    class MySpider(InitSpider):
        name = 'myspider'
        allowed_domains = ['domain.com']
        login_page = 'http://www.domain.com/login'
        start_urls = ['http://www.domain.com/useful_page/',
                      'http://www.domain.com/another_useful_page/']

        rules = (
            Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
                 callback='parse_item', follow=True),
        )

        def init_request(self):
            """This function is called before crawling starts."""
            return Request(url=self.login_page, callback=self.login)

        def login(self, response):
            """Generate a login request."""
            return FormRequest.from_response(response,
                        formdata={'name': 'herman', 'password': 'password'},
                        callback=self.check_login_response)

        def check_login_response(self, response):
            """Check the response returned by a login request to see if we are
            successfully logged in.
            """
            if "Hi Herman" in response.body:
                self.log("Successfully logged in. Let's start crawling!")
                # Now the crawling can begin..
                return self.initialized()
            else:
                self.log("Bad times :(")
                # Something went wrong, we couldn't log in, so nothing happens.

        def parse_item(self, response):

            # Scrape data from page
```
* Ref: [Using selenium get cookies](http://stackoverflow.com/q/11271928)

```
    from scrapy.contrib.spiders.init import InitSpider
    from scrapy.http import Request, FormRequest
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.contrib.spiders import Rule
    from selenium import webdriver

    class ProductDetailsSpider(InitSpider):
        name = 'product_details_spider'
        allowed_domains = ['my_domain.com']
        login_page = 'http://www.my_domain.com/'
        start_urls = ['http://www.my_domain.com/nextpage1/',
                      'http://www.my_domain.com/nextpage2/',
                      'http://www.my_domain.com/nextpage3/']

        rules = (
            Rule(SgmlLinkExtractor(allow=()),
                callback='parse_item',
                follow=True),
            )

        def get_cookies(self):
            driver = webdriver.Firefox()
            driver.implicitly_wait(30)
            base_url = "http://www.my_domain.com"
            driver.get(base_url + "/")
            driver.find_element_by_name("USR").clear()
            driver.find_element_by_name("USR").send_keys("my_user")
            driver.find_element_by_name("PASSWRD").clear()
            driver.find_element_by_name("PASSWRD").send_keys("my_pass")
            driver.find_element_by_name("submit").click()
            cookies = driver.get_cookies()
            driver.close()
            cookie_dic = {}
            for c in cookies:
                cookie_dic[c['name']] = c['value']
            return cookie_dic

        def init_request(self):
            print '=======================INIT======================='
            """This function is called before crawling starts."""
            return Request(url=self.login_page, callback=self.login)

        def login(self, response):
            print '=======================LOGIN======================='
            """Generate a login request."""
            return [FormRequest.from_response(response,formname='login_form',
                formdata={'USR': 'my_user', 'PASSWRD': 'my_pass'},
                callback=self.login_cookies)]

        def login_cookies(self, response):
            print '=======================COOKIES======================='
            return Request(url='http://www.my_domain.com/home',
                cookies=self.get_cookies(),
                callback=self.check_login_response)

        def check_login_response(self, response):
            print '=======================CHECK LOGIN======================='
            """Check the response returned by a login request to see if we are
            successfully logged in.
            """
            if "Logoff" in response.body:
                print "=========Successfully logged in.========="
                return self.initialized() # Add return
                # Now the crawling can begin..
            else:
                print "==============Bad times :(==============="
                # Something went wrong, we couldn't log in, so nothing happens.

        def parse_item(self, response):
            print "==============PARSE ITEM=========================="
        # Scrape data from page    
```    
## Crawling rules

* *rules* Which is a list of one (or more) *Rule* objects.
* Each *Rule* defines a certain behaviour for crawling the site.
* If multiple rules match the same link, the first one will be used, according to the order they're defined in this attribute.

### Crawling rules
    ```
    class scrapy.contrib.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)
    
    ```
* When writing crawl spider rules, avoid using parse as callback, since the CrawlSpider uses the parse method itself to implement its logic. So if you override the parse method, the crawl spider will no longer work.

### CrawlSpider example

```
    from scrapy.contrib.spiders import CrawlSpider, Rule
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
    from scrapy.selector import HtmlXPathSelector
    from scrapy.item import Item

    class MySpider(CrawlSpider):
        name = 'example.com'
        allowed_domains = ['example.com']
        start_urls = ['http://www.example.com']

        rules = (
            # Extract links matching 'category.php' (but not matching 'subsection.php')
            # and follow links from them (since no callback means follow=True by default).
            Rule(SgmlLinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

            # Extract links matching 'item.php' and parse them with the spider's method parse_item
            Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
        )

        def parse_item(self, response):
            self.log('Hi, this is an item page! %s' % response.url)

            hxs = HtmlXPathSelector(response)
            item = Item()
            item['id'] = hxs.select('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
            item['name'] = hxs.select('//td[@id="item_name"]/text()').extract()
            item['description'] = hxs.select('//td[@id="item_description"]/text()').extract()
            return item
```
    
    
    
# Q&A

* exceptions.ImportError: No module named win32api
    * [PyPI上搜索](https://pypi.python.org/pypi) *pywin32* 
    * [Download URL](https://sourceforge.net/projects/pywin32/files/pywin32/)
    * [选择对应版本: pywin32-220.win-amd64-py2.7.exe](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/pywin32-220.win-amd64-py2.7.exe/download)
    * Installed.
    
* UnicodeDecodeError: scrapy.extensions.feedexport.FeedExporter
    * 