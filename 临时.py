from lxml import etree
import requests

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


if __name__ == "__main__":
    # tree = etree.parse('test.html')
    # r = tree.xpath('/html/head/title/text()')
    # print(r)
    url = "http://fund.eastmoney.com/data/fundranking.html#tgp;c0;r;s1nzf;pn50;dasc;qsd20220107;qed20230107;qdii;zq" \
          ";gg;gzbd;gzfs;bbzt;sfbb "



    response = requests.get(url=url,headers=header)
    print(response.text)
