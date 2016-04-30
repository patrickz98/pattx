DataInterface = {};

// DataInterface.conf.border
DataInterface.conf = {
    border: 10,
    headlineHeight: 85
};

DataInterface.opt = {
    // uuid:
    Country: "de",
    School: "GSH",
    Grade: "S2",
    CreateDate: (new Date()).getTime(),
    Subject: null,
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


// <textarea name="message" rows="10" cols="30">
// The cat was playing in the garden.
// </textarea>

DataInterface.nukeDimmerDiv = function()
{
    DataInterface.dimmerDiv.style.display = "none";

    if (DataInterface.opt.Subject)
    {
        WebLibSimple.setBGColor(DataInterface.Subject, "#ff9100");
        DataInterface.Subject.innerHTML = DataInterface.opt.Subject;
    }
    else
    {
        WebLibSimple.setBGColor(DataInterface.Subject, "#335bc3");
    }
}

DataInterface.createDimmerDiv = function()
{
    DataInterface.dimmerDiv = WebLibSimple.createDiv(0, 0, 0, 0, "dimemrDiv", document.body);

    var dimmerDiv = DataInterface.dimmerDiv;
    // dimmerDiv.onclick        = DataInterface.nukeDimmerDiv;

    WebLibSimple.setBGColor(dimmerDiv, "#99000000");

    var containerDiv = WebLibSimple.createDiv(50, 50, 50, 50, null, dimmerDiv);
    containerDiv.style.border       = "1px solid black";
    containerDiv.style.borderRadius = "25px";
    // containerDiv.onclick            = DataInterface.event;
    containerDiv.style.overflow = "hidden";

    WebLibSimple.setBGColor(containerDiv, "#ffffff");

    var contentDiv = WebLibSimple.createDiv(25, 25, 25, 25, null, containerDiv);

    return contentDiv;
}

DataInterface.createCircle = function(title, top, left, size, color, parent, eventFunct)
{
    var div = WebLibSimple.createDivWidHei(top, left, size, size, null, parent);
    div.style.borderRadius = "50%";
    div.style.lineHeight   = size + "px";
    div.style.fontSize     = (size * 0.15) + "px";
    div.style.textAlign    = "center";
    div.style.color        = "#ffffff";

    div.onclick   = eventFunct;
    div.innerHTML = title;

    WebLibSimple.setBGColor(div, color);

    return div;
}

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

// DataInterface.event = function(event)
// {
//     var target = event.target;
//     console.log("DataInterface.event: " + target.innerHTML);
// }

DataInterface.subjectSelected = function(event)
{
    var target = event.target;
    target.style.color = "#ff9100";

    var choice = target.innerHTML;

    console.log("Subject Selected: " + choice);
    DataInterface.opt.Subject = choice;
}

DataInterface.subjectButton = function(event)
{
    console.log("DataInterface.subjectButton");

    var target = event.target;
    var dimmerDiv = DataInterface.createDimmerDiv();

    for (var subject in Subjects)
    {
        var div = WebLibSimple.createAnyAppend("div", dimmerDiv);
        div.innerHTML = subject;
        div.style.textAlign = "center";
        div.onclick = DataInterface.subjectSelected;
    }

    var div = WebLibSimple.createAnyAppend("div", dimmerDiv);
    div.style.paddingTop = "50px";

    var backButton = DataInterface.createCenterCircle("----", 50, "#000000", div, DataInterface.nukeDimmerDiv);

    // var backButton = DataInterface.createCircle("-----", "50%", null, 50, "#000000", div, DataInterface.nukeDimmerDiv);
    // backButton.style.zIndex = "50";
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

DataInterface.createList = function(parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.height = "30px";

    WebLibSimple.setBGColor(containerDiv, "#6c3333");

    var select = WebLibSimple.createAnyAppend("select", containerDiv);
    select.style.top    = "0px";
    select.style.bottom = "0px";

    // select.name = "cars";

    for (var subject in Subjects)
    {
        var option = WebLibSimple.createOption(select, subject);
    }

    // select.add("<option value=\"car\">BMW</option>");

    console.log(select.selectedIndex);
    console.log(select.options);
    console.log(select.options[ select.selectedIndex ]);
    console.log(select.value);

    // <form action="action_page.php">
    //   <select name="cars">
    //     <option value="volvo">Volvo</option>
    //     <option value="saab">Saab</option>
    //     <option value="fiat">Fiat</option>
    //     <option value="audi">Audi</option>
    //   </select>
    //   <br><br>
    //   <input type="submit">
    // </form>
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

DataInterface.main = function()
{
    var headlineHeight = DataInterface.conf.headlineHeight;

    var parent = DataInterface.content;


    // DataInterface.createCircle("Subject", "10%", "10%", 200, "#425db8", parent, DataInterface.event);

    // DataInterface.createCircle("Subject", "40%", 0, 200, "#335bc3", parent, DataInterface.subjectButton);
    DataInterface.Subject = DataInterface.createCenterCircle("Subject", 200, "#335bc3", parent, DataInterface.subjectButton);

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

    // var input = WebLibSimple.createAnyAppend("input", containerDiv);
    // input.style.left   = "0px";
    // input.style.top    = "0px";
    // input.style.right  = "0px";
    // input.style.bottom = "0px";
    //
    // // input.style.height = "30px";
    //
    // input.type = "text";
    // input.value = "Hello World!";

    // DataInterface.createList(content);
}

DataInterface.frameSetup();
DataInterface.main();

console.log("Done...");
