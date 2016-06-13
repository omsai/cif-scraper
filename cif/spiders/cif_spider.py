import cif.items
import scrapy


class CifSpider(scrapy.Spider):
    name = "cif"
    allowed_domains = ["hmofs.northwestern.edu"]
    start_urls = ["http://hmofs.northwestern.edu/hc/crystals.php"]

    def parse(self, response):
        # Table rows are broken by \n instead of <tr>, therefore we
        # extract flattened td cells and group them by the 7.
        item = cif.items.CifItem()
        KEYS = cif.items.KEYS
        for i, sel in enumerate(response.xpath('//table[@border="1"]//td')):
            if i % 7 != 6:
                item[KEYS[i % 7]] = sel.xpath('text()').extract()[0]
            else:
                item[KEYS[i % 7]] = response.urljoin(sel.xpath('a[1]/@href').extract()[0])
                yield item

        next_page = response.xpath('//div[@id="content_wide_nopadding"]//a[starts-with(text(),"next")]/@href').extract()
        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, self.parse)

