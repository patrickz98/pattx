Edit = {};

//
// Dimmer stuff
//

Edit.nukeDimmerDiv = function()
{
    Edit.dimmerDiv.style.display = "none";
    Edit.dimmerDiv = null;

    parent.style.overflow = "auto";
}

Edit.createDimmer = function(parent)
{
    parent.style.overflow = "hidden";

    Edit.dimmerDiv = WebLibSimple.createDivHeight(0, parent.scrollTop, 0, "100%", "dimemrDiv", parent);

    var dimmer = Edit.dimmerDiv;
    dimmer.style.fontFamily = GlobalConf.fontFamily;

    WebLibSimple.setBGColor(dimmer, GlobalConf.dimmerDivColor);

    return dimmer;
}

Edit.createOkNoButton = function(parent, size)
{
    var size = parent.offsetHeight;
    var margin = 10;
    var width = size * 2 + margin * 2

    parent.inputContainer.style.right = width + "px";

    var container = WebLibSimple.createDivWidHei(0, 0, width, size, null, parent);
    container.style.left  = null;
    container.style.right = 0;

    var okButton = WebLibSimple.createDiv(margin, 0, size, 0, null, container);

    var button = Layout.createCircle("Ok", size, "#04ee85", okButton);
    // button.style.border = "1px solid #04ee85";

    var noButton = WebLibSimple.createDiv(0, 0, size, 0, null, container);
    noButton.style.left  = null;
    noButton.style.right = 0;

    var button = Layout.createCircle("No", size, "#22252B", noButton);
    // button.style.border = "1px solid #ee6604";
}

Edit.createInput = function(parent, text)
{
    var container = WebLibSimple.createDiv(0, 0, 0, 0, null, parent);
    container.style.borderRadius = "1000px";
    container.style.overflow     = "hidden";

    WebLibSimple.setBGColor(container, GlobalConf.editColor);

    var input = WebLibSimple.createAnyAppend("input", container);
    input.value                 = text;
    input.style.fontSize        = "50px";
    input.style.color           = "#ffffff";
    input.style.textAlign       = "center";
    input.style.lineHeight      = "100px";
    input.style.backgroundColor = "transparent";
    input.style.border          = "0px solid #000000";
    input.style.width           = "100%";
    input.style.height          = "100%";

    // WebLibSimple.setBGColor(container, "#c2f941");

    container.input = input;
    parent.inputContainer = container;

    return container;
}

Edit.createDimmerCircleInputDirekt = function(target, jsonBranch, parent)
{
    var borderDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, target);
    borderDiv.style.zIndex = "100";
    borderDiv.style.cursor = "default";

    var oldEvent = target.onclick;
    target.onclick = function()
    {
        return false;
    };

    // WebLibSimple.setBGColor(borderDiv, "#22cf3a");
    WebLibSimple.setBGColor(borderDiv, GlobalConf.bubbleColor);

    var containerDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, borderDiv);
    // var containerDiv = WebLibSimple.createAnyAppend("div", borderDiv);
    // containerDiv.style.height       = "100%";
    // // containerDiv.style.width        = "80%";
    // containerDiv.style.left         = "0px";
    // containerDiv.style.top          = "0px";
    // containerDiv.style.right        = "0px";
    // containerDiv.style.bottom       = "0px";

    var title = target.title;
    var input = Edit.createInput(containerDiv, title);

    Edit.createOkNoButton(containerDiv);

    return containerDiv;
}

Edit.createDimmerCircleInputKons = function(target, jsonBranch, parent)
{
    var dimmerDiv = Edit.createDimmer(parent);

    var border = 25;
    var borderDiv = WebLibSimple.createDiv(border, border + 100, border, border, null, dimmerDiv);

    var containerDiv = WebLibSimple.createAnyAppend("div", borderDiv);
    containerDiv.style.height       = "100px";
    containerDiv.style.width        = "100%";
    containerDiv.style.borderRadius = "1000px";
    containerDiv.style.overflow     = "hidden";

    WebLibSimple.setBGColor(containerDiv, GlobalConf.editColor);

    var title = target.title;
    var input = Edit.createInput(containerDiv, title);

    return containerDiv;
}

Edit.createDimmerCircleInput = Edit.createDimmerCircleInputDirekt;
