Menu = {};

Menu.conf = {
    colorTrue:  "#2e54e3",
    colorFalse: "#7e7e7e"
};

Menu.homework = function()
{
    var win = window.open("add.html", "_self");
    win.focus();
}

Menu.teacher = function()
{
    var win = window.open("teacher.html", "_self");
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
    Menu.topDiv.style.fontFamily = "Ubuntu, Helvetica, Arial";

    //
    // rows
    //

    // var row1 = WebLibSimple.createDiv(0, 0, 0, "50%", null, Layout.topDiv);
    var center = WebLibSimple.createAnyAppend("center", Menu.topDiv);

    // var case1 = WebLibSimple.createDiv(0, 0, "50%", 0, null, row1);

    var size = 200;

    Layout.createMenuPoint("Subjects", size, Menu.conf.colorTrue, center, null);
    Layout.createMenuPoint("Teacher",  size, Menu.conf.colorTrue, center, Menu.teacher);
    Layout.createMenuPoint("Schedule", size, Menu.conf.colorTrue, center, null);
    Layout.createMenuPoint("Homework", size, Menu.conf.colorTrue, center, Menu.homework);
    Layout.createMenuPoint("Task",     size, Menu.conf.colorTrue, center, null);
    Layout.createMenuPoint("School",   size, Menu.conf.colorTrue, center, null);


    // WebLibSimple.setBGColor(row1, "#d45736");

    // var row2 = WebLibSimple.createDiv(0, "50%", 0, 0, null, Layout.topDiv);
    // WebLibSimple.setBGColor(row2, Menu.conf.colorTrue);

    //
    // Headline
    //

    // Layout.createHeadline("Homework Interface", 100, Layout.topDiv);
}

Menu.frameSetup();
