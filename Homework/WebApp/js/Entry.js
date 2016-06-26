Entry = {};

Entry.mouseHandler = function(elem)
{
    elem.addEventListener("mouseover", mouseOver);
    elem.addEventListener("mouseout", mouseOut);

    function mouseOver()
    {
        // console.log(elem.innerHTML);

        var root = elem;
        if (elem.root) root = elem.root;

        var color = GlobalConf.optionCircleMouse;

        // root.Label.style.textDecoration = "underline";
        // root.Label.style.color = color;
        // root.Label.style.textDecorationColor = color;

        root.Label.style.border = "1px solid " + color;

        if (root.tagLabel)
        {
            root.tagLabel.style.color = "#ffffff";
        }

        if (root.circle)
        {
            root.circle.style.border = GlobalConf.optionCircleBorderMouse;
        }
        // root.Label.style.color  = color;
        // root.circle.style.color = color;
    }

    function mouseOut()
    {
        // console.log(elem.innerHTML);

        var root = elem;
        if (elem.root) root = elem.root;

        var color = GlobalConf.optionCircleColor;

        root.Label.style.textDecoration = null;

        if (root.tagLabel)
        {
            var tagColor = GlobalConf.tagColor;

            root.tagLabel.style.color = tagColor;
        }

        if (root.circle)
        {
            root.circle.style.border = GlobalConf.optionCircleBorder;
        }

        // root.Label.style.color  = color;
        // root.circle.style.color = color;
    }
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

Entry.editEntry = function(event)
{
    var target = event.target;

    // if (target.control === undefined)
    // {
    //     console.log("++> Entry.editEntry stopped by control");
    //     return;
    // }

    if (target.root)
    {
        target = target.root;
    }

    var json = target.jsonBranch;

    Edit.createEdit(target, json, Entry.parent);
}

Entry.nextEntryStart = 0;

Entry.addEntry = function(event)
{
	var target = event.target;
	var root   = target.root;
	var parent = target.topDiv;

    var tmp = {
        "id": null,
        "uuid": GlobalConf.uuid,
        "Name": "",
        "ShortName": "",
        "Subjects": "",
        "Notes": "",
        "School": ""
    };

    Data.entrys.push(tmp);

    Entry.createEntry(Data.entrys[ Data.entrys.length - 1 ], parent, true);
    target.root.style.top = Entry.nextEntryStart + "px";
}

Entry.createEntryTag = function(tag, title, tagSize, index, parent)
{
    var paddingLeft = GlobalConf.tagMarginLeft

    var div = WebLibSimple.createDivHeight(paddingLeft, tagSize * index, 0, tagSize, null, parent);
    // WebLibSimple.setBGColor(div, "#4877a8");

    var text = WebLibSimple.createDiv(0, 0, 0, 0, null, div);
    text.style.lineHeight   = div.offsetHeight + "px";
    text.style.fontSize     = GlobalConf.fontSize + "px";
    // border to big
    // text.style.overflow     = "hidden";
    text.style.color        = "#ffffff";
    text.style.cursor       = "pointer";

    text.tag                = tag;
    text.title              = title;
    text.jsonBranch         = Entry.parent.jsonBranch;
    text.onclick            = Entry.editEntry;
    text.control            = "control";

    var tagColor = GlobalConf.tagColor;

    var div = WebLibSimple.createDiv(0, 0, "50%", 0, null, text);
    div.style.fontWeight = "lighter";
    div.style.color      = tagColor;
    div.innerHTML        = tag + ": ";
    div.root             = text;

    text.tagLabel = div;

    var div = WebLibSimple.createDiv("50%", 0, 0, 0, null, text);
    div.style.fontWeight = "bold";
    div.innerHTML        = title;
    div.root             = text;
    div.style.overflow   = "hidden";

    text.Label = div;

    Entry.mouseHandler(text);

    // var span = WebLibSimple.createAnyAppend("span", text);
    // span.innerHTML = tag + ": ";
    // span.root      = text;
    //
    // var span = WebLibSimple.createAnyAppend("span", text);
    // span.style.fontWeight = "lighter";
    // span.innerHTML        = title;
    // span.root             = text;

    text.titleSpan = div;
    div.text       = text;

    return div;
}

Entry.createOptionLabel = function(title, size, parent)
{
    var textColor = GlobalConf.optionCircleColor;
    var margin = GlobalConf.optionCircleMargin;

    var div = WebLibSimple.createDiv(size + margin, 0, 0, 0, null, parent);
    div.innerHTML        = title;
    div.style.fontSize   = size * 0.8 + "px";
    div.style.lineHeight = size + "px";
    div.style.color      = textColor;
    div.style.overflow   = "hidden";
    div.style.fontWeight = "lighter";

    return div;
}

Entry.openScan = function(event)
{
    var target = event.target;

    if (target.root) target = target.root;

    console.log("--> Open Qr id: " + target.id);
}

Entry.deleteEntry = function(event)
{
    var target = event.target;

    if (target.root) target = target.root;

    console.log("--> Delete Entry id: " + target.id);

    Elastic.delteById("teacher", target.id);
}

Entry.createOptionDivStd = function(size, id, parent)
{
    var margin = 30;
    var circleSize = GlobalConf.optionCircleSize;
    var optionHeight = circleSize + margin * 2;

    var color  = GlobalConf.optionCircleColor;
    var border = GlobalConf.optionCircleBorder;

    //
    // topDiv
    //

    var topDiv = WebLibSimple.createDivHeight(0, margin, 0, circleSize, null, parent);
    topDiv.onclick      = Entry.openScan;
    topDiv.style.cursor = "pointer";
    topDiv.id           = id;
    Entry.mouseHandler(topDiv);

    var containerDiscription = Entry.createOptionLabel("Scan", circleSize, topDiv);
    containerDiscription.root = topDiv;

    var containerLabel  = WebLibSimple.createDiv(0, 0, circleSize, 0, null, topDiv);
    containerLabel.root = topDiv;

    var cLabel = Layout.createBorderCircle("S", circleSize, color, border, containerLabel, null);
    cLabel.style.fontSize = circleSize * 0.8 + "px"
    cLabel.root = topDiv;

    topDiv.Label  = containerDiscription;
    topDiv.circle = cLabel;

    // WebLibSimple.setBGColor(topDiv, "#3ed436");

    //
    // bottomDiv
    //

    var bottomDiv = WebLibSimple.createDivHeight(0, optionHeight, 0, circleSize, null, parent);
    bottomDiv.onclick      = Entry.deleteEntry;
    bottomDiv.style.cursor = "pointer";
    bottomDiv.id           = id;
    Entry.mouseHandler(bottomDiv);

    var containerLabel = WebLibSimple.createDiv(0, 0, circleSize, 0, null, bottomDiv);
    containerLabel.root = bottomDiv;

    var cLabel = Layout.createBorderCircle("X", circleSize, color, border, containerLabel, null);
    cLabel.style.fontSize = circleSize * 0.8 + "px";
    cLabel.root = bottomDiv;

    var containerDiscription = Entry.createOptionLabel("Delete", circleSize, bottomDiv);
    containerDiscription.root = bottomDiv;

    bottomDiv.Label  = containerDiscription;
    bottomDiv.circle = cLabel;

    // WebLibSimple.setBGColor(bottomDiv, "#d43636");

    // Layout.createQrCircle(circleSize, GlobalConf.qrColor, GlobalConf.qrColorBG, "QrData", container);
}

Entry.createCircleDiv = function(size, Label, id, parent)
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

    var labelDiv = WebLibSimple.createDivWidHei(0, 0, size, size, null, circleDiv);
    // var lable = Layout.createLabelCircle(Label, size, GlobalConf.labelColor, labelDiv, null);
    var lable = Layout.createLabelCircle(Label, size, GlobalConf.labelColor, labelDiv, null);
    lable.style.fontSize = "25px";
    lable.style.border = "1px solid #1ED760";
    lable.style.fontWeight = "bold";

    // WebLibSimple.setBGColor(div, "#af36d4");

    //
    // Option div
    //

    var optionDiv = WebLibSimple.createDivWidHei(0, 0, size, size, null, circleDiv);
    optionDiv.style.top = null;
    optionDiv.style.bottom = "0px";

    // WebLibSimple.setBGColor(optionDiv, "#af36d4");

    Entry.createOptionDivStd(size, id, optionDiv);

    //
    // qr div
    //

    // var QrDiv = WebLibSimple.createDivWidHei(0, 0, size, size, null, circleDiv);
    // QrDiv.style.top = null;
    // QrDiv.style.bottom = "0px";
    //
    // if (QrData != null)
    // {
    //     Layout.createQrCircle(size, GlobalConf.qrColor, GlobalConf.qrColorBG, QrData, QrDiv);
    // }
    //
    return circleDiv;
}

