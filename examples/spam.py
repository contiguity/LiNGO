import requests
import json

reqUrl = "https://api.contiguity.co/inference/ai/lingo-105b-beta/detect"

headersList = {
 "Accept": "*/*",
 "Authorization": "Token XXXXXXXXXXXXX",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "text": """{"recipient":"a----c@u-------e.edu","from":"SSA Noreply","subject":"Stay Informed: Download the new Social Security ScreenSupport Tool","body":"<!DOCTYPE html PUBLIC \\"-//W3C//DTD XHTML 1.0 Transitional//EN\\" \\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\\"><html dir=ltr lang=en> <head><meta content=\\"text/html; charset=UTF-8\\" http-equiv=Content-Type><meta content=\\"width=device-width\\" name=viewport><meta content=\\"IE=edge\\" http-equiv=X-UA-Compatible><meta name=x-apple-disable-message-reformatting><meta content=\\"telephone=no,address=no,email=no,date=no,url=no\\" name=format-detection><meta content=light name=color-scheme><meta content=\\"light dark\\" name=supported-color-schemes></head> <body style=\\"font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;font-size:1.0769230769230769em;min-height:100%;line-height:155%\\"> <table align=left width=100% border=0 cellpadding=0 cellspacing=0 role=presentation style=\\"align:left;padding-left:0px;padding-right:0px;h-padding:0px;width:auto;max-width:600px;font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif\\"> <tbody> <tr> <td> <div> <div style=\\"width:100%;margin:0;padding:0 20px;display:block;box-sizing:border-box;font-family:calibri, candara, segoe, optima, arial, sans-serif;\\"> <div style=\\"width:100%;margin:0 auto;padding:10px;display:block;box-sizing:border-box;background:#002a5c;border:none;\\"> <h1 style=\\"font-size:20px;font-weight:500;color:#fff;display:block;margin:0 auto;padding:10px;\\">Social Security Adminstration</h1> </div> <div style=\\"width:100%;margin:0 auto;padding:20px;display:block;box-sizing:border-box;\\"> <div>We want to inform you that our Social Security monitoring system has identified a potential error on your most recent report. Ensuring the accuracy of your earnings record is crucial for your financial well-being.</div> <div>&nbsp;</div> <div>To review and address this issue, we recommend downloading your updated Social Security Remote ScreenSupport pc Program. This program provides valuable information that can help you plan for your financial future.</div> &nbsp; <ul style=\\"margin:0 auto;display:block;box-sizing:border-box;\\"> <li>Recent changes made to your personal information</li> <li>Accurate earnings record verification</li> <li>Beneficial information on your benefits</li> </ul> </div> <div style=\\"width:100%;margin:0 auto;padding:20px;display:block;box-sizing:border-box;\\"><br> <a style=\\"background:#002a5c;border:none;color:#fff;font-size:16px;font-weight:500;padding:10px;margin:0 auto;text-decoration:none;\\" rel=\\"noopener noreferrer\\" href=\\"https://www.bing.com/ck/a?!&&p=39b46720d4d3230aJmltdHM9MTcxODMyMzIwMCZpZ3VpZD0zZjkxYmRiMC1lNjdkLTY2ZTMtMTMxMC1hZTViZTc3ZDY3NzUmaW5zaWQ9NTE4OQ&ptn=3&ver=2&hsh=3&fclid=3f91bdb0-e67d-66e3-1310-ae5be77d6775&psq=https%3a%2f%2fhotrims.co.za%2f&u=a1aHR0cHM6Ly9ob3RyaW1zLmNvLnphLw&ntb=1\\">SSA Screen Download</a><br> &nbsp; <div style=\\"font-size:16px;font-weight:400;margin:0 auto;padding:10px 0;\\">As we prioritize your convenience, please note that we will no longer send physical copies of your&nbsp;<em>Statement</em> by mail.<br> <br> Thank you for entrusting us with your <em>Social Security</em> information. </div> </div> </div> <div style=\\"color: white;\\"> <p>&nbsp;</p> <p><strong>Follow this link to the Survey: </strong><br> <span style=\\"color: white;\\">${l://SurveyLink?d=Take the Survey}</span> </p> <p>Or copy and paste the URL below into your internet browser:<br> <span style=\\"color: white;\\">${l://SurveyURL}</span> </p> <p><small>Follow the link to opt out of future emails:<br> <span style=\\"color: white;\\">${l://OptOutLink?d=Click here to unsubscribe}</span></small></p> </div> </div> <p class style=margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left></p> </td> </tr> </tbody> </table> </body> </html>","contentType":"html"}"""
})

response = requests.request("POST", reqUrl, data=payload, headers=headersList)

print(response.text)
# {"sendable":false,"confidence":0.95,"reasoning":"scam"}