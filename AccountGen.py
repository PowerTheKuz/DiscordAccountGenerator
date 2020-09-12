#...
    # Code from > https://github.com/PowerTheKuz/DiscordAccountGenerator
    # Suport > https://www.buymeacoffee.com/PowerKuz

import os
import time
import sys
import colored
import random, string

cwd = os.path.dirname(os.path.realpath(__file__))

try: # Import - Driver
    import os
    import time
    import sys
    import random, string

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    from selenium.webdriver.common.keys import Keys
except:
    print('Error importing driver view > https://github.com/PowerTheKuz/DiscordAccountGenerator/blob/master/README.md')

try: # Logger
    _error = "[Error] "
    _succes = "[Succes] "
    _info = "[Info] "

    def success(content):
        color = colored.fg("green")
        print(color + _succes + colored.attr("reset") + content + colored.attr("reset"))

    def error(content):
        color = colored.fg("red")
        print(color + _error + colored.attr("reset") + content + colored.attr("reset"))

    def info(content):
        color = colored.fg("orange_1")
        print(color + _info + colored.attr("reset") + content + colored.attr("reset"))
except:
    print('Error importing logger, do u have colored Installed?')

if os.path.isdir(cwd + '\\Driver'):
    pass
else:
    error('Cannot find ' + cwd + '\\Driver')

sys.dont_write_bytecode = True
info('Using DiscordAccountGenerator - 1.0 > https://github.com/PowerTheKuz/DiscordAccountGenerator')

# Defs
def generate(proxy = 'Null', reapet = False, headless = True, init = True):
    try: # Start driver
        options = webdriver.ChromeOptions() 

        if proxy == 'Null':
            pass
        else:
            options.add_argument('--proxy-server=%s' % proxy)

        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('log-level=3')

        if headless == True:
            options.add_argument("--window-position=10000,0")

        options.add_argument("--disable-blink-features=AutomationControlled")

        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options, executable_path= cwd + '\\driver\\driver.exe')
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    except:
        error('Error while starting webdriver')
        sys.exit()

    def run():             
        def randomword(length):
            try: # Random
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(length))
            except:
                error('Error while generating random string')

        email = randomword(10) + '@email.com'
        password = randomword(10)

        username = randomword(8)

        action = ActionChains(driver)

        def click(css, time = 20):
            try: # Click
                WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css))).click()
            except:
                error('Error while finding web element > ' + css)
        
        def write(css, string):
            try: # Write
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css))).send_keys(string)
            except:
                error('Error while finding web element > ' + css)



        passwordCSS = '#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(3) > div > input'
        usernameCSS = '#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(2) > div > input'

        tosCSS = '#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div.flex-1xMQg5.flex-1O1GKY.horizontal-1ae9ci.horizontal-2EEEnY.flex-1O1GKY.directionRow-3v3tfG.justifyStart-2NDFzi.alignCenter-1dQNNs.noWrap-3jynv6.marginTop20-3TxNs6 > label > input'

        MonthCSS = '#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div.container-3bTSed.marginTop20-3TxNs6 > div.inputs-14Hc7m > div:nth-child(1) > div > div'
        MonthJanuar = '#app-mount > div.popouts-2bnG9Z > div > div.popout-2sKjHu.lookFilled-1h1y05.sizeMedium-6vZ9JV.thin-1ybCId.scrollerBase-289Jih > div:nth-child(1)'

        DayCSS = '#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div.container-3bTSed.marginTop20-3TxNs6 > div.inputs-14Hc7m > div:nth-child(2) > div > div'
        Day1 = '#app-mount > div.popouts-2bnG9Z > div > div.popout-2sKjHu.lookFilled-1h1y05.sizeMedium-6vZ9JV.thin-1ybCId.scrollerBase-289Jih > div:nth-child(1)'

        YearCSS = '#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div.container-3bTSed.marginTop20-3TxNs6 > div.inputs-14Hc7m > div:nth-child(3) > div > div'
        Year2000 = '#app-mount > div.popouts-2bnG9Z > div > div.popout-2sKjHu.lookFilled-1h1y05.sizeMedium-6vZ9JV.thin-1ybCId.scrollerBase-289Jih > div:nth-child(18)'


        try: # Signin
            driver.execute_script("window.open('http://discord.com/register?email=" + email +"');")
            driver.switch_to.window(driver.window_handles[-1])

            write(usernameCSS, username)
            write(passwordCSS, password)
            
            driver.find_element_by_css_selector(tosCSS).click()

            click(MonthCSS)
            click(MonthJanuar)

            click(DayCSS)
            click(Day1)

            click(YearCSS)
            click(Year2000)


            click(passwordCSS)
            action.send_keys(Keys.ENTER)
            action.perform()

            s = False

            
            for _ in range(5):
                if driver.current_url == 'https://discord.com/channels/@me':
                    s = True
                    break
                time.sleep(2)
        except:
            error('Error while executing signing in')

        try: # Write account
            if s == True:
                success(email + ':' + password)
                o = open(cwd + '\\Accounts.txt', 'a')
                o.write(email + ':' + password + '\n')
                o.close()
                if reapet == False:
                    return email + ':' + password
            else:
                error('Error generating account')
        except:
            error('Error while saving to file')

        try: # Quit
            driver.quit()
        except:
            error('Error while closing webdriver')

        try: # Reapet  
            if reapet == True:
                while True:
                    time.sleep(120)
                    generate()
            if reapet == False:
                pass
        except:
            error('Error while reapeting')
    run()

def cleanAccountFile():
    try:
        o = open(cwd + '\\Accounts.txt', 'w')
        o.write('')
        o.close()
    except:
        error('Error cleaing Account-file')

def install():
    try:
        os.system('py get-pip.py')
        os.system('py -m pip install selenium')
        os.system('py -m pip install colored')
    except:
        error('Error install dependencies')
