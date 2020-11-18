import pandas
import os
import subprocess
import xml.etree.ElementTree as ET
import sys

filetoprocess = sys.argv[1]
print(filetoprocess)
pass_word = os.getenv('WEBIN_USER_PASSWORD')
user_token = os.getenv('WEBIN_USER').split("@")[0]
ena_service = "https://www.ebi.ac.uk/ena/submit/drop-box/submit/"


data = pandas.read_excel(filetoprocess, keep_default_na=False)

data = data.apply(lambda x:x.astype(str))

def update_sample(registered_sample, row, sample_accession):
    #print(sample_accession)
    doc = ET.fromstring(registered_sample)
    tree = ET.ElementTree(doc)
    for header, item in row.items():
        #print("header, item", header, item)
        if header == "Accession Number":
            pass
        else:
            flag = False
            attributes = tree.find('SAMPLE').find('SAMPLE_ATTRIBUTES').findall('SAMPLE_ATTRIBUTE')
            for attribute in attributes:
                tag = attribute.find('TAG').text
                #print(tag)
                value =  attribute.find('VALUE').text
                #print(tag, value)
                if tag == header:
                    #update value
                    #print(tag)
                    value_block = attribute.find('VALUE')
                    value_block.text = item
                    flag = True
                    break
            if flag == False:
                #add new attriobute to xml
                attributes_block = tree.find('SAMPLE').find('SAMPLE_ATTRIBUTES')
                sample_attribute = ET.SubElement(attributes_block, 'SAMPLE_ATTRIBUTE')
                tag_block = ET.SubElement(sample_attribute, 'TAG')
                tag_block.text = header
                value_block = ET.SubElement(sample_attribute, 'VALUE')
                value_block.text = item
                #ET.dump(tree)

    ET.dump(tree)
    tree.write(open(sample_accession+".xml", 'w'), encoding='unicode')

def modify_sample(accession):
    curl_cmd = 'curl -u ' + user_token + ':' + pass_word \
               + ' -F "SUBMISSION=@modifysubmission.xml' \
               + '" -F "SAMPLE=@' \
               + accession +".xml" \
               + '" "' + ena_service \
               + '"'
    try:
        receipt = subprocess.check_output(curl_cmd, shell=True)
        print(receipt)
    except Exception as e:
        message = 'API call error ' + "Submitting project xml to ENA via CURL. CURL command is: " + curl_cmd.replace(
            pass_word, "xxxxxx")
        notify_dtol_status(data={"profile_id": profile_id}, msg=message, action="error",
                           html_id="dtol_sample_info")
        return False

    os.remove(accession+".xml")
    
    

for index, row in data.iterrows():
    exp_accession = row["Accession Number"].strip()
    print(exp_accession)
    curl_cmd = "curl https://www.ebi.ac.uk/ena/browser/api/xml/" + exp_accession
    experiment = subprocess.check_output(curl_cmd, shell=True)

    tree = ET.fromstring(experiment)
    for link in tree.find('RUN').find('RUN_LINKS').findall('RUN_LINK'):
        #print('here')
        db = link.find('XREF_LINK').find('DB').text
        value = link.find('XREF_LINK').find('ID').text
        if db == 'ENA-SAMPLE':
            print(value)
            curl_cmd = "curl -u " + user_token + ':' + pass_word + " https://www.ebi.ac.uk/ena/submit/drop-box/samples/" + value
            registered_sample = subprocess.check_output(curl_cmd, shell=True)
            update_sample(registered_sample, row, value)
            modify_sample(value)
            break


