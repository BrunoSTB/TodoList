
function toggle_Palette(el) {
    var checkbox = el;
    var toggleDiv = el.nextElementSibling;
    if (checkbox.checked == true) {
        toggleDiv.style.display = 'inline-block';
    }

    else {
        toggleDiv.style.display = 'none';
    }
}
