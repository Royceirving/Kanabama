
@app.route('/storyboard')
def storyboard():

    if( not current_user.is_active):
        return redirect("/index")

    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    resp = cursor.execute(get_stories_for_team(current_user.teamname))
    stories = resp.fetchall()
    outp = []
    for story in stories:
        temp = list(story)
        if(temp[3] == 0):
            temp[3] = "High"
        if(temp[3] == 1):
            temp[3] = "Medium"
        if(temp[3] == 2):
            temp[3] = "Low"
        outp.append(temp)
    stories = tuple(outp)
    return render_template('/storyboard.html', stories=stories)

