AddHomework = {};

// AddHomework.conf.circleSize
AddHomework.conf = {
    border: 10,
    headlineHeight: 85,
    circleSize: 200,
    today: WebLibSimple.getNiceDate((new Date())),
};

AddHomework.data = {
    uuid: "AVRpLAJgPkDt6iI38jVw",
    Country: "de",
    School: "GSH",
    Grade: "S2",
    CreateDate: AddHomework.conf.today,
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

AddHomework.createHeadline = function(title, parent)
{
    var containerDiv = WebLibSimple.createDivHeight(0, 0, 0, AddHomework.conf.headlineHeight, null, parent);
    containerDiv.style.borderRadius = "20px";

    var headline = WebLibSimple.createAnyAppend("h1", containerDiv);
    headline.innerHTML       = title;
    headline.style.textAlign = "center";
    headline.style.color     = "#ffffff";

    WebLibSimple.setBGColor(containerDiv, "#566b90");
}

AddHomework.createOptionButtonList = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventList);
    div.conf = conf;

    AddHomework.options.push(div);

    return div;
}

AddHomework.createOptionButtonTextField = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventTextField);
    div.conf = conf;

    AddHomework.options.push(div);

    return div;
}

AddHomework.createOptionButtonDate = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventDate);
    div.conf = conf;

    AddHomework.options.push(div);

    return div;
}

AddHomework.createOptionButtonNummber = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventNummber);
    div.conf = conf;

    AddHomework.options.push(div);

    return div;
}

AddHomework.createOptionButtonBool = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventBool);
    div.conf = conf;

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

    console.log(options);

    for (var opt in options)
    {
        var div = options[ opt ];
        div.innerHTML = div.conf.name;
        WebLibSimple.setBGColor(div, "#3688d4");

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

    var border = AddHomework.conf.border;
    var headlineHeight = AddHomework.conf.headlineHeight;

    //
    // globalContentDiv
    //

    AddHomework.globalContentDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, topDiv);
    AddHomework.globalContentDiv.style.overflow = "auto";

    //
    // top div
    //

    AddHomework.topDiv = WebLibSimple.createDiv(border, border, border, border, null, AddHomework.globalContentDiv);

    //
    // Headline
    //

    Layout.createHeadline("Easy Json Interface...!", headlineHeight, AddHomework.topDiv);

    //
    // top div
    //

    AddHomework.content = WebLibSimple.createDiv(0, headlineHeight + 10, 0, 0, null, AddHomework.topDiv);
    // WebLibSimple.setBGColor(AddHomework.topDiv, "#666666");
}

AddHomework.main = function(topDiv)
{
    AddHomework.frameSetup(topDiv);

    //
    // Vars
    //

    var headlineHeight = AddHomework.conf.headlineHeight;

    var parent = AddHomework.content;
    var circleSize = AddHomework.conf.circleSize;

    //
    // Content Array
    //

    AddHomework.options = [];

    //
    // Content with a list
    //

    AddHomework.createOptionButtonList(Subjects, circleSize, "#3688d4", parent);
    AddHomework.createOptionButtonList(Priority, circleSize, "#3688d4", parent);

    //
    // Content with a textField
    //

    AddHomework.createOptionButtonTextField(Task,  circleSize, "#3688d4", parent);
    AddHomework.createOptionButtonTextField(Notes, circleSize, "#3688d4", parent);

    //
    // Content with a Date
    //

    AddHomework.createOptionButtonDate(DestinyDate, circleSize, "#3688d4", parent);

    //
    // Content with Numbers
    //

    AddHomework.createOptionButtonNummber(EstimatedTime, circleSize, "#3688d4", parent);

    //
    // Content with boolean
    //

    AddHomework.createOptionButtonBool(Done, circleSize, "#3688d4", parent);

    //
    // Commit
    //

    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";
    Layout.createCenterCircle("+", circleSize, "#3688d4", containerDiv, AddHomework.send);
}

AddHomework.main(document.body);

console.log("Done...");
