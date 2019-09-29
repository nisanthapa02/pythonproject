import time
from selenium import webdriver

def funcXpath(browser, name):
    return browser.find_element_by_xpath(r"//div[@name='" + name + r"']").text

file = open("D:\\collegelist.txt", "r", newline='\r\n')
#   open chrome before loop so that it doesnt have to close and open every loop
browser = webdriver.Chrome()

for indUrl in file:

    #   navigate to the uni Url
    browser.get(indUrl.rstrip())

    time.sleep(3)
    #   get uni url
    uniUrl = browser.find_element_by_name("collegeURL").get_attribute("href")
    print(uniUrl)

    #   find Deadlines
    deadline = browser.find_element_by_xpath(r"//a[text()='Deadlines']")
    #   scroll so that deadline can be viweable in the screen
    deadline.location_once_scrolled_into_view
    time.sleep(1)
    #   now finally click once the element is in view
    deadline.click()

    # time.sleep(5)
    #   get deadlines
    appDue = funcXpath(browser, "regularApplicationDueMonth") + funcXpath(browser, "regularApplicationDueDay")
    appPDue = funcXpath(browser, "priorityApplicationDueMonth") + funcXpath(browser, "priorityApplicationDueDay")
    notifDue = funcXpath(browser, "collegeNotificationEndMonth") + funcXpath(browser, "collegeNotificationEndDay")

    eaDue = funcXpath(browser, "earlyActionApplicationDueMonth") + funcXpath(browser, "earlyActionApplicationDueDay")
    satDue = funcXpath(browser, "satScoreReportDueMonth") + funcXpath(browser, "satScoreReportDueDay")
    aidDue = funcXpath(browser, "financialAidApplicationDueMonth") + funcXpath(browser, "financialAidApplicationDueDay")
    aidPDue = funcXpath(browser, "financialAidPriorityApplicationDueMonth") + funcXpath(browser, "financialAidPriorityApplicationDueDay")
    print(appDue, appPDue, notifDue, eaDue, satDue, aidDue, aidPDue)

    time.sleep(1)
    #   click applying
    browser.find_element_by_xpath(r"//a[text()='Applying']").click()

    # get EA, ED, RD
    rdApplicant = funcXpath(browser, "regularApplicants")
    rdAdmitted = funcXpath(browser, "regularAdmitted")
    eaApplicant = funcXpath(browser, "earlyActionApply")
    eaAdmitted = funcXpath(browser, "earlyActionAdmitted")
    edApplicant = funcXpath(browser, "earlyDecisionApply")
    edAdmitted = funcXpath(browser, "earlyDecisionAdmitted")
    print(rdApplicant, rdAdmitted, eaApplicant, eaAdmitted, edApplicant, edAdmitted)
    # rdRate = rdAdmitted / rdApplicant * 100
    # edRate = edAdmitted / edApplicant * 100
    # eaRate = eaAdmitted / eaApplicant * 100

    time.sleep(1)
    #   click paying
    browser.find_element_by_xpath(r"//a[text()='Paying']").click()

    time.sleep(3)
    #   get in state fee
    intuitionElems = browser.find_elements_by_xpath(r"//tbody//tr//td//span")

    intuitionFee = intuitionElems[0].text
    inroomOnC = intuitionElems[3].text
    inroomOffC = intuitionElems[4].text
    inbookFee = intuitionElems[9].text
    inpersonalFee = intuitionElems[12].text
    intransportFee = intuitionElems[15].text
    intotalOnC = intuitionElems[18].text
    intotalOffC = intuitionElems[20].text

    print(intuitionFee, inroomOnC, inroomOffC, inbookFee, inpersonalFee, intransportFee, intotalOnC, intotalOffC)

    #   click out of state
    # browser.find_element_by_xpath(r"//a[contains(text(), 'State')]").click())
    browser.find_element_by_xpath(r"//a[text()='Out-Of-State Costs']").click()

    #   get fees
    #   below xpath luckily gets all the fees with 3 additional dashes. total 21
    tuitionElems = browser.find_elements_by_xpath(r"//tbody//tr//td//span")

    tuitionFee = tuitionElems[0].text
    roomOnC = tuitionElems[3].text
    roomOffC = tuitionElems[4].text
    bookFee = tuitionElems[9].text
    personalFee = tuitionElems[12].text
    transportFee = tuitionElems[15].text
    totalOnC = tuitionElems[18].text
    totalOffC = tuitionElems[20].text

    print(tuitionFee, roomOnC, roomOffC, bookFee, personalFee, transportFee, totalOnC, totalOffC)

    time.sleep(1)
    # click intl
    browser.find_element_by_xpath(r"//a[text()='For International Students']").click()

    intlAidNum = browser.find_element_by_xpath(r"//li[text()='Number of enrolled international undergraduates received aid: ']//following-sibling::span").text
    intlAidSum = browser.find_element_by_xpath(r"//li[text()='Total amount awarded: ']//following-sibling::span").text
    toeflMin = browser.find_element_by_xpath(r"//li[text()='TOEFL (internet-based test) minimum score: ']//following-sibling::span").text

    print(intlAidNum, intlAidSum, toeflMin)

browser.quit()
file.close()
