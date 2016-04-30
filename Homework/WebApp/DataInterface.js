DataInterface = {};

// DataInterface.conf.circleSize
DataInterface.conf = {
    border: 10,
    headlineHeight: 85,
    circleSize: 200,
    today: WebLibSimple.getNiceDate((new Date())),
};

DataInterface.opt = {
    // uuid:
    Country: "de",
    School: "GSH",
    Grade: "S2",
    // CreateDate: (new Date()).toString(),
    CreateDate: DataInterface.conf.today,
    // Subject: null,
    Subject: "Pups",
    Course: null,
    Teacher: null,
    DestinyDate: null,
    Room: null,
    Task: null,
    Notes: null,
    EstimatedTime: null,
    Priority: null
    // "teacher": {
    //     "sex": "M/W",
    //     "name": "Boom",
    //     "symbol": "BO"
    // },
}

DataInterface.createHeadline = function(title, parent)
{
    var containerDiv = WebLibSimple.createDivHeight(0, 0, 0, DataInterface.conf.headlineHeight, null, parent);
    containerDiv.style.borderRadius = "20px";

    var headline = WebLibSimple.createAnyAppend("h1", containerDiv);
    headline.innerHTML       = title;
    headline.style.textAlign = "center";
    headline.style.color     = "#ffffff";

    WebLibSimple.setBGColor(containerDiv, "#566b90");
}

DataInterface.frameSetup = function()
{
    //
    // Vars
    //

    var border = DataInterface.conf.border;
    var headlineHeight = DataInterface.conf.headlineHeight;

    //
    // globalContentDiv
    //

    DataInterface.globalContentDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, document.body);
    DataInterface.globalContentDiv.style.overflow = "auto";

    //
    // top div
    //

    DataInterface.topDiv = WebLibSimple.createDiv(border, border, border, border, null, DataInterface.globalContentDiv);

    //
    // top div
    //

    DataInterface.content = WebLibSimple.createDiv(0, headlineHeight + 10, 0, 0, null, DataInterface.topDiv);
    // WebLibSimple.setBGColor(DataInterface.content, "#666666");

    //
    // Headline
    //

    DataInterface.createHeadline("Easy Json Interface...!", DataInterface.topDiv);
}

// DataInterface.createCircle = function(title, top, left, size, color, parent, eventFunct)
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

DataInterface.createCenterCircle = function(title, size, color, parent, eventFunct)
{
    var center = WebLibSimple.createAnyAppend("center", parent);
    // var span   = WebLibSimple.createAnyAppend("span", center);
    // span.innerHTML = "Wollo";

    var div = WebLibSimple.createAnyAppend("div", center);
    div.style.borderRadius = "50%";
    div.style.width        = size + "px";
    div.style.height       = size + "px";
    div.style.lineHeight   = size + "px";
    div.style.fontSize     = (size * 0.15) + "px";
    div.style.textAlign    = "center";
    div.style.color        = "#ffffff";

    div.onclick   = eventFunct;
    div.innerHTML = title;

    WebLibSimple.setBGColor(div, color);

    return div;
}

DataInterface.createOptionButtonList = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = DataInterface.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventList);
    div.conf = conf;

    return div;
}

DataInterface.createOptionButtonTextField = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = DataInterface.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventTextField);
    div.conf = conf;

    return div;
}

DataInterface.createOptionButtonDate = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";

    var div = DataInterface.createCenterCircle(conf.name, size, color, containerDiv, Option.buttonEventDate);
    div.conf = conf;

    return div;
}

DataInterface.log = function(response)
{
    console.log(response);
}

DataInterface.send = function()
{
    var json = JSON.stringify(DataInterface.opt)
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

            DataInterface.log(xmlhttp.responseText);

            // return xmlhttp.responseText;
        }
    }

    json = encodeURI(json);

    xmlhttp.open("GET", "http://patrick-macbook.local/homework/uploade.php?json=" + json, false);
    xmlhttp.send();

}

DataInterface.main = function()
{
    var headlineHeight = DataInterface.conf.headlineHeight;

    var parent = DataInterface.content;
    var circleSize = DataInterface.conf.circleSize;

    // DataInterface.createCircle("Subject", "10%", "10%", 200, "#425db8", parent, DataInterface.event);

    // DataInterface.createCircle("Subject", "40%", 0, 200, "#335bc3", parent, DataInterface.subjectButton);
    // DataInterface.Subject = DataInterface.createCenterCircle("Subject", 200, "#335bc3", parent, Option.buttonEvent);

    //
    // Content with a list
    //

    DataInterface.createOptionButtonList(Subjects, circleSize, "#335bc3", parent);
    DataInterface.createOptionButtonList(Priority, circleSize, "#335bc3", parent);

    //
    // Content with a textField
    //

    DataInterface.createOptionButtonTextField(Task,  circleSize, "#335bc3", parent);
    DataInterface.createOptionButtonTextField(Room,  circleSize, "#335bc3", parent);
    DataInterface.createOptionButtonTextField(Notes, circleSize, "#335bc3", parent);

    //
    // Content with a Date
    //

    DataInterface.createOptionButtonDate(DestinyDate, circleSize, "#335bc3", parent);

    //
    // Commit
    //

    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "20px";
    DataInterface.createCenterCircle("+", circleSize, "#335bc3", containerDiv, DataInterface.send);

    // for (var opt in DataInterface.opt)
    // {
    //     DataInterface.createCircle(DataInterface.opt[ opt ], "40%", opt * 220 + 220, 200, "#425db8", parent, DataInterface.event);
    // }

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
}

DataInterface.frameSetup();
DataInterface.main();

console.log("Done...");
