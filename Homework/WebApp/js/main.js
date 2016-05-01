Menu = {};

Menu.createMenuPoint = function(title, size, color, parent, event)
{
    var paddingDiv = WebLibSimple.createAnyAppend("div", parent);
    paddingDiv.style.display = "inline-block";
    paddingDiv.style.padding = "20px";

    if (event == null)
    {
        color = "#6b6b6b";
    }

    var div = Layout.createCircle(title, size, color, paddingDiv, event);

    return div;
}

Menu.homework = function()
{
    // Menu.borderDiv.style.display = "none";

    // AddHomework.main(document.body);

    var win = window.open("index.html", "_self");
    win.focus();
}

Menu.frameSetup = function()
{
    //
    // borderDiv
    //

    var border = 10;
    Menu.borderDiv = WebLibSimple.createDiv(border, border, border, border, null, document.body);

    //
    // topDiv
    //

    Menu.topDiv = WebLibSimple.createDiv(0, 0, 0, 0, null, Menu.borderDiv);

    //
    // rows
    //

    // var row1 = WebLibSimple.createDiv(0, 0, 0, "50%", null, Layout.topDiv);
    var center = WebLibSimple.createAnyAppend("center", Menu.topDiv);

    // var case1 = WebLibSimple.createDiv(0, 0, "50%", 0, null, row1);

    var size = 200;

    Menu.createMenuPoint("Subjects", size, "#3688d4", center, null);
    Menu.createMenuPoint("Teacher",  size, "#3688d4", center, null);
    Menu.createMenuPoint("Schedule", size, "#3688d4", center, null);
    Menu.createMenuPoint("Homework", size, "#3688d4", center, Menu.homework);
    Menu.createMenuPoint("Task",     size, "#3688d4", center, null);


    // WebLibSimple.setBGColor(row1, "#d45736");

    // var row2 = WebLibSimple.createDiv(0, "50%", 0, 0, null, Layout.topDiv);
    // WebLibSimple.setBGColor(row2, "#3688d4");

    //
    // Headline
    //

    // Layout.createHeadline("Homework Interface", 100, Layout.topDiv);
}

Menu.frameSetup();
