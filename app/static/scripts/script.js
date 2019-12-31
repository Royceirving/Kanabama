

function delete_story(story_id){
    let go = confirm("Are you sure you want to delete this story?");
    if(!go){
        return;
    }
    $.get( "/deletestory/"+story_id, function (){
        window.location.reload();
    });
}

function toggle_signup(){
    cb = document.getElementById('signup_checkbox')
    if(cb.checked){
        document.getElementById("create_team_div").hidden=false;
        document.getElementById("team_config").innerHTML="Create Team";
    }
    else{
        document.getElementById("create_team_div").hidden=true;
        document.getElementById("team_config").innerHTML="Join Team";
    }
}

function update_story(story_id_and_place){
    //console.log(story_id_and_place);
    $.get( "/updatestory/"+story_id_and_place, function (){
        window.location.reload();
    });
}
