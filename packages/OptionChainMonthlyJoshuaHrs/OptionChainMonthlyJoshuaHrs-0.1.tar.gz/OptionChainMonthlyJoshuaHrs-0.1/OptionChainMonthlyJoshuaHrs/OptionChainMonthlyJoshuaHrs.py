class OptionChainMonthlyJoshuaHrs:
    #OptionChainJosuaHrs
    
    def __init__(self):
        
        print("INSIDE MOnthly Automation Function")
        
        self.dates = []
        self.choDate = ""
        self.alertGiven = []
        self.history = []
        
        #self.start()
    
    
    def collectData(self):
        import requests

        url = "https://www.nseindia.com/api/option-chain-currency?symbol=USDINR"
        baseurl = "https://www.nseindia.com/"
        headers={'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.50',
        'accept-encoding': "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
            }
        
        try:
            session = requests.Session()
            request = session.get(baseurl, headers=headers, timeout=5)
            coo = dict(request.cookies)
            response = session.get(url, headers=headers, timeout=10,cookies = coo)

            while(response.status_code != 200):
                response = session.get(url, headers=headers, timeout=10, cookies = coo)
                time.sleep(5)

            self.dates = response.json()['records']['expiryDates']

            return response.json()['records']
        
        except:
            print("Failed Collecting Data---- REPORT!")
            return self.collectData()
        
        
    
    def updateExcel(self):
        import os
        import pandas as pd
        from datetime import datetime 
        #Date | Expiry | USD | Strike | CE | PE | Total
        
        data = self.collectData()
        
        dollar_p = float(data['index']['rate'])
        
        if(self.choDate == ""):
            print("ENTER DATE NUMBER between 1 to ", len(self.dates))
            i = 1
            for d in self.dates:
                print("Press",i,"for : ", d)
                i += 1
            x = int(input()) - 1
            
            if(x < 0 or x > len(self.dates)):
                assert False
            self.choDate = self.dates[x]
            
        ce_lp, pe_lp, strike_p = self.extractData(data['data'],dollar_p)
        
        
        
        
        p1 = os.getcwd()
        li = os.listdir()
        if(self.choDate + ".xlsx" not in li):
            dataset = pd.DataFrame(columns = ['Date', 'Expiry Date',"USD", "Strike Price", "CE-LP", "PE-LP", "CE+PE"])
        else:
            dataset = pd.read_excel(p1 + "/" + self.choDate + ".xlsx")
            
        dataset.loc[len(dataset),:] = [datetime.now(),self.choDate,dollar_p,strike_p,ce_lp,pe_lp,ce_lp + pe_lp]
        dataset.to_excel(p1 + "/" +self.choDate + ".xlsx", index = False)
        
        print("SAVED AT: ",p1 + "/" +self.choDate + ".xlsx")
        
        return None 
        
    
    
    def formula2(self):
        
        pass
    
    
    
    def extractData(self,data,dollar_p):
        import time 
        from datetime import datetime
        
        infoP = {}
        infoN = {}
        
        for x in data:
            if(x['expiryDate'] == self.choDate):
                pdiff = dollar_p - x['strikePrice']
                if("CE" not in x or "PE" not in x):
                    continue
                
                ce = x['CE']['lastPrice']
                pe = x['PE']['lastPrice']
                
                if(pdiff >= 0):
                    infoP[pdiff] = [x['strikePrice'],ce,pe]
                else:
                    infoN[pdiff] = [ce,pe]
        
        vp = sorted(infoP)[0]
        vn = sorted(infoN)[0]
        
        
        print("Expiry Date : ", self.choDate, end= "\t")
        print("Current Time: ", datetime.now(), end = "\t")
        print("Dollar Price : ", dollar_p, end = "\n")
        
        if(abs(vn) < abs(vp)):
            info = infoN[vn]
        else:
            info = infoP[vp]
        
        print("Strike at : ", info[0], end = "\t")
        print("PUT : ", info[2], " CALL : ", info[1], end = "\t")
        print("TOTAL : ", info[1] + info[2])
        
        print("\n")
        
        return info[1],info[2], info[0]
    
        
    
    
    def raiseAlert(self,dollar_p,ce_p,pe_p,Strike_p):
        import cv2
        import numpy as np
        from datetime import datetime
        
        image = np.zeros((500, 500, 3), dtype = "uint8")
        window_name = 'ALERT'
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (200, 75)
        fontScale = 1
        color = (0,0, 255)
        thickness = 2
        image = cv2.putText(image, 'ALERT!', org, font, fontScale, color, thickness, cv2.LINE_AA)
        
        txt1 = "Option-chain-currency : USDINR"
        txt2 = "Expiry Date : " + str(self.choDate)
        txt3 = "Current Time : " + str(datetime.now())
        txt4 = "USA Dollar Price : " + str(dollar_p)
        txt5 = "Strike Price : " + str(Strike_p)
        txt6 = "CALL price : " + str(ce_p) + "  |   PUT Price : " + str(pe_p)
        image = cv2.putText(image, txt1, (50,125), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        image = cv2.putText(image, txt2, (50,150), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        image = cv2.putText(image, txt3, (50,175), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        image = cv2.putText(image, txt4, (50,200), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        image = cv2.putText(image, txt5, (50,250), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        image = cv2.putText(image, txt6, (50,275), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        image = cv2.putText(image, str(pe_p + ce_p), (50,300), font, 0.65, (255,255,255), thickness, cv2.LINE_AA)
        
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    
    
    
    def start(self):
        import time
        from datetime import datetime
        
        print("THIS IS OPTION-CHAIN US/INR DATA")
        data = self.collectData()
        dollar_p = float(data['index']['rate'])
        
        if(self.choDate == ""):
            print("ENTER DATE NUMBER between 1 to ", len(self.dates))
            i = 1
            for d in self.dates:
                print("Press",i,"for : ", d)
                i += 1
            x = int(input()) - 1
            
            if(x < 0 or x > len(self.dates)):
                assert False
            self.choDate = self.dates[x]
            
        ce_lp, pe_lp, strike_p = self.extractData(data['data'],dollar_p)
        
        while(True):
            r = 0
            ce_lp, pe_lp, strike_p = self.extractData(data['data'],dollar_p)
            
            #ce_lp + pe_lp >= 1.20 #and ce_lp + pe_lp <= 1.35
            if(ce_lp + pe_lp >= 1.20):
                print("RAISING ALERT")
                self.raiseAlert(dollar_p,ce_lp,pe_lp,strike_p)
                r = 1
                
            dd = [datetime.now(), self.choDate, dollar_p, strike_p, ce_lp, pe_lp, ce_lp + pe_lp,r]
            #self.updateExcel(dd)
            
            print("\nNext Collection after 30 minutes...")
            time.sleep(60*30) #30 mins 
            data = self.collectData()
            dollar_p = float(data['index']['rate'])
            

        
        
            
            