def email_content(token, url):

    if url.split("/")[-1] == "reset":  # (reset password)

        callback_url = f"{url}?token={token}"

        text = f"""
            Please click in the following link to reset your password.\n
            {callback_url}
            """

        html = f"""
            <html>
                <head><head>
                <body>
                <p>Please click in the following link to reset your password.</p>

                <a href="{callback_url}">{callback_url}</a>
                </body>
            </html>
            """

        subject = "Reset password for activities-app"

    else:  # (confirm email)

        callback_url = f"{url}?token={token}"

        text = f"""
            Please click in the following link to verify your email.\n
            {callback_url}
            """

        html = f"""
            <html>
                <head><head>
                <body>
                <p>Please click in the following link to verify your email.</p>
                <a href="{callback_url}">{callback_url}</a>
                </body>
            </html>
            """

        subject = "Confirm your email"

    body = dict({"text": text, "html": html})

    return dict({"subject": subject, "body": body})
