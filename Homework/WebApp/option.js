Option = {};

//
// Setup
//

Option.nukeDimmerDiv = function()
{
    DataInterface.dimmerDiv.style.display = "none";
}

Option.createDimmerDiv = function()
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

//
// Option List
//

Option.exitList = function()
{
    Option.nukeDimmerDiv();

    if (Option.target.choice)
    {
        WebLibSimple.setBGColor(Option.globalTarget, "#ff9100");
        Option.globalTarget.innerHTML = Option.target.choice;
    }
    else
    {
        WebLibSimple.setBGColor(Option.globalTarget, "#335bc3");
    }
}

Option.selected = function(event)
{
    var target = event.target;

    var children = Option.content.childNodes;

    for (var inx = 0; inx < children.length; inx++)
    {
        children[ inx ].style.color = "#000000";
    }

    target.style.color = "#ff9100";

    var choice = target.innerHTML;

    console.log("Subject Selected: " + choice);

    var optionKey = Option.globalTarget.conf.optionKey;

    DataInterface.opt[ optionKey ] = choice;

    target.choice = choice;

    Option.target = target;
}

Option.buttonEventList = function(event)
{
    Option.globalTarget = event.target;

    var target = Option.globalTarget;
    var conf   = target.conf;
    var opts   = target.conf.options;

    console.log("Option: " + target.innerHTML);
    console.log("opts:   " + opts);

    Option.content = Option.createDimmerDiv();
    var content = Option.content;

    for (var index in opts)
    {
        var div = WebLibSimple.createAnyAppend("div", content);
        div.innerHTML = opts[ index ];
        div.style.textAlign = "center";
        div.onclick = Option.selected;
    }

    var div = WebLibSimple.createAnyAppend("div", content);
    div.style.paddingTop = "50px";

    var backButton = DataInterface.createCenterCircle("----", 50, "#000000", div, Option.exitList);
}

//
// textField
//

Option.exitTextField = function()
{
    Option.nukeDimmerDiv();

    console.log(Option.input.value);

    var value = Option.input.value;

    if (value)
    {
        var target = Option.globalTarget;
        WebLibSimple.setBGColor(target, "#ff9100");

        DataInterface.opt[ target.conf.optionKey ] = value;
    }
    else
    {
        WebLibSimple.setBGColor(Option.globalTarget, "#335bc3");
    }
}

Option.buttonEventTextField = function(event)
{
    Option.globalTarget = event.target;

    Option.content = Option.createDimmerDiv();
    var content = Option.content;

    var center = WebLibSimple.createAnyAppend("center", content);

    // var input = WebLibSimple.createAnyAppend("input", center);
    // input.style.width = "300px";
    // // input.style.height = "30px";
    // input.type = "text";
    // // input.value = "Hello World!";
    // input.placeholder = "Type here..";

    Option.input = WebLibSimple.createAnyAppend("textarea", center);

    var input = Option.input;
    input.placeholder = "Type here..";

    var div = WebLibSimple.createAnyAppend("div", content);
    div.style.paddingTop = "50px";
    var backButton = DataInterface.createCenterCircle("----", 50, "#000000", div, Option.exitTextField);
}

//
// Date picker
//

Option.exitDate = function()
{
    Option.nukeDimmerDiv();

    var day   = Option.pickerD.value;
    var month = Option.pickerM.value;
    var year  = Option.pickerY.value;

    var date = WebLibSimple.getNiceDateYMD(year, month, day);

    var today = new Date();
    var day   = today.getDate();
    var month = today.getMonth() + 1;
    var year  = today.getFullYear();

    today = WebLibSimple.getNiceDateYMD(year, month, day);

    console.log("date: " + date);
    console.log("today: " + today);

    var target = Option.globalTarget;

    if (date != today)
    {
        target.innerHTML = date;
        WebLibSimple.setBGColor(target, "#ff9100");
        DataInterface.opt[ target.conf.optionKey ] = date;
    }
    else
    {
        WebLibSimple.setBGColor(target, "#335bc3");
        target.innerHTML = target.conf.optionKey;
    }
}

Option.createDateInput = function(label, spec, parent)
{
    var containerDiv = WebLibSimple.createAnyAppend("div", parent);
    containerDiv.style.paddingTop = "50px";

    var labelDiv = WebLibSimple.createAnyAppend("div", containerDiv);
    labelDiv.innerHTML = label;
    labelDiv.style.width = "200px";
    labelDiv.style.display = "inline-block";

    var input = WebLibSimple.createAnyAppend("input", containerDiv);
    input.style.width  = "100px";
    input.style.height = "30px";

    var today = new Date();
    var day   = today.getDate();
    var month = today.getMonth();
    var year  = today.getFullYear();


    if (spec == "DD")
    {
        input.type = "number";
        input.value = day;
        input.min = 1;
        input.max = 31;

        // var monthStart = new Date(year, month,     1);
        // var monthEnd   = new Date(year, month + 1, 1);
        // var monthLength = (monthEnd - monthStart) / (1000 * 60 * 60 * 24)
        // input.max = monthLength;

        Option.pickerD = input;
    }

    if (spec == "MM")
    {
        input.type = "number";
        // wrong month (+ 1)
        input.value = month + 1;
        input.min = 1;
        input.max = 12;

        Option.pickerM = input;
    }

    if (spec == "YYYY")
    {
        input.type = "number";
        input.value = year;
        input.min = year;
        input.max = 3000;

        Option.pickerY = input;
    }
}

