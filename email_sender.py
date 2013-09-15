#!/usr/bin/python

# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

myName = 'Robert Nederhorst'
myEmail = 'dmca@throb.net'
myContact= '21456 Salamanca Ave, Woodland Hills, CA 91364 USA, +1-310-818-3806'   
productLink = ''

illegalLink = 'http://www.todaytorrents.com/download/Gnomon-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-with-Rob-Nederhorst-5977350.html'

productURL = [
    'http://www.thegnomonworkshop.com/store/product/987/',
    'http://www.thegnomonworkshop.com/store/product/973/'
]

mainSite = illegalLink.split('//')[1].split('/')[0].replace('www.','')

baseEmailAddresses = [
    'admin',
    'dmca',
    'info',
    'abuse',
    'support'
]

COMMASPACE = ', '
allEmails = []
for email in baseEmailAddresses:
    allEmails.append('%s@%s' % (email, mainSite))
toEmail = COMMASPACE.join(allEmails)

electronic_sig = myName + '\n' + myContact + '\n' + myEmail

for link in productURL:
    productLink = '%s\n%s' % (productLink,link)

body = '''  
My name is %s and I am the Author of this material.  A website that your company hosts (according to WHOIS information) is infringing on at least one copyright owned by my intellectual property.\n\n
An article was copied onto your servers without permission. The original material, to which we own the exclusive copyrights, can be found at:\n%s\n
The unauthorized and infringing copy can be found at:\n%s\n
This letter is official notification under Section 512(c) of the Digital Millennium Copyright Act (.DMCA.), and I seek the removal of the aforementioned infringing material from your servers. I request that you immediately notify the infringer of this notice and inform them of their duty to remove the infringing material immediately, and notify them to cease any further posting of infringing material to your server in the future.\n\n
Please also be advised that law requires you, as a service provider, to remove or disable access to the infringing materials upon receiving this notice. Under US law a service provider, such as yourself, enjoys immunity from a copyright lawsuit provided that you act with deliberate speed to investigate and rectify ongoing copyright infringement. If service providers do not investigate and remove or disable the infringing material this immunity is lost. Therefore, in order for you to remain immune from a copyright infringement action you will need to investigate and ultimately remove or otherwise disable the infringing material from your servers with all due speed should the direct infringer, your client, not comply immediately.\n
I am providing this notice in good faith and with the reasonable belief that rights my company owns are being infringed. Under penalty of perjury I certify that the information contained in the notification is both true and accurate, and I have the authority to act on behalf of the owner of the copyright(s) involved.\n
Should you wish to discuss this with me please contact me directly.\n\n
Thank you.\n\n
Electronic Signature :\n
%s
''' % (myName,productLink,illegalLink,electronic_sig)

msg = MIMEText(body)

you = 'throb@throb.net'
msg['Subject'] = 'Notice of Copyright Infringement'
msg['From'] =myEmail
msg['To'] = toEmail

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(myEmail, allEmails, msg.as_string())
s.quit()


