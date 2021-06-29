// Create a new post it
function new_Post_It() {
    while ( true ) {

        var content = document.getElementById('user_input').value;

        if (content === null || content === "") {
            break;
        }
        else if (content.length > 80) {
            alert("Text is bigger than the allowed!")
            break;
        }


        // Modifies HTML to add the postit as a <li> card. 
        document.getElementById("current").innerHTML +=
            "<li class='m-3 card " + random_Color() + "'>" +
                "<div class='d-flex justify-content-around m-0 p-0'>" +
                    "<button onclick='remove_Self(this)' class='btn btn-sm'><b>x</b></button>" +
                    "<input class='ml-auto' onclick='toggle_Palette(this)' id='colorPick' type='checkbox'>" +
                    "<div class='m-0 px-1 card' id='palette' >" +
                        "<i onclick='change_Color(this, 1)' class='bi bi-square-fill d-block'></i>" +
                        "<i onclick='change_Color(this, 2)' class='bi bi-square-fill d-block'></i>" +
                        "<i onclick='change_Color(this, 3)' class='bi bi-square-fill d-block'></i>" +
                        "<i onclick='change_Color(this, 4)' class='bi bi-square-fill d-block'></i>" +
                    "</div>" + 
                "</div>" +
                "<div class='card-body px-1 pb-2 pt-0'>" + 
                    content +
                "</div>" +
            "</li>";   

        // Clears input
        document.getElementById('user_input').value = '';
        break;
    }
}

// Deletes all post its
function delete_All() {
    if (confirm('Are you sure you want to delete all Postits?')) {
        // Deletes the ordered list and replaces it with an empty copy
        
        var chosen = document.getElementById('current');
        chosen.remove()
        document.getElementById('parag').innerHTML += "<ol class='d-flex flex-row justify-content-center flex-wrap' id='current'></ol>";
    }
}

// Remove a post it
function remove_Self(el) {
    var element = el.parentElement.parentElement;
    element.remove();
}


// Auxiliary Functions ----

// For functionality --

// Toggles the palette menu
function toggle_Palette(el) {
    var checkbox = el;
    var toggleDiv = el.nextSibling;
    if (checkbox.checked == true) {
        toggleDiv.style.display = 'inline-block';
    }

    else {
        toggleDiv.style.display = 'none';
    }
}

// In the palette menu, allows the user to change the post it color
function change_Color(element, color) {
    var element = element.parentElement.previousSibling.parentElement.parentElement;

    if (color === 1) {
        element.style.backgroundColor = "#2a9d8f";
    }
    else if (color === 2) {
        element.style.backgroundColor = "#e9c46a";
    }
    else if (color === 3) {
        element.style.backgroundColor = "#f4a261";
    }
    else if (color === 4) {
        element.style.backgroundColor = "#e76f51";
    }
}

// For cleaner code --

// Get a random collor (used for random color postit when newly created)
function random_Color() {
    randomize = Math.floor(Math.random() * (5 - 1)) + 1;
    switch (randomize) {
        case 1:
            return "bg-blueish";
        case 2:
            return "bg-yellowish";
        case 3:
            return "bg-orangeish";
        case 4:
            return "bg-redish";
    }
}


