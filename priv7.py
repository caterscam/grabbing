import requests
from bs4 import BeautifulSoup
import re

def reverse_ip_lookup(domain, session, url, headers):
    r = session.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')

    soup = bs.select_one('label[for="answer"]')

    if soup:
        text = soup.get_text(strip=True)

        match = re.search(r'(\d+)\s*([+-])\s*(\d+)', text)

        if match:
            number1 = int(match.group(1))
            operator = match.group(2)
            number2 = int(match.group(3))

            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2

            form_data = {
                'domain': domain,
                'answer': result,
                'check': 'Check'
            }

            response = session.post(url, data=form_data, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')

            textarea = soup.find('textarea')

            if textarea:
                domains = textarea.get_text().strip().split('\n')
                return domains
            else:
                return ["Textarea not found"]
        else:
            return ["Expression not found in the text"]
    else:
        return ["Label not found"]

def main():
    url = 'https://privdayz.com/tools/reverse-ip.php'
    ua = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)'}

    session = requests.Session()

    headers = {
        'User-Agent': ua['User-Agent'],
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': url,
        'Origin': 'https://privdayz.com'
    }
    domains_list = open(input("[*] domain or ip without http : "),"r").read().splitlines()
    savef = input("[*] save ur result : ")

    for domain in domains_list:
        results = reverse_ip_lookup(domain, session, url, headers)
        
        if results:
            if "No DNS A records found" in results:
                results.remove("No DNS A records found")

            with open(savef, "a") as file:
                for result in results:
                    file.write(result + "\n")

            print(f"[#] [{domain}] total {len(results)} domains")
            for result in results:
                print(f"- {result}")
        else:
            print(f"No results for {domain}\n")

if __name__ == "__main__":
    main()
