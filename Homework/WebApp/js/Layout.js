Layout = {};

Layout.createHeadline = function(title, height, parent)
{
    var containerDiv = WebLibSimple.createDivHeight(0, 0, 0, height, null, parent);
    containerDiv.style.borderRadius = "25px";
    containerDiv.style.border = "3px solid #000000";

    var headline = WebLibSimple.createAnyAppend("h1", containerDiv);
    headline.innerHTML       = title;
    headline.style.textAlign = "center";
    // headline.style.color     = "#ffffff";
    headline.style.color     = "#000000";

    // WebLibSimple.setBGColor(containerDiv, "#6b6b6b");
}

Layout.createLabelCircle = function(title, size, color, parent, eventFunct)
{
    var fontWeight = "normal";

    var div = Layout.createCircle(title, size, color, parent, eventFunct);
    div.style.fontWeight = fontWeight;

    var span = WebLibSimple.createAnyAppend("span", div);
    span.innerHTML          = title;
    span.style.fontSize     = "1px";
    span.style.fontWeight   = fontWeight;

    var spansize = 2;
    var border   = 50;

    // console.log("title:" + title);

    while (((span.offsetWidth + border) < size) && ((span.offsetHeight + border) < size))
    {
        // console.log("size: " + size);
        // console.log("spansize: " + spansize);
        // console.log("span.offsetWidth:  " + span.offsetWidth);
        // console.log("span.offsetHeight: " + span.offsetHeight);
        //
        span.style.fontSize = spansize + "px";
        spansize++;

        if (spansize > 1000) break;
    }

    div.style.fontSize   = spansize + "px";
    div.style.lineHeight = size + "px";

    //
    // Nuke span
    //

    span.style.display = "none";
    span = null;

    return div;
}

Layout.createCircle = function(title, size, color, parent, eventFunct)
{
    var div = WebLibSimple.createAnyAppend("div", parent);
    div.style.borderRadius = "50%";
    div.style.width        = size + "px";
    div.style.height       = size + "px";
    div.style.lineHeight   = size + "px";
    div.style.fontSize     = (size * 0.15) + "px";
    div.style.textAlign    = "center";
    div.style.color        = "#ffffff";
    div.style.display      = "inline-block";
    div.style.overflow     = "hidden";
    // div.style.border       = "1px solid #000000";
    // div.style.borderBottom = "1px solid #000000";

    if (eventFunct != null)
    {
        div.style.cursor = "pointer";
    }


    div.onclick   = eventFunct;
    div.innerHTML = title;

    WebLibSimple.setBGColor(div, color);

    return div;
}

Layout.createQrCircle = function(size, color, bgcolor, data, parent)
{
    var div = WebLibSimple.createAnyAppend("div", parent);
    div.style.borderRadius = "50%";
    div.style.display      = "inline-block";
    div.style.width        = size + "px";
    div.style.height       = size + "px";
    WebLibSimple.setBGColor(div, bgcolor);

    var border = 18;
    var widthHeight = (100 - (border * 2)) / 100 * size;
    // var img = WebLibSimple.createImg(border, border, border, border, null, div);

    var img = WebLibSimple.createAnyAppend("img", div);

    img.style.left   = border + "%";
    img.style.right  = border + "%";
    img.style.top    = border + "%";
    img.style.bottom = border + "%";
    img.style.position = "absolute";
    // img.style.cursor = "none";

    var qrcolor  = color.substring(1, 7);
    var qrbcolor = bgcolor.substring(1, 7);

    img.src = "https://api.qrserver.com/v1/create-qr-code/?" +
        "data=" + data +
        "&size=" + widthHeight + "x" + widthHeight +
        "&margin=1" +
        "&color=" + qrcolor +
        "&bgcolor=" + qrbcolor;

    // WebLibSimple.setBGColor(div, "#c90386");
}

Layout.createCenterCircle = function(title, size, color, parent, eventFunct)
{
    var center = WebLibSimple.createAnyAppend("center", parent);
    var div    = Layout.createCircle(title, size, color, center, eventFunct);

    return div;
}

Layout.createMenuPoint = function(title, size, color, parent, event)
{
    var paddingDiv = WebLibSimple.createAnyAppend("div", parent);
    paddingDiv.style.display = "inline-block";
    paddingDiv.style.padding = "20px";

    if (event == null)
    {
        color = "#6b6b6b";
    }

    var div = Layout.createCircle(title, size, color, paddingDiv, event);

    return div;
}
