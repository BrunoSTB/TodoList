function new_post_it() {
    while (true) {
        var newItem = document.getElementById('user_input').value;
        if (newItem === null || newItem === "") {
            break;
        }
        else if (newItem.length > 80) {
            alert("Text is bigger than the allowed!")
            break;
        }
        document.getElementById("current").innerHTML += "<li class='m-3 card " + random_color() + "'><div class='d-flex justify-content-around m-0 p-0'><button onclick='remove_self(this)' class='btn btn-sm'><b>x</b></button><input class='ml-auto' onclick='togglePalette(this)' id='colorPick' type='checkbox'>" + colorPalette() + "</div><div class='card-body px-1 pb-2 pt-0'>" + newItem + "</div></li>";
        document.getElementById('user_input').value = '';
        break;
    }
}

function delete_all() {
    if (confirm('Are you sure you want to delete all Postits?')) {
        var chosen = document.getElementById('current');
        chosen.remove()
        document.getElementById('parag').innerHTML += "<ol class='d-flex flex-row justify-content-center flex-wrap' id='current'></ol>";
    }
}

function remove_self(el) {
    var element = el.parentElement.parentElement;
    element.remove();
}

function getPrevious(el) {
    var element = el.previousSibling;
    return element;
}

function togglePalette(el) {
    var checkbox = el;
    var toggleDiv = el.nextSibling;
    if (checkbox.checked == true) {
        toggleDiv.style.display = 'inline-block';
    }

    else {
        toggleDiv.style.display = 'none';
    }
}


function random_color() {
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

function changeColor(element, color) {
    var element = element.parentElement.previousSibling.parentElement.parentElement;

    if(color === 1) {
        element.style.backgroundColor = "#2a9d8f";
    }
    else if (color === 2) {
        element.style.backgroundColor = "#e9c46a";
    }
    else if (color ===  3) {
        element.style.backgroundColor = "#f4a261";
    }
    else if (color === 4) {
        element.style.backgroundColor = "#e76f51";
    }
}

function colorPalette() {
    return "<div class='m-0 px-1 card' id='palette' ><i onclick='changeColor(this, 1)' class='bi bi-square-fill d-block'></i><i onclick='changeColor(this, 2)' class='bi bi-square-fill d-block'></i><i onclick='changeColor(this, 3)' class='bi bi-square-fill d-block'></i><i onclick='changeColor(this, 4)' class='bi bi-square-fill d-block'></i> </div>";
}
