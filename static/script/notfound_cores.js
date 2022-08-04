function corparahexa(cor)
{
    var colours = {
    "black":"#616161",
    "blue":"#82ffff",
    "brown":"#c58a61",
    "gray":"#999999",
    "green":"#c1ff82",
    "pink":"#ff82ff",
    "purple":"#c182ff",
    "red": "#ff3030",
    "white":"#eaeaea",
    "yellow":"#ffff82"};

    if (typeof colours[cor.toLowerCase()] != 'undefined')
        return colours[cor.toLowerCase()];

    return false;
}

document.body.style.backgroundColor = corparahexa(color);