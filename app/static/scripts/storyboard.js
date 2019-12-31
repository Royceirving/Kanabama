

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
