   
@app.route('/updatestory/<story_id_and_place>',methods=["GET"])
def updatestory(story_id_and_place):
    # text delimiter to split will be a +
    # example 5+2 => set story of id 5 to state 2
    data = story_id_and_place.split('+')
    story_id = int(data[0])
    state = int(data[1])
    if(state <= 0):
        state = 0
    elif(state >= 3):
        state = 3

    try:
        conn = sqlite3.connect(DATABASE_FILENAME)
        cursor = conn.cursor()

        query = update_story_to_state_in_team_generator(current_user.teamname,story_id,state)
        resp = cursor.execute(query)
        resp = resp.fetchall()
        conn.commit()
        return json.dumps({'succecss':True}),200,{'ContentType':'application/json'}
    except BaseException:
        return json.dumps({'fail':False}),500,{'ContentType':'application/json'}
        
