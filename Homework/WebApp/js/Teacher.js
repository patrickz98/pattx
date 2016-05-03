Teacher = {};

// Teacher.conf.colorTrue
Teacher.conf = {
    border: 10,
    headlineHeight: 85,
    circleSize: 200,
    today: WebLibSimple.getNiceDate((new Date())),
    colorTrue:  "#3688d4",
    colorFalse: "#6b6b6b"
};

Teacher.data = {
    uuid: "AVRpLAJgPkDt6iI38jVw",
    Country: "de",
    School: null,
    CreateDate: Teacher.conf.today,
    Subjects: null,
}

Teacher.createOptionButton = function(conf, size, color, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.display    = "inline-block";
    containerDiv.style.padding    = "20px";

    var event = null;

    if (conf.type == "List")      event = Option.buttonEventList;
    if (conf.type == "TextField") event = Option.buttonEventTextField;
    if (conf.type == "Date")      event = Option.buttonEventDate;
    if (conf.type == "Nummber")   event = Option.buttonEventNummber;
    if (conf.type == "Bool")      event = Option.buttonEventBool;

    var div = Layout.createCenterCircle(conf.name, size, color, containerDiv, event);
    div.conf = conf;
    div.parent = Teacher;

    return div;
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

    //
    // top div
    //

    Teacher.topDiv = WebLibSimple.createDiv(border, border, border, border, null, Teacher.globalContentDiv);

    //
    // Headline
    //

    Layout.createHeadline("Teachers", headlineHeight, Teacher.topDiv);

    //
    // top div
    //

    Teacher.content = WebLibSimple.createDiv(0, headlineHeight + 10, 0, 0, null, Teacher.topDiv);
    // WebLibSimple.setBGColor(Teacher.topDiv, "#666666");
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
    var color          = Teacher.conf.colorFalse;

    //
    // Center
    //

    var center = WebLibSimple.createAnyAppend("center", parent);

    Teacher.createOptionButton(Subjects, circleSize, color, center);
    Teacher.createOptionButton(Name,     circleSize, color, center);
    Teacher.createOptionButton(Notes,    circleSize, color, center);
    Teacher.createOptionButton(School,   circleSize, color, center);
}

Teacher.main(document.body);

console.log("Done...");
