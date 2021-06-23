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
        document.getElementById("current").innerHTML += "<li class='m-2 card " + random_color() + "'><div class='container-fluid m-0 p-0 '><button onclick='remove_self(this)' class='btn btn-sm'><b>x</b></button></div><div class='card-body px-1 pb-2 pt-0'>" + newItem + "</div></li>";
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
