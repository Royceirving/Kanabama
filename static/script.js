

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

// Working GitHub API Code Below If Discord Does Not Work
const gitHubForm = document.getElementById('entername');
gitHubForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let usernameInput = document.getElementById('nameentered');
    let gitHubUsername = usernameInput.value;
    requestUserRepos(gitHubUsername);
})
function requestUserRepos(username){
    const api_get = new XMLHttpRequest();
    const url = `https://api.github.com/users/${username}/repos`;
    api_get.open('GET', url, true);
    api_get.onload = function () {
        const data = JSON.parse(this.response);
        for (let i in data) {
            let ul = document.getElementById('repolist');
            let li = document.createElement('li');
            li.classList.add('list-group-item')
            li.innerHTML = (`<p><strong>Repo:</strong> ${data[i].name}</p>
                <p><strong>Description:</strong> ${data[i].description}</p>
                <p><strong>URL:</strong> <a href="${data[i].html_url}">${data[i].html_url}</a></p>`);
            ul.appendChild(li);
        }
    }
    api_get.send();
}
