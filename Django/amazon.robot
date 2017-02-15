*** Settings ***
Documentation     This is info
Suite Setup       Open Browser    ${HomePage}
Test Setup        Go To    ${HomePage}    #Suite Teardown    Close All Browsers
Library           Selenium2Library
Library           csvLibrary.py
Library           DatabaseLibrary
Library           Process

*** Variables ***
${HomePage}       http://www.google.ca

*** Test Cases ***
Google istuary
    [Tags]    CID:C8
    ${data}    read csv file    try.csv
    Google and check    ${data[0][0]}
    Wait Until Page Contains    ${data[0][0]}

Google baidu
    [Tags]    CID:C9
    ${data}    read csv file    try.csv
    Google and check    ${data[1][0]}
    Wait Until Page Contains    ${data[1][0]}
    close All Browsers

Google something else
    [Tags]    CID:C10
    ${data}    read csv file    try.csv
    Google and check    ${data[1][1]}
    Wait Until Page Contains    ${data[1][1]}

*** Keywords ***
Google and check
    [Arguments]    ${searchkey}
    maximize browser window
    input text    id=lst-ib    ${searchkey}
    click element    id=_fZl
    click element    id=gb_70
    #Wait Until Page Contains    ${result}
