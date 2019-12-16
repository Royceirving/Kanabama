

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


function allowDrop(e) {
    //console.log("Allowing drop");
    e.preventDefault();
}

function drag(e) {
    //console.log("Dragging");
    e.dataTransfer.setData("move", e.target.id);
}

function drop(e) {
    //console.log("Dropping");
    e.preventDefault();
    var data = e.dataTransfer.getData("move");
    e.target.appendChild(document.getElementById(data));
    var s = data+"+";
    if(e.target.id.includes("-col")){
        s = s + String(state_switch(e.target.id));
    } else if (e.target.parentNode.id.includes("-col")) {
        s = s + String(state_switch(e.target.parentNode.id));
    }
    else{
        s = s + state_switch(e.target.parentElement.parentElement.id);
    }
    update_story(s);
}

function state_switch(name) {
    if(name=="backlog-col") {
        return "0";
    }
    else if(name=="progress-col") {
        return "1";
    }
    else if(name=="review-col") {
        return "2";
    }
    else if(name=="done-col") {
        return "3";
    }
    return -1;
}
