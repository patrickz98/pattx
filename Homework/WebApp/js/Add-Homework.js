AddHomework = {};

AddHomework.data = {
    uuid: "AVRpLAJgPkDt6iI38jVw",
    Country: "de",
    School: "GSH",
    Grade: "S2",
    CreateDate: GlobalConf.today,
    Subject: null,
    Course: null,
    Teacher: null,
    DestinyDate: null,
    Task: null,
    Notes: null,
    EstimatedTime: null,
    Priority: null,
    Done: null
}

AddHomework.createOptionButton = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.display = "inline-block";
    containerDiv.style.padding = "20px";

    var event = null;

    if (conf.type == "List")      event = Option.buttonEventList;
    if (conf.type == "TextField") event = Option.buttonEventTextField;
    if (conf.type == "Date")      event = Option.buttonEventDate;
    if (conf.type == "Nummber")   event = Option.buttonEventNummber;
    if (conf.type == "Bool")      event = Option.buttonEventBool;


    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, event);
    div.conf = conf;
    div.parent = AddHomework;

    AddHomework.options.push(div);

    return div;
}

AddHomework.log = function(response)
{
    console.log(response);
}

AddHomework.send = function()
{
    var options = AddHomework.options;
    var color = GlobalConf.colorFalse;

    console.log(options);

    for (var opt in options)
    {
        var div = options[ opt ];
        div.innerHTML = div.conf.name;
        WebLibSimple.setBGColor(div, color);

        AddHomework.data[ div.conf.optionKey ] = null;
    }

    var json = JSON.stringify(AddHomework.data)
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

            AddHomework.log(xmlhttp.responseText);

            // return xmlhttp.responseText;
        }
    }

    json = encodeURI(json);

    xmlhttp.open("GET", "http://patrick-macbook.local/homework/uploade.php?json=" + json, false);
    xmlhttp.send();

}

AddHomework.frameSetup = function(topDiv)
{
    //
    // Vars
    //

    var border = GlobalConf.border;
    var headlineHeight = GlobalConf.headlineHeight;

    //
    // globalContentDiv
    //

    AddHomework.globalContentDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, topDiv);
    AddHomework.globalContentDiv.style.overflow = "auto";
    AddHomework.globalContentDiv.style.fontFamily = "Ubuntu, Helvetica, Arial";

    //
    // top div
    //

    AddHomework.topDiv = WebLibSimple.createDiv(border, border, border, border, null, AddHomework.globalContentDiv);

    //
    // Headline
    //

    // Layout.createHeadline("Easy Json Interface...!", headlineHeight, AddHomework.topDiv);

    //
    // top div
    //

    // AddHomework.content = WebLibSimple.createDiv(0, headlineHeight + 10, 0, 0, null, AddHomework.topDiv);
    AddHomework.content = WebLibSimple.createDiv(0, 0, 0, 0, null, AddHomework.topDiv);
    // WebLibSimple.setBGColor(AddHomework.topDiv, "#666666");
}

AddHomework.main = function(topDiv)
{
    AddHomework.frameSetup(topDiv);

    //
    // Vars
    //

    var headlineHeight = GlobalConf.headlineHeight;
    var parent         = AddHomework.content;
    var circleSize     = GlobalConf.circleSize;
    var color          = GlobalConf.colorFalse;

    //
    // Content Array
    //

    AddHomework.options = [];

    //
    // Center
    //

    var center = WebLibSimple.createAnyAppend("center", parent);

    //
    // Content with a list
    //

    AddHomework.createOptionButton(Subjects, circleSize, color, center);
    AddHomework.createOptionButton(Priority, circleSize, color, center);

    //
    // Content with a textField
    //

    AddHomework.createOptionButton(Task,   circleSize, color, center);
    AddHomework.createOptionButton(Notes,  circleSize, color, center);
    AddHomework.createOptionButton(School, circleSize, color, center);

    //
    // Content with a Date
    //

    AddHomework.createOptionButton(DestinyDate, circleSize, color, center);

    //
    // Content with Numbers
    //

    AddHomework.createOptionButton(EstimatedTime, circleSize, color, center);

    //
    // Content with boolean
    //

    AddHomework.createOptionButton(Done, circleSize, color, center);

    //
    // Commit
    //

    var containerDiv = WebLibSimple.createAnyAppend("div", center);
    containerDiv.style.padding = "20px";
    containerDiv.style.display = "inline-block";

    Layout.createCenterCircle("+", circleSize, color, containerDiv, AddHomework.send);
}

AddHomework.main(document.body);

console.log("Done...");
