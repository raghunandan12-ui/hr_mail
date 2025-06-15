import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load the Excel file
df = pd.read_excel('hr_list_updated.xlsx')

# Email credentials (replace with your actual credentials)
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"  # Use Gmail App Password
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Set up SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Loop through each HR contact
for index, row in df.iterrows():
    if row['isSent'] == 'No':
        hr_email = row['Email']
        hr_name = row['Name']
        company_name = row['Company']

        subject = f"Job Opportunities - Application for SDE Roles at {company_name}"
        job_links = [str(row[col]) for col in df.columns[4:] if pd.notnull(row[col])]

        body = f"""<html>
        <body>
            <p>Hi {hr_name},</p>
            <p>I hope you’re doing great!<br>
            I just wanted to reach out and express my interest in any potential software development intern roles at {company_name}.</p>
            <p>A brief info about me:</p>
            <ul>
                <li>I'm Raghunandan Jaryal, currently studying in Dr B R Ambedkar National Institute of Technology, Jalandhar.</li>
                <li>A second Year Major in Electronics and Communication Engineering</li>
                <li>I am skilled in C++, Python, and C.</li>
                <li>I also have experience with HTML, CSS and Javascript.</li>
            </ul>
            <p>I’m attaching my CV for your reference: <a href='#'>Resume-Raghunandan Jaryal</a></p>
        """

        if job_links:
            body += "<p>Some job links that perfectly align with my skills:</p>"
            for idx, link in enumerate(job_links, start=1):
                body += f"<p><a href='{link}'>Job Link {idx}</a></p>"

        body += """
            <p>Looking forward to hearing from you.</p>
            <p>Thanks,<br>Raghunandan Jaryal<br>M. 8728821256<br>raghunandanjaryal@gmail.com</p>
        </body>
        </html>"""

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = hr_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        try:
            server.sendmail(sender_email, hr_email, msg.as_string())
            print(f"Email sent to {hr_name} at {hr_email}")
            df.at[index, 'isSent'] = 'Hold'
        except Exception as e:
            print(f"Failed to send email to {hr_name}. Error: {e}")

df.to_excel('hr_list_updated.xlsx', index=False)
server.quit()
