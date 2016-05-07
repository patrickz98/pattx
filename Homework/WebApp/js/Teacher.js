Teacher = {};

// Teacher.conf.colorTrue
Teacher.conf = {
    uuid: "AVRpLAJgPkDt6iI38jVw",
    border: 15,
    headlineHeight: 85,
    circleSize: 200,
    today: WebLibSimple.getNiceDate((new Date())),
    colorTrue:  "#2e54e3",
    colorFalse: "#7e7e7e"
};

Teacher.data = {
    uuid: Teacher.conf.uuid,
    Country: "de",
    School: null,
    CreateDate: Teacher.conf.today,
    Subjects: null,
    Name: null,
}

Teacher.log = function(response)
{
    console.log(response);
}

Teacher.send = function()
{
    var options = Teacher.options;
    var color = Teacher.conf.colorFalse;

    console.log(options);

    for (var opt in options)
    {
        var div = options[ opt ];
        div.innerHTML = div.conf.name;
        WebLibSimple.setBGColor(div, color);

        Teacher.data[ div.conf.optionKey ] = null;
    }

    var json = JSON.stringify(Teacher.data)
    console.log(json);

    var xmlhttp = null;

    if (window.XMLHttpRequest)
    {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else
    {
        // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function()
    {
        if ((xmlhttp.readyState == 4) && (xmlhttp.status == 200))
        {
            // console.log(xmlhttp.responseText);

            Teacher.log(xmlhttp.responseText);

            // return xmlhttp.responseText;
        }
    }

    json = encodeURI(json);

    xmlhttp.open("GET", "http://patrick-macbook.local/homework/uploade.php?json=" + json, false);
    xmlhttp.send();

}

Teacher.frameSetup = function(topDiv)
{
    //
    // Vars
    //

    var border = Teacher.conf.border;
    var headlineHeight = Teacher.conf.headlineHeight;

    //
    // globalContentDiv
    //

    Teacher.globalContentDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, topDiv);
    Teacher.globalContentDiv.style.overflow = "auto";

    Teacher.globalContentDiv.style.fontFamily = "Ubuntu, Helvetica, Arial";

    //
    // top div
    //

    Teacher.topDiv = WebLibSimple.createDiv(border, border, border, border, null, Teacher.globalContentDiv);

    //
    // Headline
    //

    // Layout.createHeadline("Teachers", headlineHeight, Teacher.topDiv);

    //
    // top div
    //

    // Teacher.content = WebLibSimple.createDiv(0, headlineHeight + 10, 0, 0, null, Teacher.topDiv);
    Teacher.content = WebLibSimple.createDiv(0, 0, 0, 0, null, Teacher.topDiv);
    // WebLibSimple.setBGColor(Teacher.topDiv, "#666666");
}

Teacher.createEntryTag = function(tag, title, parent, x, y, holeLine)
{
    var left   = (x * 50) + "%";
    var top    = (y * 33) + "%";
    var height = "33%";
    var width  = "50%";

    if (holeLine == true)
    {
        var left   = "0%";
        var width  = "100%";
    }

    var div = WebLibSimple.createDivWidHei(left, top, width, height, null, parent);

    var border = 5;
    // var padding = WebLibSimple.createDiv(border, border, border, border, null, div);
    var padding = WebLibSimple.createDiv(border, border, border, border, null, div);

    var text = WebLibSimple.createDiv(0, 0, 0, 0, null, padding);
    text.onclick            = Teacher.editEntry;
    text.style.cursor       = "pointer";
    text.style.textAlign    = "center";
    text.style.borderRadius = "30px";
    text.style.lineHeight   = padding.offsetHeight + "px";
    text.style.fontSize     = "25px";
    text.style.overflow     = "hidden";
    text.style.color        = "#ffffff";
    text.tag                = tag;
    text.title              = title;
    // text.root               = text;

    // text.style.border       = "1px solid #000000";


    var span = WebLibSimple.createAnyAppend("span", text);
    span.innerHTML = tag + ": ";
    span.root      = text;

    var span = WebLibSimple.createAnyAppend("span", text);
    span.innerHTML        = title;
    span.style.fontWeight = "lighter";
    span.root             = text;

    text.titleSpan      = span;

    WebLibSimple.setBGColor(text, Teacher.conf.colorFalse);

    return padding;
}

Teacher.exitInput = function(event)
{
    Option.nukeDimmerDiv();

    var target = event.target.target;
    var value  = Teacher.input.value;
    console.log(value);

    if (value)
    {
        // WebLibSimple.setBGColor(target, "#3688d4");
        target.titleSpan.innerHTML = value;
        // Option.parent.data[ target.conf.optionKey ] = value;
    }
    else
    {
        WebLibSimple.setBGColor(target, Teacher.conf.colorFalse);
    }
}

Teacher.openDialog = function(target)
{
    var dimmer = Option.createDimmerDiv();

    var value = target.titleSpan.innerHTML;

    var center = WebLibSimple.createAnyAppend("center", dimmer);

    Teacher.input = WebLibSimple.createAnyAppend("input", center);

    var input = Teacher.input;
    input.style.width  = "300px";
    input.style.height = "30px";
    input.type         = "text";
    input.value        = value;
    input.style.textAlign  = "center";
    input.style.borderRadius = "30px";
    // WebLibSimple.setBGColor(input, "#9f9f9f");

    var div = WebLibSimple.createAnyAppend("div", dimmer);
    div.style.paddingTop = "50px";

    var center = WebLibSimple.createAnyAppend("center", div);

    var backButton = Layout.createLabelCircle("Ok", 80, "#000000", center, Teacher.exitInput);
    backButton.target = target;
}

Teacher.editEntry = function(event)
{
    var target = event.target;

    if (target.root)
    {
        target = target.root;
    }

    Teacher.openDialog(target);
}

Teacher.createEntry = function(teacherData, index, size, parent)
{
    var data       = teacherData.entrys[ index ];
    var position   = teacherData.position;
    var circleSize = Teacher.conf.circleSize;
    var color      = Teacher.conf.colorTrue;
    var margin     = 40;
    var marginSize = circleSize + (margin * 2);
    var marginDiv  = WebLibSimple.createDivHeight(0, marginSize * index, 0, marginSize, null, parent);
    var entry      = WebLibSimple.createDiv(20, margin, 20, margin, null, marginDiv);
    var NameCircle = Layout.createLabelCircle(data.ShortName, circleSize, color, entry, null);
    var border     = circleSize + 10;
    var content    = WebLibSimple.createDiv(border, 0, border, 0, null, entry);

    for (var option in data)
    {
        if (option == "uuid") continue;

        var x = position[ option ].x;
        var y = position[ option ].y;

        var holeLine = position[ option ].holeLine;

        var tag   = option;
        var title = data[ option ];

        var entryTag = Teacher.createEntryTag(tag, title, content, x, y, holeLine);
    }

    var div = WebLibSimple.createDiv(null, 0, 0, 0, null, entry);
    Layout.createQrCircle(circleSize, "#ffffff", Teacher.conf.colorFalse, data.uuid, div);
}

Teacher.main = function(topDiv)
{
    Teacher.frameSetup(topDiv);

    //
    // Vars
    //

    var headlineHeight = Teacher.conf.headlineHeight;
    var parent         = Teacher.content;
    var circleSize     = Teacher.conf.circleSize;
    var color          = Teacher.conf.colorTrue;
    var margin         = 40;

    //
    // Center
    //

    for (var index in Data.entrys)
    {
        Teacher.createEntry(Data, index, circleSize, parent);
    }

    var marginSize = circleSize + (margin * 2);
    var addEntry   = WebLibSimple.createDivHeight(0, marginSize * Data.entrys.length, 0, marginSize, null, parent);
    var center     = WebLibSimple.createAnyAppend("center", addEntry);
    var backButton = Layout.createLabelCircle("+", circleSize, Teacher.conf.colorFalse, center, null);
}

Teacher.main(document.body);
