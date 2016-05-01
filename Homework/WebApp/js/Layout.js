Layout = {};

Layout.createHeadline = function(title, height, parent)
{
    var containerDiv = WebLibSimple.createDivHeight(0, 0, 0, height, null, parent);
    containerDiv.style.borderRadius = "25px";

    var headline = WebLibSimple.createAnyAppend("h1", containerDiv);
    headline.innerHTML       = title;
    headline.style.textAlign = "center";
    headline.style.color     = "#ffffff";

    WebLibSimple.setBGColor(containerDiv, "#6b6b6b");
}

// Layout.createCircleAbsolute = function(title, top, left, size, color, parent, eventFunct)
// {
//     var div = WebLibSimple.createDivWidHei(top, left, size, size, null, parent);
//     div.style.borderRadius = "50%";
//     div.style.lineHeight   = size + "px";
//     div.style.fontSize     = (size * 0.15) + "px";
//     div.style.textAlign    = "center";
//     div.style.color        = "#ffffff";
//
//     div.onclick   = eventFunct;
//     div.innerHTML = title;
//
//     WebLibSimple.setBGColor(div, color);
//
//     return div;
// }

Layout.createCircle = function(title, size, color, parent, eventFunct)
{
    // var div = WebLibSimple.createAnyAppend("span", parent);
    // div.style.fontSize     = "20px";
    // // div.style.textAlign    = "center";
    // div.style.color        = "#000000";
    // div.innerHTML          = "Subject";
    //
    // console.log(div.offsetWidth);
    // // console.log(div.offsetHeight);
    //
    // WebLibSimple.setBGColor(div, "#db4d1f");

    var div = WebLibSimple.createAnyAppend("div", parent);
    div.style.borderRadius = "50%";
    div.style.width        = size + "px";
    div.style.height       = size + "px";
    div.style.lineHeight   = size + "px";
    div.style.fontSize     = (size * 0.15) + "px";
    div.style.textAlign    = "center";
    div.style.color        = "#ffffff";
    div.style.cursor       = "pointer";
    div.style.display      = "inline-block";
    div.style.overflow     = "hidden";

    div.onclick   = eventFunct;
    div.innerHTML = title;

    WebLibSimple.setBGColor(div, color);

    return div;
}

Layout.createCenterCircle = function(title, size, color, parent, eventFunct)
{
    var center = WebLibSimple.createAnyAppend("center", parent);
    var div    = Layout.createCircle(title, size, color, center, eventFunct);

    return div;
}
