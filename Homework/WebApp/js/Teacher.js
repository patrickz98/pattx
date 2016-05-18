Teacher = {};

Teacher.data = {
    uuid: GlobalConf.uuid,
    Country: "de",
    School: null,
    CreateDate: GlobalConf.today,
    Subjects: null,
    Name: null
}

Teacher.log = function(response)
{
    console.log(response);
}

Teacher.send = function()
{
    var options = Teacher.options;
    // var color = GlobalConf.colorFalse;

    console.log(options);

    for (var opt in options)
    {
        var div = options[ opt ];
        div.innerHTML = div.conf.name;
        // WebLibSimple.setBGColor(div, color);

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

Teacher.frameSetup = function(parent)
{
    //
    // top div
    //

    var scrollDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, parent);
    // scrollDiv.style.overflow = "auto";
    scrollDiv.style.overflow = "hidden";

    Teacher.topDiv = WebLibSimple.createDiv(20, 20, 20, 20, null, Teacher.scrollDiv);

    var topDiv = Teacher.topDiv;
    topDiv.style.overflow = "auto";
    topDiv.style.fontFamily = "Ubuntu, Helvetica, Arial";
    topDiv.scrollDiv = scrollDiv;

    WebLibSimple.setBGColor(Teacher.topDiv, "#666666");

    // Teacher.topDiv.style.overflow = null;

    //
    // Headline
    //

    // Layout.createHeadline("Teachers", headlineHeight, Teacher.topDiv);

    //
    // top div
    //

    // WebLibSimple.setBGColor(Teacher.topDiv, "#666666");
}

Teacher.main = function(topDiv)
{
    WebLibSimple.disableSelection(topDiv);
    WebLibSimple.setBGColor(topDiv, GlobalConf.bodyColor);

    //
    // Vars
    //
    // var parent = topDiv;
    var parent = WebLibSimple.createDiv(0, 0, 0, 0, null, topDiv);
    // parent.style.height = "100%";

    parent.style.overflow = "auto";
    parent.style.fontFamily = GlobalConf.fontFamily;

    console.log(parent.scrollTop);
    console.log(parent.scrollHeight);

    var headlineHeight = GlobalConf.headlineHeight;
    var circleSize     = GlobalConf.circleSize;
    var margin         = 40;

    //
    // Center
    //
    // Entry.createEntry(Data.entrys[ 0 ], parent);

    for (var index in Data.entrys)
    {
        Entry.createEntry(Data.entrys[ index ], parent);
    }

    // var marginSize  = circleSize + (margin * 2);
    // var addEntry    = WebLibSimple.createDivHeight(0, Entry.getNextEntryStart(), 0, marginSize, null, parent);
    // var center      = WebLibSimple.createAnyAppend("center", addEntry);
    // var backButton  = Layout.createLabelCircle("+", circleSize, GlobalConf.colorFalse, center, Entry.addEntry);
    // backButton.root = addEntry;
    // backButton.topDiv = parent;
}

Teacher.main(document.body);
