from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
a = []


with open("final_SNP.txt") as f:
    for line in f:
        a.append(line.strip())


url = "https://www.ebi.ac.uk/gwas/variants/" 
url2 = []

for value in a:
    url2.append(url+value)



fr = []


driver = webdriver.Chrome()

for value in url2:
    driver.get(value)
    
    # Wait for the element to load
    allele_element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#variant-alleles > span > small"))
	)

    #Extract the text content of the element
    allele_text = allele_element.text
    print(allele_text)
    fr.append(allele_text)
    
driver.quit()

#    print(temp)
#with open('EAS_REF.txt','w+') as file:
#    file.write('\n'.join(ref))
#
#with open('EAS_ALT.txt','w+') as file:
#    file.write('\n'.join(alt))
#

