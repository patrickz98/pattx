Edit = {};

Edit.nukeEdit = function()
{
    console.log("--> Edit.nukeEdit");

    var editInfo = Edit.editInfo;
    // console.log(JSON.stringify(editInfo));

    var oldTarget     = editInfo.oldTarget;
    oldTarget.onclick = editInfo.oldEvent;

    var changeDiv = editInfo.contentDiv;
    changeDiv.style.display = "none";
    changeDiv.onclick       = null;
    changeDiv.innerHTML     = "";

    // Error
    Edit.editInfo = null;
}

Edit.finishNewEntry = function(id)
{
    console.log("New id: " + id);

    Edit.newJson[ "id" ] = id;
}

Edit.edit = function(event)
{
    console.log("--> Edit.edit");

    var choice = event.target.choice;
    // console.log("Choice: " + choice);

    var editInfo   = Edit.editInfo;
    var oldTarget  = editInfo.oldTarget;
    var change     = editInfo.input.value;
    var jsonBranch = editInfo.jsonBranch;
    var tag        = editInfo.tag;
    var virgin     = editInfo.virgin;

    // console.log("Change: " + change);
    // console.log("oldTarget.title: " + oldTarget.title);

    if (choice)
    {
        oldTarget.titleSpan.innerHTML = change;
        oldTarget.title               = change;
        jsonBranch[ tag ]             = change;

        // if (jsonBranch.id === undefined)
        // {
        //     console.log("undefined id???");
        //     console.log("??" + JSON.stringify(jsonBranch));
        // }
        //
        // if (jsonBranch.id == null)
        // {
        //     console.log("Null id");
        // }

        if (jsonBranch.id == null)
        {
            console.log("Create New Entry");

            var callback = "Edit.finishNewEntry";

            Edit.newJson = jsonBranch;

            Elastic.postByUuid("teacher", GlobalConf.uuid, jsonBranch, callback);

            Edit.nukeEdit();

            return;
        }

        if (jsonBranch.id != null && jsonBranch.id != undefined)
        {
            console.log("Update Entry");

            var id = jsonBranch.id;
            delete jsonBranch.id;

            Elastic.updateById("teacher", id, jsonBranch);
            jsonBranch.id = id;
        }

        Edit.nukeEdit();
    }
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

    var button = Layout.createCircle("Ok", size, "#04ee85", okButton, Edit.edit);
    button.choice = true;
    // button.style.border = "1px solid #04ee85";

    var noButton = WebLibSimple.createDiv(0, 0, size, 0, null, container);
    noButton.style.left  = null;
    noButton.style.right = 0;

    var button = Layout.createCircle("No", size, "#22252B", noButton, Edit.nukeEdit);
    button.choice = false;
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

Edit.createEdit = function(target, jsonBranch, parent)
{
    console.log("--> New Edit: " + JSON.stringify(jsonBranch));

    if (Edit.editInfo)
    {
        Edit.nukeEdit();
    }

    var borderDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, target);
    borderDiv.style.zIndex = "100";
    borderDiv.style.cursor = "default";
    WebLibSimple.setBGColor(borderDiv, GlobalConf.bubbleColor);

    var oldEvent = target.onclick;
    target.onclick = function()
    {
        console.log("++> Do Nothing");
        return false;
    };

    var containerDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, borderDiv);

    var title   = target.title;
    var input   = Edit.createInput(containerDiv, title);
    var buttons = Edit.createOkNoButton(containerDiv);

    var editInfo = {};
    editInfo.oldTarget  = target;
    editInfo.oldEvent   = oldEvent;
    editInfo.tag        = target.tag;

    editInfo.jsonBranch = jsonBranch;
    editInfo.virgin     = target.virgin;
    editInfo.contentDiv = borderDiv;
    editInfo.input      = input.input;

    Edit.editInfo = editInfo;

    return containerDiv;
}
