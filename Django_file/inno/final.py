import requests
from bs4 import BeautifulSoup
import re
import sys
import os
from datetime import datetime

def compare_rule_name(rule_name):
    cleaned_rule_name = re.sub(r'[^a-zA-Z0-9]+', '', rule_name)
    if len(cleaned_rule_name) > 0:
        with open('USCA_SECOND_LR.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().strip()
            cleaned_read_content = re.sub(r'[^a-zA-Z0-9]+', '', read_content)
            upper_cleaned_read_content = cleaned_read_content.upper()
            if cleaned_rule_name.strip().upper() in upper_cleaned_read_content:
                same_rules.append(rule_name)
                return True
            else:
                updated_rules.append(rule_name)
                with open('USCA_SECOND_LR _new_rules.txt', 'r', encoding='utf-8') as read_for_update:
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
    out_path = os.path.join(exe_folder, 'out', remove_invalid_paths(source_id),'Local_Rules',date_prefix)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    index = 1
    outFileName = os.path.join(out_path, remove_invalid_paths(main_rule_name) + extention)
    retFileName = outFileName
    while os.path.isfile(retFileName):
        retFileName = os.path.join(out_path, remove_invalid_paths(main_rule_name)+"_"+str(index) + extention)
        index +=1
    return retFileName

def updated_rule_file(source_id, rule_name,extention):
    exe_folder = os.path.dirname(str(os.path.abspath(sys.argv[0])))
    out_path = os.path.join(exe_folder, 'out', remove_invalid_paths(source_id),'Updated_Rules')
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    index = 1
    outFileName = os.path.join(out_path, remove_invalid_paths(rule_name) + extention)
    retFileName = outFileName
    while os.path.isfile(retFileName):
        retFileName = os.path.join(out_path, remove_invalid_paths(rule_name)+"_"+str(index) + extention)
        index +=1
    return retFileName

def remove_invalid_paths(path_val):
    return re.sub(r'[\\/*?:"<>|]', "", path_val)

def getSoup(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    return soup

def final_procedure(compared_rule_name,rule_div_content,main_rule_name):
    if compared_rule_name==True:
        output_file_name = ret_file_name_full(source_id, main_rule_name, '.html')
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(str(rule_div_content))
            print(output_file_name)
    elif compared_rule_name==False:
        output_file_name = updated_rule_file(source_id, main_rule_name,'.html')
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(str(rule_div_content))
            print(output_file_name)

def single_page_rules(url,rule_name):
    new_soup = getSoup(url)
    table_content = new_soup.find_all('table', {'style': 'width: 99%'})
    html_content = ''
    for i in table_content:
        try:
            img_tag = i.find('img')
            paragraph_tag = i.find('td', class_='subpage_text')
            if img_tag:
                text = img_tag['alt']
                text = f'<h1>{text}</h1>'
                html_content = html_content + text

            if paragraph_tag:
                paragraph = str(paragraph_tag)
                paragraph = re.sub(r'\s+', '\n', paragraph)
                html_content = html_content + str(paragraph)

        except Exception as e:
            error_list.append(e)
    compared_rule_name = compare_rule_name(rule_name)
    final_procedure(compared_rule_name, html_content, rule_name)

updated_rules=[]
same_rules=[]
error_list=[]

source_id = 'USCA_SECOND_LR_Rules'
url='https://www.ca2.uscourts.gov/clerk/case_filing/rules/rules_home.html'
soup = getSoup(url)
table=soup.find('ul',class_='treeview')
rule_links=table.find_all('a', class_='sublinks')

if os.path.exists('USCA_SECOND_LR.txt') and os.path.exists('USCA_SECOND_LR _new_rules.txt'):
    for rule_link in rule_links:
        try:
            rule_name=rule_link.text.strip()
            rule_name = re.sub(r'\s+', ' ', rule_name)
            rule_url='https://www.ca2.uscourts.gov/clerk/case_filing/rules/'+rule_link.get('href')
            single_page_rules(rule_url,rule_name)
        except Exception as e:
            error_list.append(e)
else:
    print("'USCA_SECOND_LR.txt' or 'USCA_SECOND_LR _new_rules.txt' does not exist in the current directory.")