Option.buttonEventDate = function(event)
{
    Option.globalTarget = event.target;

    Option.content = Option.createDimmerDiv();
    var content = Option.content;

    var center = WebLibSimple.createAnyAppend("center", content);

    Option.createDateInput("Day:",   "DD", center);
    Option.createDateInput("Month:", "MM", center);
    Option.createDateInput("Year:",  "YYYY", center);

    var div = WebLibSimple.createAnyAppend("div", content);
    div.style.paddingTop = "50px";
    var backButton = DataInterface.createCenterCircle("----", 50, "#000000", div, Option.exitDate);
}

//
// Nummber picker
//

Option.exitNummber = function()
{
    Option.nukeDimmerDiv();
    var target = Option.globalTarget;

    console.log(target.input.value);

    var value = target.input.value;

    if (value)
    {
        WebLibSimple.setBGColor(target, "#ff9100");

        target.innerHTML = "Time: " + value + "min";

        DataInterface.opt[ target.conf.optionKey ] = value;
    }
    else
    {
        WebLibSimple.setBGColor(target, "#335bc3");
    }
}

Option.buttonEventNummber = function(event)
{
    Option.globalTarget = event.target;
    var target = Option.globalTarget;
    var conf = target.conf;

    Option.content = Option.createDimmerDiv();
    var content = Option.content;

    var center = WebLibSimple.createAnyAppend("center", content);

    var containerDiv = WebLibSimple.createAnyAppend("div", center);
    containerDiv.style.paddingTop = "50px";

    var labelDiv = WebLibSimple.createAnyAppend("div", containerDiv);
    labelDiv.innerHTML = "Duration:";
    labelDiv.style.width = "200px";
    labelDiv.style.display = "inline-block";

    target.input = WebLibSimple.createAnyAppend("input", containerDiv);
    var input = target.input;
    input.style.width  = "100px";
    input.style.height = "30px";

    input.type = "number";
    input.placeholder = conf.min;
    input.min         = conf.min;
    input.max         = conf.max;

    var labelDiv = WebLibSimple.createAnyAppend("span", containerDiv);
    labelDiv.innerHTML = "min";
    // labelDiv.style.width = "200px";
    // labelDiv.style.display = "inline-block";
    labelDiv.style.paddingLeft = "10px";
    labelDiv.style.textAlign = "left";

    var div = WebLibSimple.createAnyAppend("div", content);
    div.style.paddingTop = "50px";
    var backButton = DataInterface.createCenterCircle("----", 50, "#000000", div, Option.exitNummber);
}

//
// boolean picker
//

Option.exitBool = function()
{
    Option.nukeDimmerDiv();

    var target = Option.globalTarget;
    var value  = target.value;

    DataInterface.opt[ target.conf.optionKey ] = value;

    console.log("Option.exitBool: " + value);

    if (value)
    {
        WebLibSimple.setBGColor(target, "#3dba42");

    }
    else
    {
        WebLibSimple.setBGColor(target, "#335bc3");
    }
}

Option.boolSelect = function(event)
{
    Option.nukeDimmerDiv();

    var target = Option.globalTarget;
    var value  = event.target.innerHTML;

    console.log("target.conf.optionKey: " + target.conf.optionKey);
    console.log(value);

    if (value == "Yes")
    {
        DataInterface.opt[ target.conf.optionKey ] = true;
        WebLibSimple.setBGColor(target, "#33c345");
    }

    if (value == "No")
    {
        DataInterface.opt[ target.conf.optionKey ] = false;
        WebLibSimple.setBGColor(target, "#c33333");
    }

    if (value == "Neutral")
    {
        DataInterface.opt[ target.conf.optionKey ] = null;
        WebLibSimple.setBGColor(target, "#335bc3");
    }
}

Option.buttonEventBool = function(event)
{
    console.log("PUPS");

    Option.globalTarget = event.target;

    Option.content = Option.createDimmerDiv();
    var content = Option.content;

    //
    // left
    //

    var div  = WebLibSimple.createAnyAppend("div", content);
    div.style.width   = "33%";
    div.style.display = "inline-block";
    // div.onclick = Option.boolSelect;

    var center = WebLibSimple.createAnyAppend("center", div);
    DataInterface.createCircle("Yes", 200, "#c39633", center, Option.boolSelect);

    //
    // middel
    //

    var div = WebLibSimple.createAnyAppend("div", content);
    div.style.width   = "33%";
    div.style.left    = "33%";
    div.style.display = "inline-block";
    // div.onclick = Option.boolSelect;

    var center = WebLibSimple.createAnyAppend("center", div);
    DataInterface.createCircle("Neutral", 200, "#33c37e", center, Option.boolSelect);

    //
    // right
    //

    var div = WebLibSimple.createAnyAppend("div", content);
    div.style.width   = "33%";
    div.style.left    = "66%";
    div.style.display = "inline-block";
    // div.onclick = Option.boolSelect;

    var center = WebLibSimple.createAnyAppend("center", div);
    DataInterface.createCircle("No", 200, "#33c37e", center, Option.boolSelect);

    //
    // exit
    //

    // var div = WebLibSimple.createAnyAppend("div", content);
    // div.style.paddingTop = "50px";
    // var backButton = DataInterface.createCenterCircle("----", 50, "#000000", div, Option.exitBool);
}
