#  Automated HR Outreach Script Using Python

This is a Python automation tool designed to send **personalized internship/job emails** to HR professionals or recruiters listed in an Excel sheet. It’s ideal for students like **Raghunandan Jaryal** who want to apply to multiple companies efficiently and professionally.

---

##  Features

- Sends custom HTML emails to each HR contact
-  Reads contact info & job links from an Excel file
-  Prevents duplicate emails using a `isSent` column
-  Easy to configure with `.env` for secure login
-  Designed for outreach related to SDE Intern roles

---

##  Real-Life Use Case (Example)

> Hi, I'm **Raghunandan Jaryal**, a second-year B.Tech student at **Dr B R Ambedkar NIT Jalandhar**, pursuing **ECE**. I’m reaching out to HRs at companies like **Zoho**, **TCS**, and **Infosys** for SDE Intern opportunities.  
> Instead of writing 50 emails manually, I use this script to send **personalized, respectful messages** with job links and a resume reference.

---

##  Project Structure


---

##  Excel File Format – `hr_list.xlsx`

| Name         | Email              | Company      | isSent | Job Link 1            | Job Link 2            |
|--------------|--------------------|--------------|--------|------------------------|------------------------|
| Priya Mehra  | priya@zoho.com     | Zoho Corp    | No     | https://zoho.com/job1  | https://zoho.com/job2  |
| Raj Sharma   | raj@tcs.com        | TCS          | No     | https://tcs.com/dev    |                        |

- `Name`, `Email`, `Company`, and `isSent` are required.
- Additional columns like `Job Link 1`, `Job Link 2`, etc., are optional.
- Set `isSent` to `No` initially. The script will update it to `Yes` after sending.

---


