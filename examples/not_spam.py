# Example (fake) but realistic Email Confirmation
import requests
import json

reqUrl = "https://api.contiguity.co/inference/ai/lingo-105b-beta/detect"

headersList = {
 "Accept": "*/*",
 "Authorization": "Token XXXXXXXXXXXXX",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "text": """{"recipient": "r------u@gm--l.com", "from": "Threads By Meta, "body": "<!doctypehtml><html lang=en xmlns=http://www.w3.org/1999/xhtml xmlns:o=urn:schemas-microsoft-com:office:office xmlns:v=urn:schemas-microsoft-com:vml><title>Welcome to Threads, by Meta</title><!--[if !mso]><!-- --><meta content="IE=edge"http-equiv=X-UA-Compatible><!--<![endif]--><meta content="text/html; charset=UTF-8"http-equiv=Content-Type><meta content="width=device-width,initial-scale=1"name=viewport><style>#outlook a{padding:0}body{margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}table,td{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0}img{border:0;height:auto;line-height:100%;outline:0;text-decoration:none;-ms-interpolation-mode:bicubic}p{display:block;margin:13px 0}</style><!--[if mso]><xml><o:officedocumentsettings><o:allowpng><o:pixelsperinch>96</o:pixelsperinch></o:officedocumentsettings></xml><![endif]--><!--[if lte mso 11]><style>.mj-outlook-group-fix{width:100%!important}</style><![endif]--><!--[if !mso]><!--><link href="https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@400;500;600&display=swap"rel=stylesheet><link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap"rel=stylesheet><style>@import url(https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@400;500;600&display=swap);@import url(https://fonts.googleapis.com/css2?family=Montserrat&display=swap);</style><!--<![endif]--><style>@media only screen and (min-width:480px){.mj-column-per-100{width:100%!important;max-width:100%}}</style><style>@media only screen and (max-width:480px){table.mj-full-width-mobile{width:100%!important}td.mj-full-width-mobile{width:auto!important}}</style><style>a,span,td,th{-webkit-font-smoothing:antialiased!important;-moz-osx-font-smoothing:grayscale!important}</style><body style=background-color:#171919><div style=display:none;font-size:1px;color:#fff;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden>Welcome to Threads, a new social platform by Meta</div><div style=background-color:#171919><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 align=center style=width:600px width=600><tr><td style=line-height:0;font-size:0;mso-line-height-rule:exactly><![endif]--><div style="margin:0 auto;max-width:600px"><table border=0 cellpadding=0 cellspacing=0 role=presentation style=width:100% align=center><tr><td style="direction:ltr;font-size:0;padding:20px 0;padding-bottom:0;text-align:center"><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 role=presentation><tr><td style=vertical-align:middle;width:600px><![endif]--><div style=font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100% class="mj-column-per-100 mj-outlook-group-fix"><table border=0 cellpadding=0 cellspacing=0 role=presentation style=vertical-align:middle width=100%><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=center><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-collapse:collapse;border-spacing:0><tr><td style=width:150px><img alt=Logo height=auto src=https://pngimg.com/d/meta_PNG7.png style=border:0;display:block;outline:0;text-decoration:none;height:auto;width:100%;font-size:14px width=150></table></table></div><!--[if mso | IE]><![endif]--></table></div><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 align=center style=width:600px width=600><tr><td style=line-height:0;font-size:0;mso-line-height-rule:exactly><![endif]--><div style="margin:0 auto;max-width:600px"><table border=0 cellpadding=0 cellspacing=0 role=presentation style=width:100% align=center><tr><td style="direction:ltr;font-size:0;padding:20px 0;text-align:center"><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 role=presentation><tr><td style=vertical-align:top;width:600px><![endif]--><div style=font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100% class="mj-column-per-100 mj-outlook-group-fix"><table border=0 cellpadding=0 cellspacing=0 role=presentation style=vertical-align:top width=100%><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=center><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-collapse:collapse;border-spacing:0><tr><td style=width:550px><img alt="welcome image"height=auto src=https://ouch-cdn.icons8.com/preview/45/ae8b07c8-d018-4205-8011-29f727059dd7.png style=border:0;display:block;outline:0;text-decoration:none;height:auto;width:100%;font-size:14px width=550></table><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=left><div style=font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#ddd><h1 style="margin:0;font-size:46px;line-height:60px;font-weight:600;font-family:'Inknut Antiqua',Helvetica,Arial,sans-serif">Lets create something amazing!</h1></div><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=left><div style=font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:18px;font-weight:400;line-height:24px;text-align:left;color:#ddd><p style=margin:0>Welcome to Threads, John Doe! Before we get started, please confirm your email address.</div><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=left vertical-align=middle><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-collapse:separate;line-height:100%><tr><td style="border:none;border-radius:3px;cursor:auto;mso-padding-alt:10px 25px;background:#fff"align=center bgcolor=#ffffff role=presentation valign=middle><a href=https://google.com style="display:inline-block;background:#fff;color:#000;font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:14px;font-weight:400;line-height:30px;margin:0;text-decoration:none;text-transform:none;padding:10px 25px;mso-padding-alt:0;border-radius:3px"target=_blank>Confirm my Email</a></table><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=left><div style=font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:16px;font-weight:400;line-height:24px;text-align:left;color:#999><p style=margin:0>Have questions or need help? Email us at <a href=# style=color:#fff;text-decoration:none;font-weight:700>threads@meta.com</a></div></table></div><!--[if mso | IE]><![endif]--></table></div><!--[if mso | IE]><![endif]--><table border=0 cellpadding=0 cellspacing=0 role=presentation style=background:#000;background-color:#000;width:100% align=center><tr><td><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 align=center style=width:600px width=600><tr><td style=line-height:0;font-size:0;mso-line-height-rule:exactly><![endif]--><div style="margin:0 auto;max-width:600px"><table border=0 cellpadding=0 cellspacing=0 role=presentation style=width:100% align=center><tr><td style="direction:ltr;font-size:0;padding:20px 0;text-align:center"><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 role=presentation><tr><td style=vertical-align:top;width:600px><![endif]--><div style=font-size:0;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100% class="mj-column-per-100 mj-outlook-group-fix"><table border=0 cellpadding=0 cellspacing=0 role=presentation style=vertical-align:top width=100%><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=center><div style=font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:16px;font-weight:400;line-height:24px;text-align:center;color:#999><a href=# style=text-decoration:none;color:#fff;font-weight:400 class=footer-link>Support</a>   |   <a href=# style=text-decoration:none;color:#fff;font-weight:400 class=footer-link>Privacy Policy</a></div><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=center><div style=font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:16px;font-weight:400;line-height:24px;text-align:center;color:#999>1 Hacker WyMenlo Park, CA 94025</div><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=center><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 role=presentation align=center><tr><td><![endif]--><table border=0 cellpadding=0 cellspacing=0 role=presentation style=float:none;display:inline-table align=center><tr><td style=padding:4px><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-radius:3px;width:24px><tr><td style=font-size:0;height:24px;vertical-align:middle;width:24px><a href=# style=color:#fff;text-decoration:none;font-weight:700 target=_blank><img alt=twitter-logo height=24 src=../../../images/social/light/twitter-logo-transparent-light.png style=border-radius:3px;display:block width=24></a></table></table><!--[if mso | IE]><td><![endif]--><table border=0 cellpadding=0 cellspacing=0 role=presentation style=float:none;display:inline-table align=center><tr><td style=padding:4px><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-radius:3px;width:24px><tr><td style=font-size:0;height:24px;vertical-align:middle;width:24px><a href=# style=color:#fff;text-decoration:none;font-weight:700 target=_blank><img alt=facebook-logo height=24 src=../../../images/social/light/facebook-logo-transparent-light.png style=border-radius:3px;display:block width=24></a></table></table><!--[if mso | IE]><td><![endif]--><table border=0 cellpadding=0 cellspacing=0 role=presentation style=float:none;display:inline-table align=center><tr><td style=padding:4px><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-radius:3px;width:24px><tr><td style=font-size:0;height:24px;vertical-align:middle;width:24px><a href=# style=color:#fff;text-decoration:none;font-weight:700 target=_blank><img alt=instagram-logo height=24 src=../../../images/social/light/instagram-logo-transparent-light.png style=border-radius:3px;display:block width=24></a></table></table><!--[if mso | IE]><td><![endif]--><table border=0 cellpadding=0 cellspacing=0 role=presentation style=float:none;display:inline-table align=center><tr><td style=padding:4px><table border=0 cellpadding=0 cellspacing=0 role=presentation style=border-radius:3px;width:24px><tr><td style=font-size:0;height:24px;vertical-align:middle;width:24px><a href=# style=color:#fff;text-decoration:none;font-weight:700 target=_blank><img alt=dribbble-logo height=24 src=../../../images/social/light/linkedin-logo-transparent-light.png style=border-radius:3px;display:block width=24></a></table></table><!--[if mso | IE]><![endif]--><tr><td style=font-size:0;word-break:break-word><!--[if mso | IE]><table border=0 cellpadding=0 cellspacing=0 role=presentation><tr><td style=vertical-align:top;height:20px height=20><![endif]--><div style=height:20px> </div><!--[if mso | IE]><![endif]--><tr><td style="font-size:0;padding:10px 25px;word-break:break-word"align=center><div style=font-family:Montserrat,Helvetica,Arial,sans-serif;font-size:16px;font-weight:400;line-height:24px;text-align:center;color:#999>Update your <a href=https://google.com style=text-decoration:none;color:#fff;font-weight:400 class=footer-link>email preferences</a> to choose the types of emails you receive, or you can <a href=https://google.com style=text-decoration:none;color:#fff;font-weight:400 class=footer-link>unsubscribe </a>from all future emails.</div></table></div><!--[if mso | IE]><![endif]--></table></div><!--[if mso | IE]><![endif]--></table></div>"}"""
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)
# {"sendable":true,"confidence":0.98,"reasoning":"administrative"}