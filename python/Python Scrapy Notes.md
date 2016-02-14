
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