import requests
from bs4 import BeautifulSoup
import json
import os
import re
import sys
from datetime import datetime

def compare_rule_name(rule_name):
    cleaned_rule_name = re.sub(r'[^a-zA-Z0-9]+', '', rule_name)
    with open('NYSE_AMEX.txt', 'r', encoding='utf-8') as read_file:
        read_content = read_file.read().strip()
        cleaned_read_content = re.sub(r'[^a-zA-Z0-9]+', '', read_content)
        upper_cleaned_read_content = cleaned_read_content.upper()
        if cleaned_rule_name.strip().upper() in upper_cleaned_read_content:
            same_rules.append(rule_name)
            return True
        else:
            updated_rules.append(rule_name)
            with open('NYSE_AMEX_new_rules.txt', 'r', encoding='utf-8') as read_for_update:
                read_update_content = read_for_update.read().strip()
                cln_update_content = re.sub(r'[^a-zA-Z0-9]+', '', read_update_content)
                upr_cln_update = cln_update_content.upper()
                if cleaned_rule_name.strip().upper() in upr_cln_update:
                    return True
                else:
                    return False

def ret_file_name_full(source_id, main_rule_name, extention):
    exe_folder = os.path.dirname(str(os.path.abspath(sys.argv[0])))
    date_prefix = datetime.today().strftime("%Y%m%d")
    out_path = os.path.join(exe_folder, 'out', remove_invalid_paths(source_id), 'Rules', date_prefix)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    outFileName = os.path.join(out_path, remove_invalid_paths(main_rule_name) + extention)
    return outFileName

def updated_rule_file(source_id, rule_name, extention):
    exe_folder = os.path.dirname(str(os.path.abspath(sys.argv[0])))
    out_path = os.path.join(exe_folder, 'out', remove_invalid_paths(source_id), 'Updated_Rules')
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    outFileName = os.path.join(out_path, remove_invalid_paths(rule_name) + extention)
    return outFileName

def final_procedure(compared_rule_name, rule_div_content, main_rule_name):
    if compared_rule_name:
        output_file_name = ret_file_name_full(source_id, main_rule_name, '.html')
    else:
        output_file_name = updated_rule_file(source_id, main_rule_name, '.html')
    with open(output_file_name, 'w', encoding='utf-8') as file:
        file.write(str(rule_div_content))
        print(output_file_name)

def remove_invalid_paths(path_val):
    return re.sub(r'[\\/*?:"<>|]', "", path_val)

def get_rule(url,rule_name):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    desired_script = soup.find('script', id='__NEXT_DATA__')
    if desired_script:
        data = json.loads(desired_script.text)
        page_props = data.get("props", {})
        content_html = page_props.get("pageProps", {}).get("document", {}).get("section", {}).get("document", {}).get(
            "content", "")

        content_soup = BeautifulSoup(content_html, 'html.parser')

        div_ele = content_soup.find('div', class_='documentContent')
        last_p_with_class_hP = div_ele.find_all('p', class_='hP')[-1]
        last_p_with_class_hP.extract()
        last_p_with_class_hP = div_ele.find_all('p', class_='hP')[-1]
        last_p_with_class_hP.extract()
        last_p_with_class_hP = div_ele.find('button', {
            'class': 'wk-button wk-button-icon wk-button-small nyse-document-download-link'})
        last_p_with_class_hP.extract()
        if len(rule_name) > 0:
            compared_rule_name = compare_rule_name(rule_name)
            final_procedure(compared_rule_name, div_ele, rule_name)
def get_child(parent_nodes):
    for document in parent_nodes:
        try:
            children_nodes = document.get("children", [])
            if children_nodes:
                return children_nodes
            else:
                new_title1 = document.get("title")
                if not new_title1 in printed_rules:
                    rule_link=document.get("href")
                    if rule_link:
                        printed_rules.append(new_title1)
                        link = rule_link.replace("/browse/", "https://nyseamericanguide.srorules.com/rules/")
                        get_rule(link,new_title1)

        except Exception as e:
            error_list.append(e)

source_id = 'NYSE_AMEX_Rules'
out_path = 'out'
if not os.path.exists(out_path):
    os.makedirs(out_path)

same_rules = []
updated_rules = []
error_list = []
printed_rules = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

if os.path.exists('NYSE_AMEX.txt') and os.path.exists('NYSE_AMEX_new_rules.txt') and os.path.exists('Links.txt'):
    try:
        with open('Links.txt', 'r') as file:
            url_list = [line.strip() for line in file]
    except Exception as e:
        error_list.append(e)

    for url in url_list:
        try:
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            desired_script = soup.find('script', id='__NEXT_DATA__')

            if desired_script:
                data = json.loads(desired_script.text)
                page_props = data.get("props", {})
                all_parent_nodes = page_props.get("pageProps", {}).get("allParentNodes", [])

                i=0
                while i<10:
                    all_parent_nodes=get_child(all_parent_nodes)
                    if all_parent_nodes:
                        i=0
                    else:
                        i=20
            else:
                print("Script with id '__NEXT_DATA__' not found in the HTML.")

        except Exception as e:
            error_list.append(e)

    with open('NYSE_AMEX_new_rules.txt', 'w', encoding='utf-8') as same_rule:
        for rule in same_rules:
            same_rule.write(rule + '\n')
else:
    print("'NYSE_AMEX.txt' or 'NYSE_AMEX_new_rules.txt' or 'Links.txt' does not exist in the current directory.")
