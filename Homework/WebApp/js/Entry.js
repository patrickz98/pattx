Entry = {};

Entry.nukeDimmerDiv = function()
{
    Entry.dimmerDiv.style.display = "none";
}

Entry.createDimmerDiv = function()
{
    console.log("create dimmer");
    var parent = Entry.parent;
    parent.style.overflow = "hidden";

    console.log("scrollTop:" + parent.scrollTop);

    Entry.dimmerDiv = WebLibSimple.createDivHeight(0, parent.scrollTop, 0, "100%", "dimemrDiv", parent);

    WebLibSimple.setBGColor(Entry.dimmerDiv, "#99000000");

    return Entry.dimmerDiv;
}

Entry.createDimmerCircleInput = function()
{
    var dimmerDiv = Entry.createDimmerDiv();

    var center = WebLibSimple.createAnyAppend("center", dimmerDiv);

    var containerDiv = WebLibSimple.createAnyAppend("div", center);
    containerDiv.style.height       = "600px";
    containerDiv.style.width        = "100px";

    containerDiv.style.border       = "1px solid black";
    containerDiv.style.borderRadius = "900px";
    // containerDiv.style.overflow     = "hidden";
    containerDiv.style.fontFamily   = "Ubuntu, Helvetica, Arial";

    WebLibSimple.setBGColor(containerDiv, "#ffffff");

    var border = 25;
    var contentDiv = WebLibSimple.createDiv(border, border, border, border, null, containerDiv);

    return contentDiv;
}

//
// Triangle
//

Entry.createTriangle = function(left, top, width, height, color, parent)
{
    var div = WebLibSimple.createDivWidHei(left, top - (height/2), width, height, null, parent);

    var canvas = WebLibSimple.createAnyAppend("canvas", div);
    canvas.style.position = "absolute";
    canvas.style.left     = "0px";
    canvas.style.right    = "0px";
    canvas.style.width    = "100%";
    canvas.style.height   = "100%";

    if(canvas.getContext)
    {
        var ctx = canvas.getContext("2d");

        ctx.fillStyle = color;
        ctx.beginPath();

        ctx.moveTo(0, 75);
        ctx.lineTo(300, 0);
        ctx.lineTo(300, 150);

        ctx.closePath();
        ctx.fill();
    }
}

Entry.exitInput = function(event)
{
    Option.nukeDimmerDiv();

    var target = event.target.target;
    var value  = Entry.input.value;
    console.log(value);

    if (value)
    {
        // WebLibSimple.setBGColor(target, "#3688d4");
        target.titleSpan.innerHTML = value;
        // Option.parent.data[ target.conf.optionKey ] = value;
    }
    else
    {
        // WebLibSimple.setBGColor(target, GlobalConf.colorGrey);
    }
}

Entry.openDialog = function(target)
{
    var dimmer = Edit.createDimmerCircleInput(target, null, Entry.parent);

    // var value = target.titleSpan.innerHTML;
    //
    // var center = WebLibSimple.createAnyAppend("center", dimmer);
    //
    // Entry.input = WebLibSimple.createAnyAppend("input", center);
    //
    // var input = Entry.input;
    // input.style.width        = "300px";
    // input.style.height       = "30px";
    // input.type               = "text";
    // input.value              = value;
    // input.style.textAlign    = "center";
    // input.style.borderRadius = "30px";
    // // WebLibSimple.setBGColor(input, "#9f9f9f");
    //
    // var div = WebLibSimple.createAnyAppend("div", dimmer);
    // div.style.paddingTop = "50px";
    //
    // var center = WebLibSimple.createAnyAppend("center", div);
    //
    // var backButton = Layout.createLabelCircle("Ok", 80, "#000000", center, Entry.exitInput);
    // backButton.target = target;
}

Entry.editEntry = function(event)
{
    // Teacher.topDiv.style.overflow = null;

    var target = event.target;

    if (target.root)
    {
        target = target.root;
    }

    Entry.openDialog(target);
}

Entry.nextEntryStart = 0;

Entry.getNextEntryStart = function()
{
    return Entry.nextEntryStart;
}

Entry.addEntry = function(event)
{
	var target = event.target;
	var root   = target.root;
	var parent = target.topDiv;

    var tmp = {
        "Name": "",
        "ShortName": "",
        "Subjects": "",
        "Notes": "",
        "School": ""
    };

    Entry.createEntry(tmp, parent, true);
    target.root.style.top = Entry.nextEntryStart + "px";
}