Entry.createBubble = function(flagPosition, flagWidth, flagSize, color, bubbleRadius, parent)
{
    var bubble = WebLibSimple.createDiv(2, 0, 0, 0, null, parent);

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

    var border  = bubbleRadius / 2;
    var content = WebLibSimple.createDiv(border, border, border, border, null, contentDiv);
    content.style.overflow = "hidden";
    // WebLibSimple.setBGColor(content, "#e85620");

    bubble.content = content;

    return bubble;
}

Entry.createAddButton = function(parent)
{
    var circleSize  = GlobalConf.circleSize;
    var margin      = GlobalConf.margin;

    var marginSize  = circleSize + (margin * 2);
    var addEntry    = WebLibSimple.createDivHeight(0, Entry.nextEntryStart, 0, marginSize, null, parent);

    var center      = WebLibSimple.createAnyAppend("center", addEntry);
    var button      = Layout.createLabelCircle("+", circleSize, GlobalConf.addButtonColor, center, Entry.addEntry);
    button.root   = addEntry;
    button.topDiv = parent;
}

Entry.createEntry = function(data, parent, virgin)
{
    console.log("New Entry: " + JSON.stringify(data));

    Entry.parent = parent;
    Entry.parent.jsonBranch = data;

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

    // remove id & uuid --> - 2
    var tagCount = Object.keys(data).length - 2;
    var entrySize = tagCount * tagSize + bubbleRadius + margin;

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

    if (virgin)
    {
        var CircleDiv = Entry.createCircleDiv(circleSize, "New", null, entry);
    }
    else
    {
        var CircleDiv = Entry.createCircleDiv(circleSize, data.Name, data.id, entry);
    }

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

        if (tag == "uuid" || tag == "id") continue;

        var entryTag = Entry.createEntryTag(tag, title, tagSize, index, bubble.content);

        index++;
    }

    if (bubble.offsetHeight < CircleDiv.offsetHeight)
    {
        bubble.style.height = CircleDiv.offsetHeight + "px";
    }
}
