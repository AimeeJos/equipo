from bs4 import BeautifulSoup
import requests
from assignment_1.tasks import do_more_scrapping
from assignment_1.progress import progress_bar


def generate_soup(url):
    soup = None
    response = None
    try:
        headers = {
            "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
    except Exception as e:
        print("Exception:----")
        print(e)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

    return soup


def extract_clickable_tr_tags(soup):
    tr_tags = list(soup.find_all("tr", class_="clickable-row"))
    return tr_tags


def extract_short(url):
    soup = generate_soup(url)
    tr = soup.find("tr")
    all_td = tr.find_all("td")
    short = all_td[1].text.strip()
    return short


def extract_codes(url, group, category, taskid):
    print(url, group, category)
    all_codes = []
    tr_tags = extract_clickable_tr_tags(generate_soup(url))
    all_td = list(map(lambda tr_tag: tr_tag.find_all("td"), tr_tags))
    for i, td in enumerate(all_td):
        progress_bar(taskid, i + 2)
        if i > 10:
            break
        codes = {}
        codes["group"] = group
        codes["category"] = category
        codes["code"] = td[0].a.text.strip()
        codes["long"] = td[1].text.strip()
        codes["short"] = extract_short(url + "/" + td[0].a.text.strip())
        all_codes.append(codes)
    return all_codes


def extract_data():

    soup = generate_soup("https://www.hcpcsdata.com/Codes")
    tr_tags = extract_clickable_tr_tags(soup)
    all_td = list(map(lambda tr_tag: tr_tag.find_all("td"), tr_tags))

    groups = list(map(lambda td: f"HCPCS {td[0].a.text.strip()}", all_td))
    counts = list(map(lambda td: td[1].text.strip(), all_td))
    categories = list(map(lambda td: td[2].text.strip(), all_td))
    snos = range(1, len(groups) + 1)
    urls = list(
        map(
            lambda td: f"https://www.hcpcsdata.com/Codes/{td[0].a.text.strip()[1:2]}",
            all_td,
        )
    )
    # taskids = [
    #     do_more_scrapping.apply_async(args=[groups[0], categories[0], urls[0]]).id
    # ]
    taskids = [
        do_more_scrapping.apply_async(args=[group, category, url]).id
        for group, category, url in zip(groups, categories, urls)
    ]

    # groups, counts, categories, snos, taskids = (
    #     [groups[0]],
    #     [counts[0]],
    #     [categories[0]],
    #     [snos[0]],
    #     taskids,
    # )
    return zip(groups, counts, categories, snos, taskids)