Entry.createEntryTag = function(tag, title, tagSize, index, parent)
{
    var paddingLeft = GlobalConf.tagMarginLeft

    var div = WebLibSimple.createDivHeight(paddingLeft, tagSize * index, 0, tagSize, null, parent);
    // WebLibSimple.setBGColor(div, "#4877a8");

    var text = WebLibSimple.createDiv(0, 0, 0, 0, null, div);
    // text.style.borderRadius = "30px";
    text.style.lineHeight   = div.offsetHeight + "px";
    text.style.fontSize     = GlobalConf.fontSize + "px";
    text.style.overflow     = "hidden";
    text.style.color        = "#ffffff";
    text.tag                = tag;
    text.title              = title;

    // text.style.textAlign    = "center";
    text.style.cursor       = "pointer";
    text.onclick            = Entry.editEntry;

    // WebLibSimple.setBGColor(text, "#4877a8");

    var span = WebLibSimple.createAnyAppend("span", text);
    span.innerHTML = tag + ": ";
    span.root      = text;

    var span = WebLibSimple.createAnyAppend("span", text);
    span.style.fontWeight = "lighter";
    span.innerHTML        = title;
    span.root             = text;

    div.text = text;

    return div;
}

Entry.createCircleDiv = function(size, Label, QrData, parent)
{
    var margin = GlobalConf.circleDivMargin;

    //
    // Container div
    //

    var circleDiv = WebLibSimple.createDivWidHei(0, 0, size, (size + margin) * 2, null, parent);
    // WebLibSimple.setBGColor(circleDiv, "#3ed436");

    //
    // Label div
    //

    var Labeldiv = WebLibSimple.createDivWidHei(0, 0, size, size, null, circleDiv);
    Layout.createLabelCircle(Label, size, GlobalConf.labelColor, Labeldiv, null);
    // WebLibSimple.setBGColor(div, "#af36d4");

    //
    // qr div
    //

    // Fehler beim Verarbeiten des Wertes für 'top'.  Deklaration ignoriert.
    var QrDiv = WebLibSimple.createDivWidHei(0, 0, size, size, null, circleDiv);
    QrDiv.style.top = null;
    QrDiv.style.bottom = "0px";

    Layout.createQrCircle(size, GlobalConf.qrColor, GlobalConf.qrColorBG, QrData, QrDiv);

    return circleDiv;
}

Entry.createBubble = function(flagPosition, flagWidth, flagSize, color, bubbleRadius, parent)
{
    var bubble = WebLibSimple.createDiv(0, 0, 0, 0, null, parent);

    //
    // Triangle
    //

    var pufferDiv = WebLibSimple.createDivWidth(0, 0, flagWidth, 0, null, bubble);

    Entry.createTriangle(0, flagPosition, "100%", flagSize, color, pufferDiv);

    //
    // content
    //

    var contentDiv = WebLibSimple.createDiv(flagWidth - 1, 0, 0, 0, null, bubble);
    contentDiv.style.borderRadius = bubbleRadius + "px";

    WebLibSimple.setBGColor(contentDiv, color);

    var content = WebLibSimple.createDiv(20, 20, 20, 20, null, contentDiv);

    bubble.content = content;

    return bubble;
}

Entry.createEntry = function(data, parent, virgin)
{
    console.log("nextEntryStart:" + Entry.nextEntryStart);

    Entry.parent = parent;

    //
    // vars
    //

    var circleSize   = GlobalConf.circleSize;

    var margin       = GlobalConf.margin;

    var borderL      = GlobalConf.borderLeft;
    var borderT      = GlobalConf.borderTop;
    var borderR      = GlobalConf.borderRight;
    var borderB      = GlobalConf.borderBottom;

    var bubbleRadius = GlobalConf.bubbleRadius;
    var tagSize      = GlobalConf.tagSize;

    var entrySize = Object.keys(data).length * tagSize + bubbleRadius + borderB;

    var marginDiv = WebLibSimple.createDivHeight
    (
            borderL,
            Entry.nextEntryStart + borderT,
            borderR,
            entrySize,
            null,
            parent
    );

    Entry.nextEntryStart += entrySize;

    var entry = WebLibSimple.createDiv(0, 0, 0, margin, null, marginDiv);

    // WebLibSimple.setBGColor(marginDiv, "#3688d4");
    // WebLibSimple.setBGColor(entry, "#d4cd36");

    //
    // Circle Stuff
    //

    var CircleDiv = Entry.createCircleDiv(circleSize, data.ShortName, "QrData", entry);

    //
    // Bubble
    //

    var Container    = WebLibSimple.createDiv(circleSize, 0, 0, 0, null, entry);
    var flagSize     = GlobalConf.flagSize;
    var flagPosition = circleSize / 2;
    var flagWidth    = GlobalConf.flagWidth;

    var bubble = Entry.createBubble(flagPosition, flagWidth, flagSize, GlobalConf.bubbleColor, bubbleRadius, Container);

    //
    // fill bubble content
    //

    var index = 0;
    var tagSize = GlobalConf.tagSize;

    for (var option in data)
    {
        var tag   = option;
        var title = data[ option ];

        var entryTag = Entry.createEntryTag(tag, title, tagSize, index, bubble.content);
        index++;
    }

    if (bubble.offsetHeight < CircleDiv.offsetHeight)
    {
        bubble.style.height = CircleDiv.offsetHeight + "px";
    }
}
