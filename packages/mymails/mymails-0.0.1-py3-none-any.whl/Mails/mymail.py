def send_email(receiver_email: str, sub: str = 'Program Info', text: str = '', sender: str or None = None, password: str or None = None, img: str or list or None = None, attach: str or list or None = None):
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    import smtplib
    import os
    # initialize connection to our
    # email server, we will use gmail here
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    # Login with your email and password
    if sender is None or password is None:
        sender = 'botmails148@gmail.com'
        password = 'jpoakatmrgsbgxrc'
    smtp.login(sender, password)

    def message(subject: str = "Python Notification",
                text: str = "", img=None,
                attachment=None):
        '''Send our email message 'msg' to our boss'''
        # build message contents
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        if img is not None:
            # Check whether we have the lists of images or not!
            if type(img) is not list:
                img = [img]

            for one_img in img:
                # read the image binary data
                img_data = open(
                    f"{os.getcwd()}/images/{one_img}", 'rb').read()
                # Attach the image data to MIMEMultipart
                # using MIMEImage, we add the given filename use os.basename
                msg.attach(MIMEImage(img_data,
                                     name=os.path.basename(one_img)))

        # Check whether we have the lists of attachments or not!
        if attachment is not None:
            # Check whether we have the lists of attachments or not!
            if type(attachment) is not list:
                attachment = [attachment]

            for one_attachment in attachment:
                with open(one_attachment, 'rb') as f:
                    # Read in the attachment
                    # using MIMEApplication
                    file = MIMEApplication(
                        f.read(),
                        name=os.path.basename(one_attachment)
                    )
                file['Content-Disposition'] = f'attachment;\filename="{os.path.basename(one_attachment)}"'

                # At last, Add the attachment to our message object
                msg.attach(file)
        return msg

    msg = message(subject=sub, text=text,
                  img=img, attachment=attach)

    # Make a list of emails, where you wanna send mail
    to = receiver_email

    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr=sub,
                  to_addrs=to, msg=msg.as_string())

    # Finally, don't forget to close the connection
    smtp.quit()
