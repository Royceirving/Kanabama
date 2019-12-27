
@app.route('/newstory', methods=['POST','GET'])
def newstory():

    if(not current_user.is_active):
        return redirect('/index')

    form = NewStoryForm()
    if form.validate_on_submit():
        story_name = form.name_field.data.replace("'","")

        description = form.description_field.data.replace("'","")

        priority = int(form.priority_field.data)

        date = form.date_field.data

        state = 0

        email = form.email.data

        conn = sqlite3.connect(DATABASE_FILENAME)
        cursor = conn.cursor()

        cursor.execute(commit_story_generator(
            current_user.teamname, story_name, description,
            priority, date, state
        ))
        conn.commit()

        if(email != ""):
            message = Mail(
                from_email='kanabama.noreply@gmail.com',
                to_emails=email,
                subject='New story: {}'.format(story_name),
                html_content='''Story Created by:{}<br>
                Due Date: {}<br>
                <br><br>
                Story Description: {}'''.format(current_user.username,date,description)
            )
            send_grid_client = SendGridAPIClient(SENDGRID_API_KEY)
            resp = send_grid_client.send(message)
            if (resp.status_code != 202):
                print("Email Failed to send")

        return redirect('/storyboard')
    else:
        return render_template('/newstory.html',form=form)
        